from flask import Flask, request, jsonify

app = Flask(__name__)

def detect_risk(amount, location):
    if amount > 10000:
        return "High Risk"
    if location.lower() == "unknown":
        return "Medium Risk"
    return "Low Risk"

@app.route("/")
def home():
    return "AI Fraud Detection System API is running"

@app.route("/check", methods=["POST"])
def check_transaction():
    data = request.get_json()

    amount = data.get("amount", 0)
    location = data.get("location", "")

    risk = detect_risk(amount, location)

    return jsonify({
        "amount": amount,
        "location": location,
        "risk": risk
    })

if __name__ == "__main__":
    app.run(debug=True)
