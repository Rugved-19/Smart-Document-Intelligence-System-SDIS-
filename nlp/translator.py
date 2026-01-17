from transformers import MarianMTModel, MarianTokenizer
import torch
import re

# ---------------- DEVICE ----------------
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# ---------------- MODELS ----------------
MODELS = {
    "hin": "Helsinki-NLP/opus-mt-hi-en",
    "mar": "Helsinki-NLP/opus-mt-mr-en",
    "hye": "Helsinki-NLP/opus-mt-hy-en",
}

# ---------------- CACHE ----------------
_CACHE = {}


def _load_model(lang):
    if lang not in MODELS:
        return None, None

    if lang not in _CACHE:
        tokenizer = MarianTokenizer.from_pretrained(MODELS[lang])
        model = MarianMTModel.from_pretrained(MODELS[lang])
        model.to(DEVICE)
        model.eval()
        _CACHE[lang] = (tokenizer, model)

    return _CACHE[lang]


def _split_preserve_symbols(text):
    """
    Split text while preserving symbols, emojis, and numbers.
    """
    pattern = r"([\U0001F600-\U0001F64F]|[₹$€£%?!()।…]|[0-9]+)"
    return re.split(pattern, text)


def translate_to_english(text: str, lang: str) -> str:
    """
    Robust translation:
    - Line-by-line
    - Preserves symbols & emojis
    - Stable for Marathi / Hindi / Armenian
    """

    if lang == "eng" or not text.strip():
        return text

    tokenizer, model = _load_model(lang)
    if tokenizer is None:
        return text

    translated_lines = []

    for line in text.splitlines():
        if not line.strip():
            translated_lines.append("")
            continue

        parts = _split_preserve_symbols(line)
        translated_line = ""

        for part in parts:
            # Preserve symbols / numbers / emojis
            if re.fullmatch(r"[\U0001F600-\U0001F64F]|[₹$€£%?!()।…]|[0-9]+", part):
                translated_line += part
            else:
                inputs = tokenizer(
                    part,
                    return_tensors="pt",
                    truncation=True,
                    max_length=256
                ).to(DEVICE)

                with torch.no_grad():
                    output = model.generate(
                        **inputs,
                        max_new_tokens=128,
                        num_beams=3,
                        do_sample=False
                    )


                translated_text = tokenizer.decode(
                    output[0],
                    skip_special_tokens=True
                )

                translated_line += translated_text

        translated_lines.append(translated_line.strip())

    return "\n".join(translated_lines)
