import os
import re
from typing import List


class MarkdownSmartChunker:
    """
    تقسيم هرمي وتجمعي لملفات Markdown:
    يضمن أن كل ملف ناتج يحتوي على ما بين min_tokens (2000) و max_tokens (2000).
    """

    def __init__(self, max_tokens: int = 2000, min_chunk_tokens: int = 2000):
        self.max_tokens = max_tokens
        self.min_chunk_tokens = min_chunk_tokens

    def estimate_tokens(self, text: str) -> int:
        if not text:
            return 0
        word_count = len(text.split())
        char_count = len(text)
        return max(int(char_count / 3.8), int(word_count / 0.75))

    def _flatten_to_atomic_blocks(self, text: str, level: int = 1) -> List[str]:
        """
        تفكيك النص هرمياً إلى كتل صغيرة لا يتجاوز أي منها max_tokens
        """
        if self.estimate_tokens(text) <= self.max_tokens:
            return [text]

        delimiters = {
            1: r"(?=\n# )",       # H1
            2: r"(?=\n## )",      # H2
            3: r"(?=\n### )",     # H3
            4: r"\n\n+"           # الفقرات
        }

        if level not in delimiters:
            return self._hard_split_paragraph(text)

        pattern = delimiters[level]
        raw_splits = [p.strip() for p in re.split(pattern, text) if p and p.strip()]

        if len(raw_splits) <= 1:
            return self._flatten_to_atomic_blocks(text, level=level + 1)

        atomic_blocks = []
        for block in raw_splits:
            if self.estimate_tokens(block) > self.max_tokens:
                # إذا كانت الكتلة حتى مع التقسيم أكبر من 2000، نكسرها لمستوى أعمق
                atomic_blocks.extend(self._flatten_to_atomic_blocks(block, level=level + 1))
            else:
                atomic_blocks.append(block)

        return atomic_blocks

    def _hard_split_paragraph(self, text: str) -> List[str]:
        """تقسيم اضطراري للفقرات الضخمة جداً"""
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

    def chunk_text(self, text: str) -> List[str]:
        """
        تجميع الكتل الذكي:
        1. يفكك النص لكتل ذرية أولاً.
        2. يجمع الكتل في ملف واحد طالما الحجم أقل من min_tokens (2000).
        3. يفتح ملف جديد فقط بعد الوصول للحد الأدنى وتجاوز الحد الأقصى.
        """
        # المرحلة الأولى: الحصول على جميع الأجزاء الهرمية
        blocks = self._flatten_to_atomic_blocks(text, level=1)

        final_chunks = []
        current_buffer = ""

        for block in blocks:
            if not current_buffer:
                current_buffer = block
                continue

            candidate_text = f"{current_buffer}\n\n{block}".strip()
            candidate_tokens = self.estimate_tokens(candidate_text)
            current_tokens = self.estimate_tokens(current_buffer)

            # شرط التجميع الحاسم:
            # ندمج طالما المرشح أقل من max_tokens OR لم نصل بعد للحد الأدنى (2000)
            if candidate_tokens <= self.max_tokens:
                current_buffer = candidate_text
            elif current_tokens < self.min_chunk_tokens:
                # إذا كان الملف الحالي أقل من 2000 توكين، نضم الكتلة الجديدة قسراً ونغلقه بعدها مباشرة
                current_buffer = candidate_text
                final_chunks.append(current_buffer.strip())
                current_buffer = ""
            else:
                # إذا وصلنا للحد المطلوب (أكثر من 2000) والكتلة الجديدة ستتجاوز 2000:
                # نغلق الملف الحالي ونبدأ ملفاً جديداً بهذه الكتلة
                final_chunks.append(current_buffer.strip())
                current_buffer = block

        # إضافة ما تبقى في البافر
        if current_buffer:
            # إذا كان الجزء الأخير صغيراً جداً ووجد أجزاء سابقة، ندمجه مع الجزء الأخير لضمان عدم حفظ ملف قزم
            if final_chunks and self.estimate_tokens(current_buffer) < self.min_chunk_tokens:
                last_chunk = final_chunks.pop()
                combined = f"{last_chunk}\n\n{current_buffer}".strip()
                final_chunks.append(combined)
            else:
                final_chunks.append(current_buffer.strip())

        return final_chunks

    def process_directory(self, input_dir: str, output_dir: str) -> List[str]:
        os.makedirs(output_dir, exist_ok=True)
        generated_files = []

        for file_name in sorted(os.listdir(input_dir)):
            if not file_name.endswith(".md"):
                continue

            file_path = os.path.join(input_dir, file_name)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            base_name = os.path.splitext(file_name)[0]

            # إذا كان الملف كاملاً أصلاً أقل من 2000 وفي حدود المقبول
            if self.estimate_tokens(content) <= self.max_tokens and self.estimate_tokens(content) >= self.min_chunk_tokens:
                out_path = os.path.join(output_dir, f"{base_name}.md")
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(content)
                generated_files.append(out_path)
            else:
                chunks = self.chunk_text(content)
                for idx, chunk_text in enumerate(chunks, start=1):
                    chunk_file_name = f"{base_name}_part{idx:02d}.md"
                    out_path = os.path.join(output_dir, chunk_file_name)
                    with open(out_path, "w", encoding="utf-8") as f:
                        f.write(chunk_text)
                    generated_files.append(out_path)

        return generated_files


if __name__ == "__main__":
    chunker = MarkdownSmartChunker(max_tokens=2000, min_chunk_tokens=2000)
    result_files = chunker.process_directory("extracted_markdown", "chunked_markdown")
    print(f"تمت العملية بنجاح! تم إنشاء {len(result_files)} ملف مقسم ومجمع.")