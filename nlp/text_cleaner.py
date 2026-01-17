import re

def clean_ocr_text(text: str) -> str:
    """
    Clean OCR text for better readability/translation.
    """
    text = re.sub(r"[A-Za-z]{3,}", "", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\.{2,}", "…", text)
    return text.strip()
