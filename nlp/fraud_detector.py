def detect_fraud(text, amounts):
    score = 0

    if len(amounts) > 3:
        score += 25
    if any("overwrite" in text.lower() for _ in amounts):
        score += 20
    if any(float(a.replace("₹","").replace(",","")) > 100000 for a in amounts):
        score += 30

    if score > 50:
        return "High Risk"
    elif score > 25:
        return "Medium Risk"
    else:
        return "Low Risk"
