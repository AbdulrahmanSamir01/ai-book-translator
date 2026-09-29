import os
import re
from typing import List, Dict, Any


class MarkdownSmartChunker:
    """
    Hierarchical and recursive Markdown chunker that splits content 
    based on heading levels (#, ##, ###) down to paragraph boundaries 
    to ensure no chunk exceeds a maximum token threshold.
    """

    def __init__(self, max_tokens: int = 2000):
        """
        Initialize chunker with target token limit per file/chunk.
        """
        self.max_tokens = max_tokens

    def estimate_tokens(self, text: str) -> int:
        """
        Estimate token count for English/Markdown text.
        A standard rule of thumb: 1 token ≈ 4 characters or 0.75 words.
        
        Algorithm Steps:
        1. Count total characters and words in text.
        2. Calculate weighted token approximation.
        """
        if not text:
            return 0
        word_count = len(text.split())
        char_count = len(text)
        # Conservative token estimation suited for English LLM tokenizers
        return max(int(char_count / 3.8), int(word_count / 0.75))

    def _split_by_pattern(self, text: str, pattern: str) -> List[str]:
        """
        Split text using regex pattern while preserving heading indicators.
        """
        raw_splits = re.split(pattern, text)
        chunks = []
        
        # Re-attach split delimiters if matched
        for part in raw_splits:
            if part and part.strip():
                chunks.append(part.strip())
        return chunks

    def _recursive_split(self, text: str, level: int = 1) -> List[str]:
        """
        Recursively split markdown text by decreasing heading levels (# to ###)
        and finally by paragraphs (\n\n).
        
        Algorithm Steps:
        1. Check if current text is within max_tokens limit.
        2. If over limit, determine delimiter based on hierarchy level.
        3. Split text into sub-blocks.
        4. Recursively process over-limit sub-blocks.
        5. Aggregate small adjacent blocks into a single block under max_tokens.
        """
        # Step 1: Base Case - Text is within token limit
        if self.estimate_tokens(text) <= self.max_tokens:
            return [text]

        # Step 2: Define delimiter hierarchy
        delimiters = {
            1: r"(?=\n# )",       # Split before H1
            2: r"(?=\n## )",      # Split before H2
            3: r"(?=\n### )",     # Split before H3
            4: r"\n\n+"           # Split by Paragraphs
        }

        # Step 3: Handle falling off hierarchy (Fallback to hard character limits if a single paragraph is huge)
        if level not in delimiters:
            return self._hard_split_paragraph(text)

        pattern = delimiters[level]
        sub_blocks = self._split_by_pattern(text, pattern)

        # If splitting at this level produced no division, jump to next level
        if len(sub_blocks) <= 1:
            return self._recursive_split(text, level=level + 1)

        # Step 4: Process sub-blocks recursively and re-aggregate
        final_chunks = []
        current_aggregated = ""

        for block in sub_blocks:
            # If a single block exceeds tokens, break it further down
            if self.estimate_tokens(block) > self.max_tokens:
                # Flush existing aggregated text first
                if current_aggregated:
                    final_chunks.append(current_aggregated.strip())
                    current_aggregated = ""
                
                # Dig deeper into lower hierarchy
                deeper_chunks = self._recursive_split(block, level=level + 1)
                final_chunks.extend(deeper_chunks)
            else:
                # Aggregate adjacent small blocks together up to max_tokens limit
                test_combined = f"{current_aggregated}\n\n{block}".strip()
                if self.estimate_tokens(test_combined) <= self.max_tokens:
                    current_aggregated = test_combined
                else:
                    if current_aggregated:
                        final_chunks.append(current_aggregated.strip())
                    current_aggregated = block

        if current_aggregated:
            final_chunks.append(current_aggregated.strip())

        return final_chunks

    def _hard_split_paragraph(self, text: str) -> List[str]:
        """
        Fallback method to split an oversized single paragraph by sentences or word bounds.
        """
        words = text.split()
        chunks = []
        current_words = []

        for word in words:
            current_words.append(word)
            temp_text = " ".join(current_words)
            if self.estimate_tokens(temp_text) >= self.max_tokens:
                chunks.append(" ".join(current_words[:-1]))
                current_words = [word]

        if current_words:
            chunks.append(" ".join(current_words))

        return chunks

    def process_directory(self, input_dir: str, output_dir: str) -> List[str]:
        """
        Process all .md files in input_dir, chunking oversized files, 
        and save result chunks in output_dir.
        
        Algorithm Steps:
        1. Read all .md files from input_dir.
        2. Evaluate token size for each file.
        3. If <= max_tokens, copy as is. If >, run recursive chunking.
        4. Save generated sub-chunks with systematic naming (e.g. chapter_001_part1.md).
        """
        os.makedirs(output_dir, exist_ok=True)
        generated_files = []

        # Step 1: Iterate over markdown files
        for file_name in sorted(os.listdir(input_dir)):
            if not file_name.endswith(".md"):
                continue

            file_path = os.path.join(input_dir, file_name)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            base_name = os.path.splitext(file_name)[0]

            # Step 2 & 3: Check token size and split recursively
            if self.estimate_tokens(content) <= self.max_tokens:
                out_path = os.path.join(output_dir, f"{base_name}.md")
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(content)
                generated_files.append(out_path)
            else:
                chunks = self._recursive_split(content, level=1)
                for idx, chunk_text in enumerate(chunks, start=1):
                    chunk_file_name = f"{base_name}_part{idx:02d}.md"
                    out_path = os.path.join(output_dir, chunk_file_name)
                    with open(out_path, "w", encoding="utf-8") as f:
                        f.write(chunk_text)
                    generated_files.append(out_path)

        return generated_files


# --- Usage Demonstration ---
if __name__ == "__main__":
    input_folder = "extracted_markdown"
    output_folder = "chunked_markdown"

    chunker = MarkdownSmartChunker(max_tokens=2000)
    result_files = chunker.process_directory(input_folder, output_folder)
    
    print(f"Process complete. Created {len(result_files)} chunked markdown files.")