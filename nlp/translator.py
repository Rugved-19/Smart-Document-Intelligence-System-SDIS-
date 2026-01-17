from transformers import MarianMTModel, MarianTokenizer
import torch
import re

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

MODELS = {
    "hin": "Helsinki-NLP/opus-mt-hi-en",
    "mar": "Helsinki-NLP/opus-mt-mr-en"
}

_CACHE = {}

def clean_for_translation(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\.{2,}", "…", text)
    return text.strip()

def translate_to_english(text: str, lang: str) -> str:
    if lang not in MODELS or not text.strip():
        return text

    cleaned = clean_for_translation(text)

    if lang not in _CACHE:
        tokenizer = MarianTokenizer.from_pretrained(MODELS[lang])
        model = MarianMTModel.from_pretrained(MODELS[lang]).to(DEVICE)
        model.eval()
        _CACHE[lang] = (tokenizer, model)

    tokenizer, model = _CACHE[lang]

    result_lines = []
    for line in cleaned.splitlines():
        if not line.strip():
            result_lines.append("")
            continue
        inputs = tokenizer(
            line,
            return_tensors="pt",
            truncation=True,
            max_length=256
        ).to(DEVICE)
        with torch.no_grad():
            output = model.generate(**inputs, num_beams=4, do_sample=False)
        result_lines.append(
            tokenizer.decode(output[0], skip_special_tokens=True)
        )
    return "\n".join(result_lines)
