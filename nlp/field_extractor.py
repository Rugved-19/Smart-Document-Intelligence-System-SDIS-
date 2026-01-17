import re

def extract_fields(text: str) -> dict:
    """
    Example: return numbers, dates, emails, phones, etc.
    """
    fields = {
        "numbers": re.findall(r"\b\d+\b", text),
        "emails": re.findall(r"\S+@\S+", text),
        "phones": re.findall(r"\b\d{10}\b", text)
    }
    return fields
