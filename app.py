import streamlit as st
import numpy as np
from PIL import Image
import re

from ocr.preprocess import preprocess_image
from ocr.ocr_engine import extract_text
from utils.language_detector import detect_best_language, LANGUAGES
from nlp.text_cleaner import clean_ocr_text

st.set_page_config(page_title="Smart Document Intelligence System", layout="wide")
st.title("📄 Smart Document Intelligence System (SDIS)")
st.caption("Marathi → Extract Only IDs | English → Extract Full Text")

uploaded_file = st.file_uploader(
    "Upload Marathi or English Document Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    image_np = np.array(image)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    processed = preprocess_image(image_np)

    detected_lang, _ = detect_best_language(processed)

    st.subheader("🌐 Detected Language")
    st.success(f"{LANGUAGES.get(detected_lang, 'Unknown')} ({detected_lang})")

    if detected_lang == "mar":
        raw_text = extract_text(processed, language="mar+hin+eng")
    elif detected_lang == "eng":
        raw_text = extract_text(processed, language="eng")
    else:
        raw_text = extract_text(processed, language="eng")

    clean_text = clean_ocr_text(raw_text)

    if detected_lang == "mar":
        st.subheader("🆔 Extracted ID(s) from Marathi Text")
        ids = re.findall(r"\b\d+\b", clean_text)

        if ids:
            for i, id_value in enumerate(ids, start=1):
                st.write(f"✅ ID {i}: **{id_value}**")
        else:
            st.warning("No ID number found in Marathi text.")

        with st.expander("📝 Full Marathi OCR Text"):
            st.text(clean_text if clean_text else "No text detected")

    else:
        st.subheader("📝 Extracted English Text")
        if clean_text.strip():
            st.text(clean_text)
        else:
            st.warning("No English text detected.")
