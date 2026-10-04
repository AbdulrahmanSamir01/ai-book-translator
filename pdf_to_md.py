import os
import re
import logging
from typing import List, Dict
from collections import Counter
import pymupdf  # بديل fitz لتفادي التحذير (DeprecationWarning)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


class PdfToMarkdownConverter:
    """
    تحويل ملف PDF إلى ملفات Markdown منظم مع:
    1. تصفية الصور الصغيرة والأيقونات.
    2. تحديد العناوين استناداً إلى حجم الخط السائد في المستند كاملاً.
    3. استبعاد الصفحات الفارغة ورؤوس/تذييلات الصفحات الضوضائية.
    """

    def __init__(self, pdf_path: str, min_img_width: int = 100, min_img_height: int = 100):
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"ملف PDF غير موجود في المسار: {pdf_path}")
        
        self.pdf_path = pdf_path
        self.doc = pymupdf.open(pdf_path)
        self.min_img_width = min_img_width
        self.min_img_height = min_img_height
        
        # حساب حجم الخط الأساسي العام
        self.base_font_size = self._calculate_global_base_font_size()
        logger.info(f"حجم الخط الأساسي المحدد للمستند: {self.base_font_size:.2f}pt")

    def _calculate_global_base_font_size(self) -> float:
        font_counter = Counter()
        sample_pages = min(len(self.doc), 50)
        
        for page_index in range(sample_pages):
            page_dict = self.doc[page_index].get_text("dict")
            for block in page_dict.get("blocks", []):
                if "lines" in block:
                    for line in block["lines"]:
                        for span in line["spans"]:
                            text = span["text"].strip()
                            if len(text) > 3:
                                rounded_size = round(span["size"] * 2) / 2
                                font_counter[rounded_size] += len(text)

        if not font_counter:
            return 10.0
        
        return font_counter.most_common(1)[0][0]

    def extract_and_save_images(self, output_dir: str) -> Dict[int, List[str]]:
        images_dir = os.path.join(output_dir, "images")
        os.makedirs(images_dir, exist_ok=True)
        page_images_map = {}

        for page_index in range(len(self.doc)):
            page = self.doc[page_index]
            image_list = page.get_images(full=True)
            page_images_map[page_index] = []

            for img_index, img_info in enumerate(image_list, start=1):
                xref = img_info[0]
                base_image = self.doc.extract_image(xref)
                
                if base_image["width"] < self.min_img_width or base_image["height"] < self.min_img_height:
                    continue

                image_bytes = base_image["image"]
                image_ext = base_image["ext"]

                image_name = f"page_{page_index + 1:03d}_img_{img_index:02d}.{image_ext}"
                image_path = os.path.join(images_dir, image_name)

                with open(image_path, "wb") as f:
                    f.write(image_bytes)

                page_images_map[page_index].append(f"images/{image_name}")

        return page_images_map

    def _convert_page_to_markdown(self, page: pymupdf.Page, image_paths: List[str]) -> str:
        page_dict = page.get_text("dict")
        md_blocks = []

        for block in page_dict.get("blocks", []):
            if "lines" not in block:
                continue

            block_lines = []
            for line in block["lines"]:
                line_text = ""
                max_line_font_size = 0.0
                is_bold = False

                for span in line["spans"]:
                    text = span["text"]
                    max_line_font_size = max(max_line_font_size, span["size"])
                    if "bold" in span["font"].lower():
                        is_bold = True
                    line_text += text

                clean_line = line_text.strip()
                
                # استبعاد الأسطر الفارغة أو أرقام الصفحات المجردة
                if not clean_line or (clean_line.isdigit() and len(clean_line) <= 3):
                    continue

                ratio = max_line_font_size / self.base_font_size if self.base_font_size > 0 else 1.0

                if ratio >= 1.5:
                    line_md = f"# {clean_line}"
                elif ratio >= 1.25:
                    line_md = f"## {clean_line}"
                elif ratio >= 1.1:
                    line_md = f"### {clean_line}"
                elif is_bold:
                    line_md = f"**{clean_line}**"
                else:
                    line_md = clean_line

                block_lines.append(line_md)

            if block_lines:
                md_blocks.append("\n".join(block_lines))

        if image_paths:
            img_md = "\n".join([f"![صورة]({img})" for img in image_paths])
            md_blocks.append(img_md)

        return "\n\n".join(md_blocks).strip()

    def convert_and_save_all(self, output_dir: str, single_file: bool = True) -> List[str]:
        """
        الدالة المتوافقة مع main.py والتي تدعم التجميع في ملف واحد أو تقسيم الصفحات.
        """
        os.makedirs(output_dir, exist_ok=True)
        page_images_map = self.extract_and_save_images(output_dir)
        saved_file_paths = []


        if single_file:
            combined_md = []
            for page_index in range(len(self.doc)):
                page = self.doc[page_index]
                images = page_images_map.get(page_index, [])
                page_md = self._convert_page_to_markdown(page, images)

                if not page_md or (len(page_md) < 15 and not images):
                    continue

                # تم حذف الترقيم المتمثل في f"<!-- Page {page_index + 1} -->\n"
                combined_md.append(page_md)

            output_file_path = os.path.join(output_dir, "document_complete.md")
            final_text = re.sub(r"\n{3,}", "\n\n", "\n\n---\n\n".join(combined_md)).strip()
            
            with open(output_file_path, "w", encoding="utf-8") as f:
                f.write(final_text)

            saved_file_paths.append(output_file_path)
            logger.info("تم الحفظ في ملف واحد mdn بنجاح.")

        else:
            for page_index in range(len(self.doc)):
                page = self.doc[page_index]
                images = page_images_map.get(page_index, [])
                page_md = self._convert_page_to_markdown(page, images)

                # فلترة الصفحات الفارغة أو القصيرة جداً
                if not page_md or (len(page_md) < 15 and not images):
                    continue

                file_name = f"page_{page_index + 1:03d}.md"
                file_path = os.path.join(output_dir, file_name)

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(page_md)

                saved_file_paths.append(file_path)

            logger.info(f"تم إنشاء {len(saved_file_paths)} ملف صفحة بنجاح.")

        return saved_file_paths