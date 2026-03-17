# Simple ML-like fraud detection (simulation)

def predict_fraud(amount, location):
    score = 0

    # feature 1: amount
    if amount > 10000:
        score += 0.7
    elif amount > 5000:
        score += 0.4
    else:
        score += 0.1

    # feature 2: location
    if location.lower() == "unknown":
        score += 0.3

    # decision
    if score > 0.7:
        return "High Risk"
    elif score > 0.4:
        return "Medium Risk"
    else:
        return "Low Risk"
