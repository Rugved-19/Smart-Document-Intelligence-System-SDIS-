def split_by_script(text: str):
    parts = {
        "eng": "",
        "hin_mar": "",
        "armenian": "",
        "symbols": ""
    }

    for ch in text:
        if '\u0900' <= ch <= '\u097F':      # Devanagari
            parts["hin_mar"] += ch
        elif '\u0530' <= ch <= '\u058F':    # Armenian
            parts["armenian"] += ch
        elif ch.isascii() and ch.isalnum():
            parts["eng"] += ch
        else:
            parts["symbols"] += ch

    return parts
