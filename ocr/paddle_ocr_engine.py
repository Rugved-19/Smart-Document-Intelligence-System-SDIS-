from paddleocr import PaddleOCR

# PaddleOCR v3.x compatible
ocr_model = PaddleOCR(lang="en")  # works for mixed English + Marathi/Hindi documents

def extract_text_paddle(image_np):
    """
    Extract full text using PaddleOCR.
    Compatible with PaddleOCR v3.x
    """
    result = ocr_model.ocr(image_np)

    lines = []
    if not result:
        return ""

    # PaddleOCR output format: list -> each item contains detected text info
    for page in result:
        for line in page:
            text = line[1][0]   # recognized text
            lines.append(text)

    return "\n".join(lines)
