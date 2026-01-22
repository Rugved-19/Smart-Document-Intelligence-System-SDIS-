import pytesseract
import numpy as np

LANGUAGES = {
    "eng": "English",
    "hin": "Hindi",
    "mar": "Marathi",
    "hye": "Armenian"
}

def ocr_confidence(image, lang):
    data = pytesseract.image_to_data(
        image,
        lang=lang,
        output_type=pytesseract.Output.DICT
    )
    confs = [
        conf for conf in data["conf"]
        if isinstance(conf, (int, float)) and conf > 0
    ]
    if not confs:
        return 0.0
    return float(np.mean(confs))

def detect_best_language(image):
    scores = {}
    for lang in LANGUAGES.keys():
        try:
            scores[lang] = ocr_confidence(image, lang)
        except:
            scores[lang] = 0.0
    best_lang = max(scores, key=scores.get)
    return best_lang, scores
