import re

def extract_fields(text):
    fields = {}

    fields["Dates"] = re.findall(
        r'\d{2}[./-]\d{2}[./-]\d{4}', text
    )

    fields["Numbers"] = re.findall(
        r'\b\d+\b', text
    )

    fields["Amounts"] = re.findall(
        r'\d+[.,]?\d*', text
    )

    return fields
