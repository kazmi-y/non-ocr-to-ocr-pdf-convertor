# 📝 OCR PDF Conversion Script

This Python script adds an **OCR text layer** to scanned or image-based PDF files, making them **searchable** and preserving the original formatting.

---

## 🚀 Script Overview

- Uses `ocrmypdf` to add OCR layers to PDFs  
- Leverages `pytesseract` as a Python wrapper for Tesseract OCR  
- Tesseract executable path must be set explicitly  
- Supports deskewing, page rotation, and multi-core processing  

---

## 📜 Script Code

```
import ocrmypdf
import pytesseract

# Set the path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def add_ocr_to_pdf(input_pdf_path, output_pdf_path, languages='eng'):
    """
    Adds an OCR text layer to a scanned PDF, making it searchable.

    Parameters:
    - input_pdf_path (str): Path to the scanned/image-based PDF.
    - output_pdf_path (str): Path to save the OCR-enabled PDF.
    - languages (str): Language(s) code(s) for OCR (default is English).
    """
    try:
        ocrmypdf.ocr(
            input_pdf_path,
            output_pdf_path,
            language=languages,
            output_type='pdfa',    # Produces PDF/A for long term archiving
            deskew=True,           # Automatically straighten crooked pages
            rotate_pages=True,     # Automatically rotate pages upright
            jobs=2                 # Utilize multiple CPU cores
        )
        print(f"✅ OCR completed successfully, saved to {output_pdf_path}")
    except Exception as e:
        print(f"❌ Error during OCR process: {e}")

# Example usage:
input_pdf = r'F:\New folder\OFFICE_ORDER_29072025.pdf'[1]
output_pdf = r'F:\New folder\Output.pdf'

add_ocr_to_pdf(input_pdf, output_pdf)
```

---

## 🛠 How to Use

1. Make sure you have the following installed:  
   - [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) (add to system PATH or set path explicitly)  
   - [Ghostscript](https://ghostscript.com/) (version 9.54+)  
   - Python libraries: `ocrmypdf`, `pytesseract`

2. Update the `input_pdf` and `output_pdf` variables with your file paths.

3. Run the script, and it will generate a searchable PDF at the specified output location.

---

## ⚠️ Notes

- The output PDF is created in **PDF/A** format (archive standard).  
- The script automatically deskews and rotates scanned pages for better OCR accuracy.  
- You can specify additional OCR languages using language codes (e.g., `'eng+fra'`).  
- Make sure the output directory exists and is writable.

---

### 📚 References

- [OCRmyPDF Documentation](https://ocrmypdf.readthedocs.io/)  
- [Tesseract OCR GitHub](https://github.com/tesseract-ocr/tesseract)  
- [pytesseract GitHub](https://github.com/madmaze/pytesseract)

---

✨ *Happy OCR Converting!* ✨
```

[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/51712843/24095234-1e07-46b6-916d-dd1e2a05d9f8/OCR-convertor.py
