# 📝 OCR PDF Conversion Script

This repository contains a Python script that adds an OCR (Optical Character Recognition) text layer to scanned or image-based PDF files, making them searchable and text-extractable while preserving the original visual layout. It uses popular open-source tools like `ocrmypdf` and `pytesseract` along with the Tesseract OCR engine.

---

## 🚦 Step-by-Step Prompt Development (How This Script Was Generated)

### 1. Identify the Requirement
- Extract accurate text from scanned/image-based PDFs that are not OCR compatible
- Convert them into OCR-enabled PDFs or Word documents
- Preserve the formatting as much as possible

### 2. Research OCR Tools
- Explored several Python libraries and tools capable of handling image-based PDFs
- Focused on tools that retain layout and formatting

### 3. Choose OCRmyPDF as a Core Tool
- Selected **OCRmyPDF** for its ability to add an OCR text layer beneath the original scanned image in PDFs
- Maintains visual integrity and makes PDFs searchable

### 4. Handle Text Extraction and OCR
- Chose **Tesseract**, an open-source OCR engine
- Integrated using the `pytesseract` Python wrapper for seamless recognition within the script

### 5. Address Technical Execution Details
- Confirmed that **Tesseract** must be installed and accessible in the system PATH
- Used **PyCharm** as the development environment and resolved path formatting and dependency issues
- Managed system dependencies like **Ghostscript** required by OCRmyPDF

### 6. Write the Script and Test
- Script handles input/output paths and uses multiple CPU cores for performance
- Exception handling added for robust error reporting

---

## ⚙️ How the Script Works

### Dependencies

- **ocrmypdf**: Main library that adds the searchable OCR text layer to PDFs
- **pytesseract**: Python wrapper for the Tesseract OCR engine
- **Tesseract OCR**: Underlying engine that recognizes text from scanned images
- **Ghostscript**: Used by OCRmyPDF for PDF manipulation (must be installed system-wide, version 9.54+)

### Script Components

#### Tesseract Path Configuration

Explicitly set in the script—update if your installation differs:
```
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

#### `add_ocr_to_pdf` Function

**Parameters:**
- `input_pdf_path` : Path to the scanned/image-based PDF
- `output_pdf_path` : Path for the OCR-enabled, searchable PDF
- `languages` : Language code(s) for OCR (default: `'eng'`)

**Calls:**
- `ocrmypdf.ocr()` with:
  - `output_type='pdfa'` (for archiving)
  - `deskew=True` (straighten crooked pages)
  - `rotate_pages=True` (auto-rotate)
  - `jobs=2` (multi-core processing)

Exception handling prints all errors encountered during processing.

#### Example Usage

Update these hardcoded file paths to your actual files:
```
input_pdf = r'F:\New folder\OFFICE_ORDER_29072025.pdf'[1]
output_pdf = r'F:\New folder\Output.pdf'
add_ocr_to_pdf(input_pdf, output_pdf)
```

---

## 🛠 How to Use This Script

### Prerequisites

- **Python 3.6+**
- Install the following system programs:
  - [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) (add to PATH or update in script)
  - [Ghostscript](https://ghostscript.com/download/gsdnld.html) (version 9.54+)

- Python dependencies (install in your environment or globally):
  ```
  pip install ocrmypdf pytesseract
  ```

### Running the Script

1. Edit the script’s `input_pdf` and `output_pdf` paths as needed.
2. Run the script:
   ```
   python OCR-convertor.py
   ```
3. The output will be an OCR-enabled searchable PDF at your specified location.

---

## 💡 Notes & Tips

- Ensure the output folder exists and is writable
- Specify additional languages with `add_ocr_to_pdf(languages='eng+fra')`
- For `.docx` output, additional processing with libraries like `python-docx` is needed
- This script preserves the original PDF’s layout while making the text searchable and copyable

---

## ⚖️ License

This script and repository are provided under the MIT License. Use freely and modify as needed.

---

## 🙏 Acknowledgments

- [OCRmyPDF project](https://github.com/ocrmypdf/OCRmyPDF)
- [Tesseract OCR engine](https://github.com/tesseract-ocr/tesseract)
- [pytesseract wrapper](https://github.com/madmaze/pytesseract)

---

**Feel free to open issues or submit pull requests for improvements!** 🚀
```

[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/51712843/24095234-1e07-46b6-916d-dd1e2a05d9f8/OCR-convertor.py
