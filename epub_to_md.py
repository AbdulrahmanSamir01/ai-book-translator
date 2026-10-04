import os
import re
import logging
from typing import List, Dict, Optional
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from markdownify import markdownify as md

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


class EpubToMarkdownConverter:
    """
    Parses an EPUB file, extracts all images, and converts document items 
    into structured Markdown files strictly following the EPUB spine order.
    """

    def __init__(self, epub_path: str):
        if not os.path.exists(epub_path):
            raise FileNotFoundError(f"EPUB file not found at: {epub_path}")
        
        self.epub_path = epub_path
        self.book = epub.read_epub(epub_path)

    def extract_and_save_images(self, output_dir: str) -> Dict[str, str]:
        """
        Extracts all standard images as well as explicit cover items from the EPUB.
        """
        images_dir = os.path.join(output_dir, "images")
        os.makedirs(images_dir, exist_ok=True)
        
        image_mapping = {}

        image_items = list(self.book.get_items_of_type(ebooklib.ITEM_IMAGE))
        cover_items = list(self.book.get_items_of_type(ebooklib.ITEM_COVER))
        all_image_items = image_items + cover_items

        for item in all_image_items:
            image_name = os.path.basename(item.get_name())
            image_path = os.path.join(images_dir, image_name)

            with open(image_path, "wb") as f:
                f.write(item.get_content())

            rel_path = f"images/{image_name}"
            image_mapping[item.get_name()] = rel_path
            image_mapping[image_name] = rel_path

        return image_mapping

    def _extract_body_markdown(self, soup: BeautifulSoup, image_mapping: Dict[str, str]) -> str:
        """
        Converts <body> HTML content to Markdown and rebinds <img> / <svg> tags to local images.
        """
        body = soup.find("body")
        target_element = body if body else soup

        for element in target_element(["script", "style", "meta"]):
            element.decompose()

        # Update <img> src attributes
        for img_tag in target_element.find_all("img"):
            src = img_tag.get("src", "")
            img_filename = os.path.basename(src)
            if img_filename in image_mapping:
                img_tag["src"] = image_mapping[img_filename]

        # Handle inline SVG images (common in EPUB covers/titlepages)
        for svg_tag in target_element.find_all("svg"):
            image_tag = svg_tag.find("image")
            if image_tag:
                href = image_tag.get("xlink:href") or image_tag.get("href", "")
                img_filename = os.path.basename(href)
                if img_filename in image_mapping:
                    new_img = soup.new_tag("img", src=image_mapping[img_filename])
                    svg_tag.replace_with(new_img)

        raw_markdown = md(
            str(target_element),
            heading_style="ATX",
            strip=["script", "style"]
        )

        clean_markdown = re.sub(r"<\?xml.*?\?>|xml version=.*?\?", "", raw_markdown, flags=re.IGNORECASE)
        clean_markdown = re.sub(r"\n{3,}", "\n\n", clean_markdown).strip()

        return clean_markdown

    def _get_ordered_documents(self) -> List[epub.EpubHtml]:
        """
        Retrieves document items in the EXACT sequence specified by the EPUB spine.
        """
        ordered_items = []
        
        # 1. Read the reading order from spine
        for spine_item in self.book.spine:
            item_id = spine_item[0]
            item = self.book.get_item_with_id(item_id)
            if item and item.get_type() == ebooklib.ITEM_DOCUMENT:
                ordered_items.append(item)

        # 2. Fallback if spine is missing or empty
        if not ordered_items:
            ordered_items = list(self.book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

        return ordered_items

    def convert_and_save_all(self, output_dir: str) -> List[str]:
        os.makedirs(output_dir, exist_ok=True)

        # 1. Save all extracted images
        image_mapping = self.extract_and_save_images(output_dir)

        # 2. Get document pages in strict EPUB Spine Order
        ordered_docs = self._get_ordered_documents()

        chapters = []
        chapter_index = 1

        # 3. Process each document item sequentially
        for item in ordered_docs:
            content_bytes = item.get_content()
            if not content_bytes:
                continue

            soup = BeautifulSoup(content_bytes.decode("utf-8", errors="ignore"), "html.parser")
            cleaned_markdown = self._extract_body_markdown(soup, image_mapping)

            # Skip empty or negligible system files (e.g., empty spacers)
            if not cleaned_markdown or len(cleaned_markdown.strip()) < 5:
                continue

            chapters.append({
                "chapter_index": chapter_index,
                "markdown_content": cleaned_markdown
            })
            chapter_index += 1

        # 4. Save Markdown files strictly numbered by Spine Sequence
        saved_file_paths = []
        for chapter in chapters:
            file_name = f"chapter_{chapter['chapter_index']:03d}.md"
            file_path = os.path.join(output_dir, file_name)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(chapter["markdown_content"])

            saved_file_paths.append(file_path)
            logger.info(f"Saved: {file_name}")

        return saved_file_paths


if __name__ == "__main__":
    sample_epub_path = "2-Find Your Why (Simon Sinek David Mead Peter Docker) (z-library.sk, 1lib.sk, z-lib.sk).epub"
    output_directory = "extracted_markdown"

    try:
        converter = EpubToMarkdownConverter(sample_epub_path)
        generated_files = converter.convert_and_save_all(output_directory)
        logger.info(f"Successfully converted {len(generated_files)} files in correct spine order.")
    except Exception as error:
        logger.error(f"Error during EPUB conversion: {error}")