import os
import re
from typing import List, Dict, Any
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from markdownify import markdownify as md


class EpubToMarkdownConverter:
    """
    Class to parse an EPUB file and convert its contents into structured Markdown chapters,
    filtering out XML declarations and non-body/empty metadata pages.
    """

    def __init__(self, epub_path: str):
        """
        Initialize converter with the path to the EPUB file.
        
        Algorithm Steps:
        1. Validate file existence.
        2. Load EPUB container via ebooklib.
        """
        if not os.path.exists(epub_path):
            raise FileNotFoundError(f"EPUB file not found at: {epub_path}")
        
        self.epub_path = epub_path
        self.book = epub.read_epub(epub_path)

    def _extract_body_markdown(self, soup: BeautifulSoup) -> str:
        """
        Extract content strictly from <body> tag and convert to clean Markdown,
        stripping top-level XML tags and metadata scripts.
        
        Algorithm Steps:
        1. Find <body> tag (or use full soup if missing).
        2. Remove script and style tags.
        3. Convert HTML to Markdown.
        4. Clean up lingering XML declaration artifacts using Regex.
        """
        # Step 1: Target only the body element to skip XML declaration & head
        body = soup.find("body")
        target_element = body if body else soup

        # Step 2: Strip script and style elements
        for element in target_element(["script", "style", "meta"]):
            element.decompose()

        # Step 3: Convert targeted HTML to Markdown
        raw_markdown = md(
            str(target_element),
            heading_style="ATX",
            strip=["script", "style"]
        )

        # Step 4: Regex cleanup for any XML headers that slipped through
        clean_markdown = re.sub(r"<\?xml.*?\?>|xml version=.*?\?", "", raw_markdown, flags=re.IGNORECASE)
        clean_markdown = re.sub(r"\n{3,}", "\n\n", clean_markdown).strip()

        return clean_markdown

    def extract_chapters(self) -> List[Dict[str, Any]]:
        """
        Extract valid body chapters from the EPUB document.
        
        Algorithm Steps:
        1. Iterate through ITEM_DOCUMENT items in the EPUB.
        2. Parse HTML and extract body markdown.
        3. Filter out empty files or single-line XML residual artifacts.
        4. Return clean, numbered chapter dictionaries.
        """
        chapters = []
        chapter_index = 1

        for item in self.book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            content_bytes = item.get_content()
            if not content_bytes:
                continue

            soup = BeautifulSoup(content_bytes.decode("utf-8", errors="ignore"), "html.parser")
            cleaned_markdown = self._extract_body_markdown(soup)

            # Filter out empty files or files containing fewer than 10 characters (like standalone xml strings)
            if not cleaned_markdown or len(cleaned_markdown.strip()) < 10:
                continue

            chapter_info = {
                "id": item.get_id(),
                "file_name": item.get_name(),
                "chapter_index": chapter_index,
                "markdown_content": cleaned_markdown
            }
            
            chapters.append(chapter_info)
            chapter_index += 1

        return chapters

    def convert_and_save_all(self, output_dir: str) -> List[str]:
        """
        Convert all valid chapters and write them to individual .md files.
        """
        os.makedirs(output_dir, exist_ok=True)
        chapters = self.extract_chapters()
        saved_file_paths = []

        for chapter in chapters:
            file_name = f"chapter_{chapter['chapter_index']:03d}.md"
            file_path = os.path.join(output_dir, file_name)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(chapter["markdown_content"])

            saved_file_paths.append(file_path)

        return saved_file_paths


# --- Usage Demonstration ---
if __name__ == "__main__":
    sample_epub_path = "sample_book.epub"
    output_directory = "extracted_markdown"

    try:
        converter = EpubToMarkdownConverter(sample_epub_path)
        generated_files = converter.convert_and_save_all(output_directory)
        print(f"Successfully converted {len(generated_files)} clean chapters.")
    except Exception as error:
        print(f"Error during EPUB conversion: {error}")