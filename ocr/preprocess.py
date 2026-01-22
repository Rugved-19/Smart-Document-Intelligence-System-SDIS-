import cv2
import numpy as np

def preprocess_image(image):
    """
    High-quality preprocessing for document OCR.
    Works well for Marathi / Hindi / English printed text.
    """

    # Ensure correct format
    if len(image.shape) == 2:
        img = image
    else:
        img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Resize for better OCR (important)
    h, w = gray.shape
    if max(h, w) < 1200:
        gray = cv2.resize(gray, (w * 2, h * 2), interpolation=cv2.INTER_CUBIC)

    # Remove noise while preserving edges
    denoised = cv2.bilateralFilter(gray, 9, 75, 75)

    # Sharpen
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    sharp = cv2.filter2D(denoised, -1, kernel)

    # OTSU Threshold (best for documents)
    _, thresh = cv2.threshold(sharp, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return thresh
