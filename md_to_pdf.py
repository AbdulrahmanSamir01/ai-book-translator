import os
import re
import logging
import mimetypes
from typing import Dict, List, Optional
import markdown
from bs4 import BeautifulSoup
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

# إعداد نظام التسجيل (Logging)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


class PDFBookBuilder:
    """
    Builder module to aggregate Markdown files derived from EPUB structures, 
    embed local images properly, and construct a fully formatted RTL Arabic PDF 
    with accurate anchor-to-heading matching and optional closing page.
    """

    def __init__(self, book_title: str, font_path: str, author: str = "Translated Book", language: str = "ar"):
        """
        Initialize PDF metadata, font configurations, and general settings.
        """
        if not os.path.exists(font_path):
            raise FileNotFoundError(f"Font file not found at path: '{font_path}'")
            
        self.book_title = book_title
        self.author = author
        self.language = language
        self.font_path = os.path.abspath(font_path)

    def _get_arabic_css(self) -> str:
        """
        Return modern RTL CSS rules tailored for Arabic typography, images, and PDF layout.
        """
        font_url = f"file:///{self.font_path.replace(os.sep, '/')}"

        return f"""
        @charset "utf-8";
        
        @font-face {{
            font-family: 'CustomArabicFont';
            src: url('{font_url}');
        }}

        @page {{
            size: A4;
            margin: 20mm;
            @bottom-center {{
                content: counter(page);
                font-family: 'CustomArabicFont', sans-serif;
                font-size: 10pt;
            }}
        }}

        /* تم إزالة height: 100% لتجنب انقطاع الصفحات التالية في WeasyPrint */
        html, body {{
            direction: rtl;
            text-align: right;
            font-family: 'CustomArabicFont', sans-serif;
            line-height: 1.8;
            color: #111111;
            background-color: #ffffff;
            margin: 0;
            padding: 0;
        }}

        .chapter {{
            page-break-before: always;
            break-before: page;
        }}

        .chapter.first-chapter {{
            page-break-before: avoid;
            break-before: avoid;
        }}
        
        /* تصميم صفحة الرسالة الختامية للطباعة (تسنطير رأسي وأفقي آمن في WeasyPrint) */
        .closing-page {{
            page-break-before: always;
            break-before: page;
            height: 230mm; /* ارتفاع قريب من مساحة الصفحة المطبوعة بدون تجاوز */
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            box-sizing: border-box;
            padding: 20px;
        }}

        .closing-page-content {{
            max-width: 85%;
            font-size: 1.25em;
            line-height: 2;
            color: #2c3e50;
            white-space: pre-wrap;
        }}

        h1, h2, h3, h4, h5, h6 {{
            font-weight: bold;
            line-height: 1.4;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
            color: #000000;
            page-break-after: avoid;
            break-after: avoid;
        }}
        
        h1 {{ 
            font-size: 2em; 
            border-bottom: 2px solid #eeeeee; 
            padding-bottom: 0.3em;
        }}

        h2 {{ font-size: 1.6em; }}
        h3 {{ font-size: 1.3em; }}
        
        p {{
            margin-top: 0;
            margin-bottom: 1.2em;
            text-align: justify;
            text-justify: inter-word;
        }}

        img {{
            max-width: 100%;
            height: auto;
            display: block;
            margin: 1.5em auto;
            page-break-inside: avoid;
            break-inside: avoid;
        }}
        
        blockquote {{
            margin: 1em 2em 1em 0;
            padding-right: 1em;
            border-right: 4px solid #0056b3;
            border-left: none;
            color: #555555;
            font-style: italic;
        }}
        
        ul, ol {{
            padding-right: 2em;
            padding-left: 0;
            margin-bottom: 1em;
        }}
        
        li {{
            margin-bottom: 0.5em;
        }}

        a {{
            color: #0056b3;
            text-decoration: none;
        }}

        a:hover {{
            text-decoration: underline;
        }}
        
        code {{
            font-family: monospace;
            direction: ltr;
            unicode-bidi: embed;
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 3px;
        }}
        
        pre {{
            direction: ltr;
            text-align: left;
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            padding: 1em;
            overflow-x: auto;
            border-radius: 5px;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 1em;
            page-break-inside: avoid;
            break-inside: avoid;
        }}
        
        th, td {{
            border: 1px solid #dddddd;
            padding: 8px;
            text-align: right;
        }}
        
        th {{
            background-color: #f2f2f2;
        }}
        """

    def _resolve_image_path(self, raw_src: str, input_dir: str, custom_images_dir: Optional[str]) -> Optional[str]:
        """
        Locates the actual image file across multiple potential paths on the local system.
        """
        img_filename = os.path.basename(raw_src)
        possible_paths = []
        
        if custom_images_dir:
            possible_paths.append(os.path.join(custom_images_dir, img_filename))
            possible_paths.append(os.path.join(custom_images_dir, raw_src))
            
        possible_paths.append(os.path.join(input_dir, raw_src))
        possible_paths.append(os.path.join(input_dir, "images", img_filename))
        possible_paths.append(raw_src)

        for path in possible_paths:
            normalized_path = os.path.normpath(path)
            if os.path.isfile(normalized_path):
                return os.path.abspath(normalized_path)
                
        return None

    def _process_images(self, soup: BeautifulSoup, input_dir: str, custom_images_dir: Optional[str]) -> None:
        """
        Finds all <img> tags in the DOM and replaces their src attributes 
        with local file:// URIs so WeasyPrint can load them seamlessly.
        """
        for img_tag in soup.find_all('img', src=True):
            raw_src = img_tag['src'].strip()
            
            if raw_src.startswith(('http://', 'https://', 'data:')):
                continue

            resolved_path = self._resolve_image_path(raw_src, input_dir, custom_images_dir)

            if resolved_path:
                file_uri = f"file:///{resolved_path.replace(os.sep, '/')}"
                img_tag['src'] = file_uri
                logger.info(f"Resolved Image: '{raw_src}' -> '{file_uri}'")
            else:
                logger.warning(f"Image not found for path: '{raw_src}'")

    def _normalize_text(self, text: str) -> str:
        """
        Normalize Arabic text for strict matching: remove punctuation, diacritics, and extra whitespace.
        """
        text = re.sub(r'[^\w\s]', '', text, flags=re.UNICODE)
        return re.sub(r'\s+', ' ', text).strip().lower()

    def _resolve_heading_links(self, soup: BeautifulSoup, toc_file_id: Optional[str] = None) -> BeautifulSoup:
        """
        Target-Only Indexing Engine:
        1. Excludes TOC container/file from heading indexing.
        2. Assigns target IDs exclusively to actual chapter headings.
        3. Maps links in TOC page directly to chapter heading targets.
        """
        heading_map: Dict[str, str] = {}
        
        content_containers = soup.find_all('div', class_='chapter')
        heading_counter = 1

        for container in content_containers:
            if toc_file_id and container.get('id') == toc_file_id:
                continue

            if container.find(class_=re.compile(r'\btoc\b', re.I)):
                headings = [
                    h for h in container.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
                    if not h.find_parent(class_=re.compile(r'\btoc\b', re.I))
                ]
            else:
                headings = container.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

            for heading in headings:
                heading_id = f"target_heading_{heading_counter}"
                heading['id'] = heading_id
                heading_counter += 1
                
                clean_text = self._normalize_text(heading.text)
                if clean_text and clean_text not in heading_map:
                    heading_map[clean_text] = heading_id

        for a_tag in soup.find_all('a', href=True):
            link_text_clean = self._normalize_text(a_tag.text)

            if not link_text_clean:
                continue

            if link_text_clean in heading_map:
                a_tag['href'] = f"#{heading_map[link_text_clean]}"
            else:
                matched_id = None
                for h_text, h_id in heading_map.items():
                    if len(link_text_clean) > 3 and (link_text_clean in h_text or h_text in link_text_clean):
                        matched_id = h_id
                        break
                
                if matched_id:
                    a_tag['href'] = f"#{matched_id}"
                else:
                    a_tag.attrs.pop('href', None)

        return soup

    def build_from_directory(
        self, 
        input_dir: str, 
        output_pdf_path: str, 
        images_dir: Optional[str] = None,
        toc_filename: Optional[str] = None,
        closing_message_file: Optional[str] = None
    ) -> None:
        """
        Read markdown files, parse HTML DOM, resolve local image links, exclude TOC from heading indexing,
        append optional centered closing page, and render PDF.
        """
        if not os.path.exists(input_dir):
            raise FileNotFoundError(f"Input directory '{input_dir}' does not exist.")

        md_files = sorted([f for f in os.listdir(input_dir) if f.endswith(".md")])
        if not md_files:
            raise ValueError(f"No .md files found in '{input_dir}'.")

        md_parser = markdown.Markdown(extensions=["extra", "codehilite", "tables"])
        combined_html_body = ""
        toc_file_id = os.path.splitext(toc_filename)[0] if toc_filename else None

        logger.info(f"Processing {len(md_files)} markdown files for PDF generation...")

        for idx, file_name in enumerate(md_files, start=1):
            file_path = os.path.join(input_dir, file_name)
            
            with open(file_path, "r", encoding="utf-8") as f:
                raw_md = f.read()

            html_chunk = md_parser.convert(raw_md)
            md_parser.reset()

            file_base_id = os.path.splitext(file_name)[0]
            chapter_class = "chapter first-chapter" if idx == 1 else "chapter"
            
            chapter_html = f'<div class="{chapter_class}" id="{file_base_id}">{html_chunk}</div>\n'
            combined_html_body += chapter_html

        # قراءة رسالة الخاتمة وإضافتها كـ HTML في النهاية إن وُجدت
        if closing_message_file:
            if os.path.exists(closing_message_file):
                with open(closing_message_file, "r", encoding="utf-8") as f:
                    closing_text = f.read().strip()

                if closing_text:
                    closing_html = f'''
                    <div class="closing-page">
                        <div class="closing-page-content">{closing_text}</div>
                    </div>
                    '''
                    combined_html_body += closing_html
                    logger.info("Closing page message loaded successfully.")
            else:
                logger.warning(f"Closing message file not found at: '{closing_message_file}'")

        # Step 1: Parse combined HTML DOM tree
        full_soup = BeautifulSoup(combined_html_body, "html.parser")

        # Step 2: Process images and embed local paths
        self._process_images(full_soup, input_dir, images_dir)

        # Step 3: Resolve links and exclude TOC from heading index
        resolved_soup = self._resolve_heading_links(full_soup, toc_file_id=toc_file_id)

        full_html_document = f"""<!DOCTYPE html>
        <html dir="rtl" lang="{self.language}">
        <head>
            <meta charset="utf-8">
            <title>{self.book_title}</title>
            <meta name="author" content="{self.author}">
        </head>
        <body>
            {str(resolved_soup)}
        </body>
        </html>
        """

        # Step 4: Render Final PDF using WeasyPrint
        font_config = FontConfiguration()
        css_obj = CSS(string=self._get_arabic_css(), font_config=font_config)
        html_obj = HTML(string=full_html_document)

        html_obj.write_pdf(target=output_pdf_path, stylesheets=[css_obj], font_config=font_config)
        logger.info(f"PDF document successfully created at: '{output_pdf_path}'")

# --- Usage Demonstration ---
if __name__ == "__main__":
    translated_folder = "temp/LFS-SYSD-BOOK-13.1/translated_markdown"
    custom_images_folder = "extracted_pdf_markdown/images"
    output_pdf = "Arabic_Translated_Book.pdf"
    custom_font = "fonts/ElMessiri.ttf"
    closing_txt_path = "closing_note.txt"  # مسار ملف الرسالة الختامية

    try:
        builder = PDFBookBuilder(
            book_title="العلامة التجارية الشخصية والتسويق الذاتي",
            font_path=custom_font if os.path.exists(custom_font) else "arial.ttf",
            author="مترجم بواسطة الذكاء الاصطناعي",
            language="ar"
        )
        
        builder.build_from_directory(
            input_dir=translated_folder,
            output_pdf_path=output_pdf,
            images_dir=custom_images_folder,
            closing_message_file=closing_txt_path  # تمرير مسار الملف
        )
    except Exception as error:
        logger.error(f"Error building PDF: {error}")