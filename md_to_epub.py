import os
import logging
from typing import Optional
import markdown
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


class EPUBBookBuilder:
    def __init__(
        self, 
        book_title: str, 
        author: str = "Translated Book", 
        language: str = "ar",
        font_path: Optional[str] = None
    ):
        self.book_title = book_title
        self.author = author
        self.language = language
        self.font_path = font_path

    def _get_epub_css(self) -> str:
        font_css = ""
        if self.font_path and os.path.exists(self.font_path):
            font_filename = os.path.basename(self.font_path)
            # تعديل المسار النسبي لأن الـ CSS داخل مجلد style/
            font_css = f"""
            @font-face {{
                font-family: 'CustomArabicFont';
                src: url('../fonts/{font_filename}');
                font-weight: normal;
                font-style: normal;
            }}
            """

        font_family = "'CustomArabicFont', sans-serif" if font_css else "sans-serif"

        return f"""
        @charset "utf-8";
        {font_css}

        html, body {{
            direction: rtl;
            text-align: right;
            font-family: {font_family} !important;
            line-height: 1.8;
            color: #111111;
            background-color: #ffffff;
            margin: 0;
            padding: 1em;
        }}

        .closing-page {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            min-height: 80vh;
            padding: 2em;
            box-sizing: border-box;
        }}

        .closing-page-content {{
            max-width: 85%;
            font-size: 1.25em;
            line-height: 2;
            color: #2c3e50;
            white-space: pre-wrap;
        }}

        h1, h2, h3, h4, h5, h6 {{
            font-family: {font_family} !important;
            font-weight: bold;
            line-height: 1.4;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
            color: #000000;
        }}

        h1 {{ 
            font-size: 1.8em; 
            border-bottom: 2px solid #eeeeee; 
            padding-bottom: 0.3em;
        }}

        p {{
            margin-top: 0;
            margin-bottom: 1.2em;
            text-align: justify;
        }}

        img {{
            max-width: 100%;
            height: auto;
            display: block;
            margin: 1.5em auto;
        }}
        """

    def build_from_directory(
        self,
        input_dir: str,
        output_epub_path: str,
        images_dir: Optional[str] = None,
        closing_message_file: Optional[str] = None
    ) -> None:
        if not os.path.exists(input_dir):
            raise FileNotFoundError(f"Input directory '{input_dir}' does not exist.")

        md_files = sorted([f for f in os.listdir(input_dir) if f.endswith(".md")])
        if not md_files:
            raise ValueError(f"No .md files found in '{input_dir}'.")

        book = epub.EpubBook()
        book.set_title(self.book_title)
        book.set_language(self.language)
        book.add_author(self.author)

        # 1. إضافة الخط المخصص أولاً لتأكيد إدراجه
        if self.font_path and os.path.exists(self.font_path):
            font_filename = os.path.basename(self.font_path)
            ext = os.path.splitext(font_filename)[1].lower()
            media_type = "font/otf" if ext == ".otf" else "font/ttf"

            with open(self.font_path, "rb") as f:
                font_data = f.read()

            font_item = epub.EpubItem(
                uid="custom_font",
                file_name=f"fonts/{font_filename}",
                media_type=media_type,
                content=font_data
            )
            book.add_item(font_item)
            logger.info(f"Custom font '{font_filename}' embedded successfully.")

        # 2. إضافة التنسيقات (CSS)
        css_content = self._get_epub_css()
        style_item = epub.EpubItem(
            uid="style_nav",
            file_name="style/style.css",
            media_type="text/css",
            content=css_content.encode("utf-8")
        )
        book.add_item(style_item)

        # 3. تحويل ملفات الـ Markdown وإضافتها كفصول
        md_parser = markdown.Markdown(extensions=["extra", "codehilite", "tables"])
        epub_chapters = []

        logger.info(f"Processing {len(md_files)} markdown files...")

        for idx, file_name in enumerate(md_files, start=1):
            file_path = os.path.join(input_dir, file_name)
            with open(file_path, "r", encoding="utf-8") as f:
                raw_md = f.read()

            html_body = md_parser.convert(raw_md)
            md_parser.reset()
            soup = BeautifulSoup(html_body, "html.parser")

            chapter_filename = f"chapter_{idx:03d}.xhtml"
            chapter = epub.EpubHtml(
                title=f"Chapter {idx}",
                file_name=chapter_filename,
                lang=self.language
            )
            chapter.set_content(f"""
            <!DOCTYPE html>
            <html dir="rtl" lang="{self.language}">
            <head>
                <meta charset="utf-8"/>
                <link rel="stylesheet" href="style/style.css" type="text/css"/>
            </head>
            <body>
                {str(soup)}
            </body>
            </html>
            """)
            chapter.add_item(style_item)
            book.add_item(chapter)
            epub_chapters.append(chapter)

        # 4. إلغاء الفهرس الافتراضي وتضمين الفصول مباشرة
        book.toc = ()
        book.spine = epub_chapters

        epub.write_epub(output_epub_path, book)
        logger.info(f"EPUB document created successfully at: '{output_epub_path}'")


# --- Usage Demonstration ---
if __name__ == "__main__":
    translated_folder = "temp/LFS-SYSD-BOOK-13.1/translated_markdown"
    custom_images_folder = "extracted_pdf_markdown/images"
    output_book = "Arabic_Translated_Book.epub"
    font_file_path = "fonts/ElMessiri.ttf"
    closing_txt_path = "closing_note.txt"  # مسار ملف الرسالة الختامية

    try:
        builder = EPUBBookBuilder(
            book_title="العلامة التجارية الشخصية والتسويق الذاتي",
            author="مترجم بواسطة الذكاء الاصطناعي",
            language="ar",
            font_path=font_file_path if os.path.exists(font_file_path) else None
        )

        builder.build_from_directory(
            input_dir=translated_folder,
            output_epub_path=output_book,
            images_dir=custom_images_folder,
            closing_message_file=closing_txt_path
        )
    except Exception as error:
        logger.error(f"Error during EPUB build: {error}")