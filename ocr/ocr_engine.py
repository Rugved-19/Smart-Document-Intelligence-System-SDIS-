import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def extract_text(image, language):
    """
    language:
    eng  -> English
    hin  -> Hindi
    mar  -> Marathi
    hye  -> Armenian
    """

    # 🔥 CRITICAL CONFIG
    custom_config = (
        r"--oem 3 "
        r"--psm 6 "
        r"-c preserve_interword_spaces=1"
    )

    return pytesseract.image_to_string(
        image,
        lang=language,
        config=custom_config
    )
