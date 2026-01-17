import re

def extract_fields(text):
    fields = {}

    fields["Emails"] = re.findall(r'\S+@\S+', text)
    fields["Phones"] = re.findall(r'\b\d{10}\b', text)
    fields["Amounts"] = re.findall(r'₹?\s?\d+[.,]?\d*', text)
    fields["Dates"] = re.findall(r'\b\d{2}[/-]\d{2}[/-]\d{4}\b', text)

    return fields
