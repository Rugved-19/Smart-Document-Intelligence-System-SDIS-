import cv2
import numpy as np

def preprocess_image(image):
    """
    Handles grayscale, RGB, RGBA images safely.
    Optimized for OCR (including Armenian).
    """

    # --- Ensure grayscale ---
    if len(image.shape) == 2:
        # Already grayscale
        gray = image

    elif len(image.shape) == 3:
        if image.shape[2] == 3:
            # RGB or BGR
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        elif image.shape[2] == 4:
            # RGBA
            gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
        else:
            raise ValueError("Unsupported image format")

    else:
        raise ValueError("Invalid image shape")

    # --- Contrast enhancement (important for Armenian) ---
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)

    # --- Noise removal ---
    denoised = cv2.fastNlMeansDenoising(enhanced, h=30)

    # --- Adaptive thresholding ---
    thresh = cv2.adaptiveThreshold(
        denoised,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        10
    )

    return thresh
