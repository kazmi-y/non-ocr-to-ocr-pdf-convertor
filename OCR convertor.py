import ocrmypdf
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def add_ocr_to_pdf(input_pdf_path, output_pdf_path, languages='eng'):
    """
    Adds an OCR text layer to a scanned PDF, making it searchable.

    Parameters:
        input_pdf_path (str): Path to the scanned/image-based PDF.
        output_pdf_path (str): Path to save the OCR-enabled PDF.
        languages (str): Language(s) code(s) for OCR (default is English).
    """
    try:
        ocrmypdf.ocr(
            input_pdf_path,
            output_pdf_path,
            language=languages,
            output_type='pdfa',   # Produces PDF/A for long term archiving
            deskew=True,          # Automatically straighten crooked pages
            rotate_pages=True,    # Automatically rotate pages upright
            jobs=2                # Use multiple CPU cores if available
        )
        print(f"OCR completed successfully, saved to {output_pdf_path}")
    except Exception as e:
        print(f"Error during OCR process: {e}")

# Example usage:
input_pdf = r'F:\New folder\OFFICE_ORDER_29072025[1].pdf'
output_pdf = r'F:\New folder\Output.pdf'
add_ocr_to_pdf(input_pdf, output_pdf)
