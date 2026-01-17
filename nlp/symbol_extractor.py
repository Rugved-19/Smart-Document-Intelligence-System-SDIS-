import re

def extract_symbols(text: str):
    return {
        "laughter": re.findall(r"(🤣|😂|😄|😆)+", text),
        "emphasis": re.findall(r"[!]{2,}", text),
        "ellipsis": re.findall(r"…", text),
        "currency": re.findall(r"[₹$€£]", text),
        "questions": re.findall(r"\?", text),
    }
