import streamlit as st
import numpy as np
from PIL import Image

from ocr.preprocess import preprocess_image
from ocr.ocr_engine import extract_text
from utils.language_detector import detect_best_language, LANGUAGES
from nlp.text_cleaner import clean_ocr_text
from nlp.translator import translate_to_english
from nlp.field_extractor import extract_fields


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Smart Document Intelligence System",
    layout="wide"
)

st.title("📄 Smart Document Intelligence System")
st.caption("English | Hindi | Marathi | Armenian OCR + Translation")


# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "Upload Document Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    # ---------- Load Image ----------
    image = Image.open(uploaded_file)
    image_np = np.array(image)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    # ---------- Preprocess ----------
    processed = preprocess_image(image_np)

    # ---------- Detect Language ----------
    detected_lang, scores = detect_best_language(processed)

    # ---------- OCR ----------
    if detected_lang == "eng":
        extracted_text = extract_text(processed, "eng")

    elif detected_lang in ["hin", "mar"]:
        extracted_text = extract_text(processed, "mar+hin+eng")

    elif detected_lang == "hye":
        extracted_text = extract_text(processed, "hye")

    else:
        extracted_text = extract_text(processed, "eng")

    # ---------- Display Language ----------
    st.subheader("🌐 Detected Language")
    st.success(f"{LANGUAGES.get(detected_lang, 'Unknown')} ({detected_lang})")

    # ---------- Display OCR ----------
    st.subheader("📝 Extracted Text")
    st.text(extracted_text if extracted_text.strip() else "No text detected")

    # ---------- Clean OCR ----------
    clean_text = clean_ocr_text(extracted_text)

    # ---------- Translation ----------
    if detected_lang in ["mar", "hin"]:
        english_text = translate_to_english(clean_text, detected_lang)
    else:
        english_text = clean_text

    st.subheader("🇬🇧 Translated English Text")
    st.text(english_text if english_text.strip() else "No translation")

    # ---------- Field Extraction ----------
    fields = extract_fields(english_text)

    st.subheader("📌 Extracted Fields")
    st.json(fields)

    # ---------- Debug Scores ----------
    st.subheader("📊 OCR Confidence Scores")
    st.json(scores)
