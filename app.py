import streamlit as st
import numpy as np
from PIL import Image

from ocr.paddle_ocr_engine import extract_text_paddle

st.set_page_config(page_title="SDIS - OCR Extractor", layout="wide")
st.title("📄 Smart Document Intelligence System (SDIS)")
st.caption("High Accuracy OCR using PaddleOCR (Best for Marksheet / Aadhaar / Documents)")

uploaded_file = st.file_uploader(
    "Upload Document Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    st.subheader("📝 Extracted Text")
    text = extract_text_paddle(image_np)

    if text.strip():
        st.text(text)
    else:
        st.warning("No text detected. Try uploading a clearer image.")
