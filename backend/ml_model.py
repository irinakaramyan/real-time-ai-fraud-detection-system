def predict_fraud(amount, country, is_new_device):
    score = 0

    if amount > 1000:
        score += 40

    if country.lower() not in ["armenia", "france"]:
        score += 30

    if is_new_device:
        score += 20

    if score >= 60:
        decision = "BLOCK"
    elif score >= 30:
        decision = "REVIEW"
    else:
        decision = "APPROVE"

    return {
        "risk_score": score,
        "decision": decision
    }
