# Simple fraud detection logic

def detect_fraud(transaction):
    amount = transaction["amount"]
    location = transaction["location"]

    # simple rules
    if amount > 10000:
        return "High Risk"

    if location == "Unknown":
        return "Medium Risk"

    return "Low Risk"


# test data
transaction1 = {"amount": 15000, "location": "Yerevan"}
transaction2 = {"amount": 200, "location": "Unknown"}
transaction3 = {"amount": 100, "location": "Yerevan"}

print(detect_fraud(transaction1))
print(detect_fraud(transaction2))
print(detect_fraud(transaction3))
