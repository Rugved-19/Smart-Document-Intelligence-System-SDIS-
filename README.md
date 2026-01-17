
# 📄 Smart Document Intelligence System (SDIS) — v1.0 🚀

A multilingual **OCR + Translation** web app built using **Streamlit + Tesseract OCR + Hugging Face MarianMT**.

This is the **first version (v1.0)** of the project focusing on **stability, clean OCR extraction, and correct Marathi/Hindi → English translation**.

---

## ✨ Key Features (v1.0)

✅ Upload document images (JPG / PNG / JPEG)  
✅ OCR for **Marathi, Hindi, English
✅ Smart preprocessing for better OCR results  
✅ Auto language detection (confidence-based)  
✅ Marathi & Hindi text → English translation  
✅ Clean UI with Streamlit  
✅ Field extraction from translated output (basic)  

---

## 🧠 Supported Languages

| Language | OCR | Translation to English |
|---------|-----|------------------------|
| English | ✅ | Not needed |
| Marathi | ✅ | ✅ |
| Hindi   | ✅ | ✅ |

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (UI)
- **OpenCV** (Image preprocessing)
- **Tesseract OCR**
- **Hugging Face Transformers**
- **MarianMT Models**
- **PyTorch**

---

## 📂 Project Folder Structure

```bash
Smart-Document-Intelligence-System-SDIS/
│
├── app.py
├── requirements.txt
├── README.md
│
├── ocr/
│   ├── preprocess.py
│   ├── ocr_engine.py
│
├── nlp/
│   ├── translator.py
│   ├── text_cleaner.py
│   ├── field_extractor.py
│
└── utils/
    ├── language_detector.py
