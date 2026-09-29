import os
import json
import time
from typing import Dict, Any
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()


class GroqBookTranslator:
    """
    Translator module using Groq API with dynamic memory tracking,
    context propagation, and automatic 429 rate-limit handling.
    """

    def __init__(self, api_key: str = None, model_name: str = "qwen/qwen3.8-27b"):
        """
        Initialize Groq client and translator configurations.
        """
        resolved_key = api_key or os.getenv("GROQ_API_KEY")
        
        if not resolved_key or resolved_key == "your_groq_api_key_here":
            raise ValueError("GROQ_API_KEY is missing or invalid. Please set it in your .env file.")
        
        self.client = Groq(api_key=resolved_key)
        self.model_name = model_name

    def _build_system_prompt(self, memory: Dict[str, Any]) -> str:
        """
        Construct system prompt embedding glossary and contextual summary.
        
        Algorithm Steps:
        1. Format existing glossary terms into markdown bullet points.
        2. Format cumulative context summary.
        3. Enforce strict JSON output schema and translation rules.
        """
        glossary_text = "\n".join([f"- {en}: {ar}" for en, ar in memory.get("glossary", {}).items()])
        if not glossary_text:
            glossary_text = "لا توجد مصطلحات محددة بعد."

        summary_text = memory.get("summary_so_far", "بداية الكتاب/الفصل.")

        prompt = f"""You are an expert translator specializing in Personal Branding, Self-Marketing, and Professional Development books.
Translate the provided English Markdown text to professional, inspiring, and clear Arabic suited for business and personal growth literature.

### CRITICAL RULES:
1. Preserve ALL Markdown formatting elements (headings #, bold **, code blocks ```, list items -, links, image tags).
2. Do NOT translate code blocks, variables, URLs, image paths, platform names, or social media handles/hashtags.
3. Adopt a clean, motivating, and highly professional Arabic writing style suited for modern branding and career-growth books.
4. Respect the established Glossary for specialized marketing and personal branding terms.
5. Output MUST be a valid JSON object matching this schema strictly:
{{
  "translated_md": "Full Arabic markdown translated text here...",
  "new_terms": {{"EnglishTerm": "المصطلح بالعربي"}},
  "chapter_summary_update": "A brief 2-sentence summary of what happened in this chunk to append to overall context."
}}

### EXISTING GLOSSARY:
{glossary_text}

### CONTEXT SUMMARY SO FAR:
{summary_text}"""

        return prompt

    def translate_chunk(self, markdown_text: str, memory: Dict[str, Any]) -> Dict[str, Any]:
        """
        Send chunk translation request to Groq API with robust retry mechanism for Rate Limits (429).
        
        Algorithm Steps:
        1. Build prompt using current memory context.
        2. Execute API request inside retry loop with rate-limit detection.
        3. Catch HTTP 429 / Rate Limit errors and enforce full 60-second backoff.
        4. Parse and validate JSON structure before returning.
        """
        system_prompt = self._build_system_prompt(memory)
        
        max_retries = 5
        base_backoff = 5

        for attempt in range(1, max_retries + 1):
            try:
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"Translate this Markdown text:\n\n{markdown_text}"}
                    ],
                    response_format={"type": "json_object"},
                    temperature=0.2
                )
                
                raw_response = response.choices[0].message.content
                parsed_data = json.loads(raw_response)
                return parsed_data

            except Exception as e:
                error_msg = str(e)
                # Detect HTTP 429 Rate Limit error explicitly
                is_rate_limit = "429" in error_msg or "rate_limit_exceeded" in error_msg.lower()
                
                if is_rate_limit:
                    sleep_time = 60
                    print(f"[Rate Limit] Hit API Rate Limit on attempt {attempt}/{max_retries}. Sleeping for {sleep_time} seconds...")
                else:
                    sleep_time = base_backoff * attempt
                    print(f"[Warning] API Error on attempt {attempt}/{max_retries}: {e}. Retrying in {sleep_time}s...")

                if attempt < max_retries:
                    time.sleep(sleep_time)
                else:
                    raise RuntimeError(f"Failed to translate chunk after {max_retries} attempts. Last error: {e}")

    def process_directory(self, input_dir: str, output_dir: str, memory_dir: str) -> None:
        """
        Process all chunked markdown files sequentially, supporting safe resumes and memory tracking.
        
        Algorithm Steps:
        1. Initialize directory structures and load/create memory state.
        2. Scan and sort source markdown files.
        3. Execute continuous skip verification for pre-existing output files.
        4. Perform translation for missing chunks and update memory state.
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

        print(f"Starting translation process for {len(files_to_process)} chunks...")

        # Step 2: Iterate over sorted markdown chunks
        for idx, file_name in enumerate(files_to_process, start=1):
            input_file_path = os.path.join(input_dir, file_name)
            output_file_path = os.path.join(output_dir, file_name)

            # Step 3: Checkpoint Validation - Skip if output exists
            if os.path.exists(output_file_path):
                print(f"[{idx}/{len(files_to_process)}] Skipping {file_name} (Output file already exists)")
                continue

            print(f"[{idx}/{len(files_to_process)}] Translating {file_name} via Groq ({self.model_name})...")
            
            with open(input_file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Step 4: Execute Translation Request
            result = self.translate_chunk(content, memory)

            # Save translated file
            with open(output_file_path, "w", encoding="utf-8") as f:
                f.write(result.get("translated_md", ""))

            # Step 5: Update and persist memory state
            new_terms = result.get("new_terms", {})
            if new_terms:
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

    try:
        translator = GroqBookTranslator(model_name="qwen/qwen3.8-27b")
        translator.process_directory(
            input_dir=input_chunks_folder,
            output_dir=output_translated_folder,
            memory_dir=memory_folder
        )
    except Exception as error:
        print(f"Error during translation process: {error}")