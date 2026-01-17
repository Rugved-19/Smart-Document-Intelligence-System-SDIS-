import re

def clean_ocr_text(text: str) -> str:
    """
    Cleans OCR noise before translation.
    - Removes random Roman garbage
    - Fixes broken punctuation
    - Normalizes spaces
    """

    lines = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue

        # Remove random Roman words (Sat, Rte, Prenat etc.)
        line = re.sub(r"\b[A-Za-z]{3,}\b", "", line)

        # Normalize dots
        line = re.sub(r"\.{2,}", "…", line)

        # Fix broken brackets
        if "(" in line and ")" not in line:
            line = line.replace("(", "")

        # Remove mixed junk numbers like 8८
        line = re.sub(r"\d+[०-९]+|\d+", "", line)

        # Remove extra spaces
        line = re.sub(r"\s+", " ", line).strip()

        if len(line) > 3:
            lines.append(line)

    return "\n".join(lines)
