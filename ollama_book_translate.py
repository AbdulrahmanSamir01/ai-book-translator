import os
import re
import json
import time
from typing import Dict, Any
import ollama


class OllamaBookTranslator:
    """
    Local and Cloud book translation module utilizing Ollama API with dynamic memory tracking,
    context propagation, external prompt file configuration, dynamic retry logic, and robust JSON repair.
    """

    def __init__(
        self, 
        prompt_file_path: str = "prompts/system_prompt.md", 
        model_name: str = "gemma4:31b-cloud",
        max_retries: int = 3
    ):
        """
        Initialize Ollama translator options, system prompt, and retry constraints.
        """
        self.model_name = model_name
        self.prompt_file_path = prompt_file_path
        self.max_retries = max_retries
        self.prompt_template = self._load_system_prompt_template(prompt_file_path)

    def _load_system_prompt_template(self, file_path: str) -> str:
        """Load system prompt template from external markdown file."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"System prompt file not found at: {file_path}")
        
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    def _build_system_prompt(self, memory: Dict[str, Any]) -> str:
        """Construct system prompt by injecting dynamic memory into template."""
        glossary_text = "\n".join([f"- {en}: {ar}" for en, ar in memory.get("glossary", {}).items()])
        if not glossary_text:
            glossary_text = "لا توجد مصطلحات محددة بعد."

        summary_text = memory.get("summary_so_far", "بداية الكتاب/الفصل.")

        prompt = self.prompt_template.format(
            glossary_text=glossary_text,
            summary_text=summary_text
        )

        return prompt


    def _repair_and_parse_json(self, json_str: str) -> Dict[str, Any]:
        """
        Advanced multi-stage JSON repair algorithm for handling LLM JSON generation quirks.
        """
        # Step 1: Direct JSON parsing attempt
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            pass

        # Step 2: Fix unescaped backslashes commonly emitted inside Markdown payloads
        sanitized_str = re.sub(r'\\(?!["\\/bfnrtu])', r'\\\\', json_str)
        try:
            return json.loads(sanitized_str)
        except json.JSONDecodeError:
            pass

        # Step 3: Handle raw control characters / raw unescaped newlines inside strings
        # Replace unescaped newlines inside quotes
        cleaned_control = re.sub(r'(?<!\\)\r?\n', r'\\n', sanitized_str)
        try:
            return json.loads(cleaned_control)
        except json.JSONDecodeError:
            pass

        # Step 4: Fallback to optional third-party library if installed (json_repair)
        try:
            import json_repair
            return json_repair.loads(json_str)
        except ImportError:
            pass

        # If all repairs fail, raise explicit JSONDecodeError for retry mechanism
        return json.loads(json_str)


    def _extract_and_parse_json(self, raw_response: str) -> Dict[str, Any]:
        """
        Robust JSON extraction algorithm preserving internal Markdown formatting.
        """
        if not raw_response or not raw_response.strip():
            raise ValueError("API returned an empty response string.")

        cleaned_text = raw_response.strip()

        # Remove outer JSON markdown block wrapper if LLM wrapped whole payload in ```json ... ```
        if cleaned_text.startswith("```"):
            cleaned_text = re.sub(r"^```(?:json)?\s*", "", cleaned_text, flags=re.IGNORECASE)
            cleaned_text = re.sub(r"\s*```$", "", cleaned_text)

        cleaned_text = cleaned_text.strip()

        # Try parsing full extracted payload
        try:
            return self._repair_and_parse_json(cleaned_text)
        except json.JSONDecodeError:
            # Step 2: Regex extraction for valid object bounds {...}
            json_match = re.search(r"\{.*\}", cleaned_text, re.DOTALL)
            if json_match:
                try:
                    return self._repair_and_parse_json(json_match.group(0))
                except json.JSONDecodeError as err:
                    raise ValueError(f"Extracted string failed JSON parsing: {err}")
            
            raise ValueError(f"Could not locate valid JSON structure inside response payload.")

    def translate_chunk(self, markdown_text: str, memory: Dict[str, Any]) -> Dict[str, Any]:
        """
        Send chunk translation request to Ollama API with automatic retry logic on malformed JSON responses.
        """
        system_prompt = self._build_system_prompt(memory)
        
        # Enhanced instruction reinforcing strict JSON rules
        user_prompt = (
            "Translate the following Markdown text into Arabic.\n"
            "CRITICAL: Output ONLY a valid strictly-formatted JSON object with keys: "
            '"translated_md", "new_terms", and "chapter_summary_update". '
            "Do NOT use raw double quotes inside JSON string values without escaping them (use \\\" instead).\n\n"
            f"Markdown Text:\n{markdown_text}"
        )

        last_exception = None

        for attempt in range(1, self.max_retries + 1):
            try:
                # Lower temperature gradually on retries to enforce stricter formatting compliance
                current_temperature = max(0.0, 0.2 - (attempt - 1) * 0.1)

                response = ollama.chat(
                    model=self.model_name,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    format="json",
                    options={
                        "temperature": current_temperature
                    }
                )

                raw_response = response.get("message", {}).get("content", "")
                parsed_data = self._extract_and_parse_json(raw_response)
                
                # Basic schema validation
                if "translated_md" not in parsed_data:
                    raise ValueError("JSON response missing required key 'translated_md'")

                return parsed_data

            except Exception as e:
                last_exception = e
                print(f"   [Warning] Attempt {attempt}/{self.max_retries} failed for chunk translation: {e}")
                
                if attempt < self.max_retries:
                    sleep_time = attempt * 2
                    print(f"   [Retry] Retrying request in {sleep_time}s with temperature={max(0.0, 0.2 - attempt * 0.1):.1f}...")
                    time.sleep(sleep_time)

        raise RuntimeError(f"Failed to process chunk after {self.max_retries} attempts. Last Error: {last_exception}")

    def process_directory(self, input_dir: str, output_dir: str, memory_dir: str) -> None:
        """
        Process all chunked markdown files sequentially using Ollama engine.
        """
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(memory_dir, exist_ok=True)

        memory_file_path = os.path.join(memory_dir, "memory.json")

        # Step 1: Load or initialize translation memory
        if os.path.exists(memory_file_path):
            with open(memory_file_path, "r", encoding="utf-8") as f:
                memory = json.load(f)
        else:
            memory = {"summary_so_far": "بداية الكتاب.", "glossary": {}}

        files_to_process = sorted([f for f in os.listdir(input_dir) if f.endswith(".md")])

        print(f"Starting translation process via Ollama ({self.model_name}) for {len(files_to_process)} chunks...")

        # Step 2: Iterate over sorted markdown chunks
        for idx, file_name in enumerate(files_to_process, start=1):
            input_file_path = os.path.join(input_dir, file_name)
            output_file_path = os.path.join(output_dir, file_name)

            # Step 3: Checkpoint Validation - Skip if output exists
            if os.path.exists(output_file_path):
                print(f"[{idx}/{len(files_to_process)}] Skipping {file_name} (Output file already exists)")
                continue

            print(f"[{idx}/{len(files_to_process)}] Translating {file_name}...")

            with open(input_file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Step 4: Execute Translation Request with Retries
            result = self.translate_chunk(content, memory)

            # Save translated file
            with open(output_file_path, "w", encoding="utf-8") as f:
                f.write(result.get("translated_md", ""))

            # Step 5: Update and persist memory state safely
            new_terms = result.get("new_terms", {})
            if isinstance(new_terms, dict) and new_terms:
                memory["glossary"].update(new_terms)

            updated_summary = result.get("chapter_summary_update", "")
            if updated_summary:
                memory["summary_so_far"] += f" {updated_summary}"

            with open(memory_file_path, "w", encoding="utf-8") as f:
                json.dump(memory, f, ensure_ascii=False, indent=2)

            print(f"Successfully processed {file_name}. Glossary terms count: {len(memory['glossary'])}")

        print("\nAll chunks processed successfully!")


# --- Usage Demonstration ---
if __name__ == "__main__":
    input_chunks_folder = "chunked_markdown"
    output_translated_folder = "translated_markdown"
    memory_folder = "translation_memory"
    prompt_file = "translator_prompt.md"

    try:
        translator = OllamaBookTranslator(
            prompt_file_path=prompt_file,
            model_name="gemma4:31b-cloud",
            max_retries=3  # عدد المحاولات لكل ملف عند حدوث خطأ
        )
        translator.process_directory(
            input_dir=input_chunks_folder,
            output_dir=output_translated_folder,
            memory_dir=memory_folder
        )
    except Exception as error:
        print(f"Error during local translation process: {error}")