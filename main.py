"""
Book Translation Pipeline Execution Script (EPUB & PDF)

Architecture & Workflow:
1. Argument Parsing & Output Format Flags (--format pdf/epub/both, --closing-file)
2. Format Detection (.epub vs .pdf) & Dynamic Extractor Binding
3. Structural Isolation in workspace: temp/{book_stem}/
4. Sequential Execution Steps:
   - Step 1: EPUB/PDF -> Markdown Extraction
   - Step 2: Markdown Smart Chunking (Token Limiting)
   - Step 3: LLM Translation via Ollama
   - Step 4: Book Generation (PDF, EPUB, or Both with dynamic images_dir & closing_message_file binding)
5. Robust Error Handling & Terminal Logging (OWASP/Clean Code)
"""

import os
import sys
import argparse
from pathlib import Path

# Module Imports
try:
    from epub_to_md import EpubToMarkdownConverter
    from pdf_to_md import PdfToMarkdownConverter
    from md_chunker import MarkdownSmartChunker
    from ollama_book_translate import OllamaBookTranslator
    from md_to_pdf import PDFBookBuilder
    from md_to_epub import EPUBBookBuilder  # كلاس بناء الـ EPUB
except ImportError as err:
    print(f"Import Error: Missing pipeline dependency module. Details: {err}")
    sys.exit(1)


def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments.
    Allows passing the target file, selecting output format (pdf, epub, both),
    and specifying a custom closing note file.
    """
    parser = argparse.ArgumentParser(description="Automated EPUB/PDF to Arabic Translation Pipeline")
    parser.add_argument(
        "file_path",
        type=str,
        nargs="?",
        default=None,
        help="Path to the input EPUB or PDF file"
    )
    parser.add_argument(
        "--format",
        choices=["pdf", "epub", "both"],
        default="both",
        help="Select output format: pdf, epub, or both (default: both)"
    )
    parser.add_argument(
        "--closing-file", "-c",
        type=str,
        default="closing_note.txt",
        help="Path to the closing message text file (default: closing_note.txt)"
    )
    return parser.parse_args()


def extract_markdown(source_file: Path, output_dir: Path) -> list:
    """
    تحديد نوع الملف واستدعاء المحول المناسب بناءً على الامتداد.
    """
    file_ext = source_file.suffix.lower()

    if file_ext == ".epub":
        print("Detected EPUB file format. Using EpubToMarkdownConverter...")
        converter = EpubToMarkdownConverter(str(source_file))
        return converter.convert_and_save_all(str(output_dir))

    elif file_ext == ".pdf":
        print("Detected PDF file format. Using PdfToMarkdownConverter...")
        converter = PdfToMarkdownConverter(
            str(source_file),
            min_img_width=100,
            min_img_height=100
        )
        return converter.convert_and_save_all(str(output_dir), single_file=True)

    else:
        raise ValueError(f"Unsupported file format: '{file_ext}'. Only .epub and .pdf are supported.")


def build_final_books(
    book_stem: str,
    translated_dir: Path,
    images_dir: Path,
    custom_font: Path,
    output_format: str,
    closing_txt_path: Optional[Path] = None
) -> None:
    """
    إنشاء ملفات الكتاب النهائي (PDF أو EPUB أو كلاهما) مع توجيه مسار الصور
    وملف الرسالة الختامية الخياري.
    """
    # تجهيز مجلدات المخرجات
    pdf_output_dir = Path("pdf")
    epub_output_dir = Path("epub")
    
    font_path_str = str(custom_font) if custom_font.exists() else "arial.ttf"
    font_path_epub = str(custom_font) if custom_font.exists() else None
    
    # تحديد مسار ملف الخاتمة إن وجد
    closing_msg_file_str = str(closing_txt_path) if closing_txt_path and closing_txt_path.exists() else None
    if closing_msg_file_str:
        print(f"Loaded closing note from: '{closing_msg_file_str}'")
    else:
        print("No closing note file found. Skipping closing page.")

    # 1. بناء ملف PDF
    if output_format in ["pdf", "both"]:
        pdf_output_dir.mkdir(parents=True, exist_ok=True)
        final_pdf_path = pdf_output_dir / f"{book_stem}_Arabic.pdf"
        print(f"\n[Step 4/4] Building PDF book at '{final_pdf_path}'...")
        try:
            pdf_builder = PDFBookBuilder(
                book_title=book_stem,
                font_path=font_path_str,
                author="مترجم بواسطة الذكاء الاصطناعي",
                language="ar"
            )
            pdf_builder.build_from_directory(
                input_dir=str(translated_dir),
                output_pdf_path=str(final_pdf_path),
                images_dir=str(images_dir) if images_dir.exists() else None,
                closing_message_file=closing_msg_file_str
            )
            print("PDF generation completed successfully.")
        except Exception as error:
            print(f"Error building PDF: {error}")

    # 2. بناء ملف EPUB
    if output_format in ["epub", "both"]:
        epub_output_dir.mkdir(parents=True, exist_ok=True)
        final_epub_path = epub_output_dir / f"{book_stem}_Arabic.epub"
        print(f"\n[Step 4/4] Building EPUB book at '{final_epub_path}'...")
        try:
            epub_builder = EPUBBookBuilder(
                book_title=book_stem,
                author="مترجم بواسطة الذكاء الاصطناعي",
                language="ar",
                font_path=font_path_epub
            )
            epub_builder.build_from_directory(
                input_dir=str(translated_dir),
                output_epub_path=str(final_epub_path),
                images_dir=str(images_dir) if images_dir.exists() else None,
                closing_message_file=closing_msg_file_str
            )
            print("EPUB generation completed successfully.")
        except Exception as error:
            print(f"Error building EPUB: {error}")


def execute_pipeline(file_path: str, output_format: str = "both", closing_file: str = "closing_note.txt") -> None:
    """
    Executes the sequential end-to-end processing pipeline for a given EPUB or PDF file.
    """
    source_file = Path(file_path).resolve()
    
    if not source_file.exists():
        print(f"Error: Target file does not exist at '{source_file}'")
        sys.exit(1)
        
    if source_file.suffix.lower() not in [".epub", ".pdf"]:
        print(f"Error: File '{source_file.name}' is not a valid .epub or .pdf file.")
        sys.exit(1)

    # Base workspace setup: temp/{book_stem}/
    book_stem = source_file.stem
    base_temp_dir = Path("temp") / book_stem
    
    extracted_md_dir = base_temp_dir / "extracted_markdown"
    images_dir = extracted_md_dir / "images"  # المسار الديناميكي للصور المستخرجة
    chunked_md_dir = base_temp_dir / "chunked_markdown"
    translated_md_dir = base_temp_dir / "translated_markdown"
    memory_dir = base_temp_dir / "translation_memory"
    
    prompt_file = Path("translator_prompt.md")
    custom_font = Path("fonts/ElMessiri.ttf")
    closing_txt_path = Path(closing_file)

    print(f"--- Starting Pipeline for: {source_file.name} ---")
    print(f"Workspace Directory: {base_temp_dir.resolve()}")
    print(f"Extracted Images Directory: {images_dir.resolve()}")

    # -------------------------------------------------------------------------
    # Step 1: Convert EPUB/PDF to Clean Markdown
    # -------------------------------------------------------------------------
    print("\n[Step 1/4] Extracting Markdown & Images from source file...")
    try:
        generated_files = extract_markdown(source_file, extracted_md_dir)
        print(f"Step 1 Complete: Successfully extracted {len(generated_files)} markdown files.")
    except Exception as error:
        print(f"Error during extraction step: {error}")
        sys.exit(1)

    # -------------------------------------------------------------------------
    # Step 2: Markdown Smart Chunking
    # -------------------------------------------------------------------------
    print("\n[Step 2/4] Chunking Markdown files by token count...")
    try:
        chunker = MarkdownSmartChunker(max_tokens=2000)
        result_files = chunker.process_directory(str(extracted_md_dir), str(chunked_md_dir))
        print(f"Step 2 Complete: Created {len(result_files)} chunked markdown files.")
    except Exception as error:
        print(f"Error during Markdown chunking step: {error}")
        sys.exit(1)

    # -------------------------------------------------------------------------
    # Step 3: LLM Translation via Ollama
    # -------------------------------------------------------------------------
    print("\n[Step 3/4] Translating content with Ollama model...")
    try:
        translator = OllamaBookTranslator(
            prompt_file_path=str(prompt_file),
            model_name="gemma4:31b-cloud"
        )
        translator.process_directory(
            input_dir=str(chunked_md_dir),
            output_dir=str(translated_md_dir),
            memory_dir=str(memory_dir)
        )
        print("Step 3 Complete: Translation processed successfully.")
    except Exception as error:
        print(f"Error during local translation process step: {error}")
        sys.exit(1)

    # -------------------------------------------------------------------------
    # Step 4: Build Output Books (PDF / EPUB / Both)
    # -------------------------------------------------------------------------
    build_final_books(
        book_stem=book_stem,
        translated_dir=translated_md_dir,
        images_dir=images_dir,
        custom_font=custom_font,
        output_format=output_format,
        closing_txt_path=closing_txt_path
    )

    print(f"\n=== Pipeline Completed Successfully for {source_file.name} ===")


if __name__ == "__main__":
    args = parse_arguments()
    
    default_file = "LFS-SYSD-BOOK-13.1.pdf"
    input_file = args.file_path or default_file
    
    execute_pipeline(
        file_path=input_file,
        output_format=args.format,
        closing_file=args.closing_file
    )