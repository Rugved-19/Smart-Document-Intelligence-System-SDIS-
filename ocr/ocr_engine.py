import pytesseract

# ✅ Update this path if your tesseract is installed somewhere else
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image, language="eng"):
    config = r"--oem 3 --psm 6 -c preserve_interword_spaces=1"
    return pytesseract.image_to_string(image, lang=language, config=config)
