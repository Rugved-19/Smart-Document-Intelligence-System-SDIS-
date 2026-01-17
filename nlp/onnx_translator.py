from transformers import MarianTokenizer
import onnxruntime as ort

MODELS = {
    "hin": "onnx_models/hi_en",
    "mar": "onnx_models/mr_en",
    "hye": "onnx_models/hy_en",
}

_sessions = {}
_tokenizers = {}

def translate_to_english(text, lang):
    if lang == "eng" or not text.strip():
        return text

    if lang not in MODELS:
        return text

    if lang not in _sessions:
        _tokenizers[lang] = MarianTokenizer.from_pretrained(MODELS[lang])
        _sessions[lang] = ort.InferenceSession(
            f"{MODELS[lang]}/model.onnx",
            providers=["CPUExecutionProvider"]
        )

    tokenizer = _tokenizers[lang]
    session = _sessions[lang]

    inputs = tokenizer(text, return_tensors="np", truncation=True)
    outputs = session.run(None, dict(inputs))
    return tokenizer.decode(outputs[0][0], skip_special_tokens=True)