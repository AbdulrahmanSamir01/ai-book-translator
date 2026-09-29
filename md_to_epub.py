import os
import re
from typing import List
import markdown
from bs4 import BeautifulSoup
from ebooklib import epub


class EPUBBookBuilder:
    """
    Builder module to aggregate translated Markdown files and construct a 
    fully formatted RTL Arabic EPUB 3 book with embedded CSS styles.
    """

    def __init__(self, book_title: str, author: str = "Translated Book", language: str = "ar"):
        """
        Initialize EPUB metadata and core layout configurations.
        """
        self.book_title = book_title
        self.author = author
        self.language = language
        
        # Initialize EPUB Book object
        self.book = epub.EpubBook()
        self.book.set_title(self.book_title)
        self.book.set_language(self.language)
        self.book.add_author(self.author)
        
        # Set RTL direction metadata for EPUB readers
        self.book.direction = "rtl"

    def _get_arabic_css(self) -> str:
        """
        Return modern RTL CSS rules tailored for Arabic typography and readers.
        
        Algorithm Steps:
        1. Set global document direction to RTL.
        2. Adjust typography (line-height, margins, font sizes).
        3. Style code blocks, quotes, tables, and headers for RTL flow.
        """
        return """
        @charset "utf-8";
        
        html, body {
            direction: rtl;
            text-align: right;
            font-family: "Amiri", "Traditional Arabic", "Segoe UI", Arial, sans-serif;
            line-height: 1.8;
            margin: 5%;
            padding: 0;
            color: #111111;
            background-color: #ffffff;
        }
        
        h1, h2, h3, h4, h5, h6 {
            font-weight: bold;
            line-height: 1.4;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
            color: #000000;
            page-break-after: avoid;
        }
        
        h1 { font-size: 2em; border-bottom: 2px solid #eeeeee; padding-bottom: 0.3em; }
        h2 { font-size: 1.6em; }
        h3 { font-size: 1.3em; }
        
        p {
            margin-top: 0;
            margin-bottom: 1.2em;
            text-align: justify;
            text-justify: inter-word;
        }
        
        blockquote {
            margin: 1em 2em 1em 0;
            padding-right: 1em;
            border-right: 4px solid #0056b3;
            border-left: none;
            color: #555555;
            font-style: italic;
        }
        
        ul, ol {
            padding-right: 2em;
            padding-left: 0;
            margin-bottom: 1em;
        }
        
        li {
            margin-bottom: 0.5em;
        }
        
        code {
            font-family: "Courier New", Courier, monospace;
            direction: ltr;
            unicode-bidi: embed;
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 3px;
        }
        
        pre {
            direction: ltr;
            text-align: left;
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            padding: 1em;
            overflow-x: auto;
            border-radius: 5px;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 1em;
        }
        
        th, td {
            border: 1px solid #dddddd;
            padding: 8px;
            text-align: right;
        }
        
        th {
            background-color: #f2f2f2;
        }
        """

    def build_from_directory(self, input_dir: str, output_epub_path: str) -> None:
        """
        Read markdown chunks from input directory, parse HTML, inject CSS, and package EPUB.
        
        Algorithm Steps:
        1. Read and sort all translated .md files in input_dir.
        2. Convert Markdown content to HTML using extensions (tables, codehilite).
        3. Wrap converted HTML inside BeautifulSoup to enforce RTL attributes on section roots.
        4. Create EpubHtml chapters and attach them to the book instance.
        5. Generate Table of Contents (TOC) and NCX navigation.
        6. Write EPUB file to output path.
        """
        if not os.path.exists(input_dir):
            raise FileNotFoundError(f"Input directory '{input_dir}' does not exist.")

        md_files = sorted([f for f in os.listdir(input_dir) if f.endswith(".md")])
        if not md_files:
            raise ValueError(f"No .md files found in '{input_dir}'.")

        # Step 1: Add Custom CSS Item
        css_style = epub.EpubItem(
            uid="style_rtl",
            file_name="style/style.css",
            media_type="text/css",
            content=self._get_arabic_css()
        )
        self.book.add_item(css_style)

        chapters: List[epub.EpubHtml] = []
        md_parser = markdown.Markdown(extensions=["extra", "codehilite", "tables", "toc"])

        print(f"Building EPUB from {len(md_files)} markdown files...")

        # Step 2: Convert each markdown chunk into an EPUB chapter
        for idx, file_name in enumerate(md_files, start=1):
            file_path = os.path.join(input_dir, file_name)
            
            with open(file_path, "r", encoding="utf-8") as f:
                raw_md = f.read()

            # Convert MD to HTML
            html_content = md_parser.convert(raw_md)
            md_parser.reset()

            # Parse HTML with BeautifulSoup to add RTL wrappers
            soup = BeautifulSoup(html_content, "html.parser")
            
            # Extract title from first H1 or construct fall-back
            h1_tag = soup.find("h1")
            chapter_title = h1_tag.text.strip() if h1_tag else f"الفصل {idx}"

            chapter_filename = f"chap_{idx:03d}.xhtml"
            
            # Create EPUB HTML Chapter
            chapter = epub.EpubHtml(
                title=chapter_title,
                file_name=chapter_filename,
                lang=self.language,
                uid=f"chapter_{idx}"
            )
            
            # Set body content with RTL attributes
            chapter.set_content(
                f'<html dir="rtl" lang="ar"><head></head><body>{str(soup)}</body></html>'
            )
            chapter.add_item(css_style)
            
            self.book.add_item(chapter)
            chapters.append(chapter)

        # Step 3: Configure Navigation Table of Contents (TOC) & Spine
        self.book.toc = tuple(chapters)
        self.book.add_item(epub.EpubNcx())
        self.book.add_item(epub.EpubNav())

        # Define reading order (spine)
        self.book.spine = ["nav"] + chapters

        # Step 4: Write EPUB File
        epub.write_epub(output_epub_path, self.book, {})
        print(f"\nEPUB book successfully created at: '{output_epub_path}'")


# --- Usage Demonstration ---
if __name__ == "__main__":
    translated_folder = "translated_markdown"
    output_book = "Arabic_Translated_Book.epub"

    try:
        builder = EPUBBookBuilder(
            book_title="العلامة التجارية الشخصية والتسويق الذاتي",
            author="مترجم بوااسطة الذكاء الاصطناعي",
            language="ar"
        )
        builder.build_from_directory(
            input_dir=translated_folder,
            output_epub_path=output_book
        )
    except Exception as error:
        print(f"Error building EPUB: {error}")