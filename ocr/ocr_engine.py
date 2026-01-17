import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image, language="eng"):
    """
    Extract text using Tesseract.
    """
    config = r"--oem 3 --psm 6 -c preserve_interword_spaces=1"
    return pytesseract.image_to_string(
        image,
        lang=language,
        config=config
    )
