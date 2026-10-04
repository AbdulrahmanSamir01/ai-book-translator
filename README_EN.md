# 📚 AI Book Translator

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[النسخة العربية (Arabic Version)](README.md)

A CLI tool for translating books and documents using AI models while preserving layout and structure, with support for exporting to multiple formats.

---

## 📖 About

The project processes and translates books through an automated pipeline:

1. **Format Conversion:** Converts **PDF** or **EPUB** files into **Markdown** documents.
2. **Smart Chunking:** Splits large files into text chunks optimized for the LLM context window.
3. **Translation:** Translates text chunks into Arabic using the `gemma4:cloud` model via **Ollama**.
4. **Final Export:** Re-assembles translated texts and exports them into publishable **PDF** and **EPUB** books.

---

## 🛠️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/AbdulrahmanSamir01/ai-book-translator.git
cd ai-book-translator
````

### 2. Configure Ollama & Cloud Model

1. Download and install [Ollama](https://ollama.com/).
    
      
    
2. Create an account on Ollama to access the free tier (supports translating ~10 books per week via cloud models).
    
      
    
3. Run the following command to link and pull the `gemma4:cloud` model:
    
      
    

Bash

```
ollama run gemma4:cloud
```

### 3. Virtual Environment & Dependencies Setup

- **Create a virtual environment:**
    
      
    
    Bash
    
    ```
    python -m venv venv
    ```
    
- **Activate the virtual environment:**
    
      
    - On **Linux / macOS**:
        
          
        
        Bash
        
        ```
        source venv/bin/activate
        ```
        
    - On **Windows**:
        
          
        
        DOS
        
        ```
        venv\Scripts\activate
        ```
        
- **Install required packages:**
    
      
    
    Bash
    
    ```
    pip install -r pip.txt
    ```
    

## 🚀 Usage

### 1. Translate & Export to Both Formats (PDF & EPUB) — Default

Bash

```
python main.py path/to/book.pdf
# or
python main.py path/to/book.epub
```

### 2. Export to PDF Only

Bash

```
python main.py path/to/book.epub --format pdf
```

### 3. Export to EPUB Only

Bash

```
python main.py path/to/book.pdf --format epub
```

## 📄 License

This project is licensed under the **GNU General Public License v3.0 (GPLv3)** — see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.
