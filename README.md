# 📚 AI Book Translator

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[English Version](README_EN.md) 

أداة سطر أوامر (CLI) لترجمة الكتب والمستندات الذكية مع الحفاظ على هيكلية النشر والتصدير بصيغ متعددة.

---

## 📖 حول المشروع (About)

يقوم المشروع بمعالجة وترجمة الكتب عبر خط إنتاج متكامل يمر بالخطوات التالية:

1. **تحويل الصيغ:** تحويل ملفات **PDF** أو **EPUB** إلى مستندات **Markdown**.
2. **التجزئة الذكية:** تقسيم الملفات الكبيرة إلى أجزاء (Chunks) تناسب نافذة السياق لنموذج الذكاء الاصطناعي.
3. **الترجمة:** إرسال الأجزاء لترجمتها إلى اللغة العربية عبر نموذج `gemma4:cloud` باستخدام أداة **Ollama**.
4. **التصدير النهائي:** إعادة تجميع النصوص المترجمة وتصديرها ككتب جاهزة بصيغتي **PDF** و **EPUB**.

---

## 🛠️ متطلبات الإعداد والتثبيت (Setup & Installation)

### 1. استنساخ المستودع

```bash
git clone https://github.com/AbdulrahmanSamir01/ai-book-translator.git
cd ai-book-translator

```

### 2. إعداد Ollama والنموذج السحابي

1. قم بتنزيل وتثبيت أداة [Ollama](https://ollama.com/).
2. أنشئ حسابًا على موقع Ollama للاستفادة من الخطة المجانية (تسمح بترجمة ما يقارب 10 كتب أسبوعيًا عبر النماذج السحابية).
3. قم بتشغيل الأمر التالي لربط وتجهيز نموذج `gemma4:cloud`:

```bash
ollama run gemma4:cloud

```

### 3. إعداد البيئة الافتراضية وتثبيت المكتبات

* **إنشاء البيئة الافتراضية:**
```bash
python -m venv venv

```


* **تفعيل البيئة الافتراضية:**
* على نظام **Linux / macOS**:
```bash
source venv/bin/activate

```


* على نظام **Windows**:
```cmd
venv\Scripts\activate

```




* **تثبيت المكتبات المطلوبة:**
```bash
pip install -r pip.txt

```



---

## 🚀 طريقة الاستخدام (Usage)

### 1. الترجمة والتصدير بالصيغتين معًا (PDF & EPUB) — الوضع الافتراضي

```bash
python main.py path/to/book.pdf
# أو
python main.py path/to/book.epub

```

### 2. التصدير لصيغة PDF فقط

```bash
python main.py path/to/book.epub --format pdf

```

### 3. التصدير لصيغة EPUB فقط

```bash
python main.py path/to/book.pdf --format epub

```

---

## 📄 الترخيص (License)

هذا المشروع مرخص تحت رخصة **GNU General Public License v3.0 (GPLv3)** — راجع ملف [LICENSE](https://www.google.com/search?q=LICENSE) لمزيد من التفاصيل.
