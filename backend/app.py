from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ml_model import predict_fraud

app = FastAPI(
    title="AI Fraud Detection API",
    description="Simple prototype for real-time fraud detection",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Transaction(BaseModel):
    amount: float
    country: str
    is_new_device: bool

@app.get("/")
def root():
    return {
        "message": "AI Fraud Detection API is running"
    }

@app.get("/health")
def health():
    return {
        "status": "OK"
    }

@app.post("/predict")
def predict(transaction: Transaction):
    result = predict_fraud(
        amount=transaction.amount,
        country=transaction.country,
        is_new_device=transaction.is_new_device
    )

    return {
        "input": {
            "amount": transaction.amount,
            "country": transaction.country,
            "is_new_device": transaction.is_new_device
        },
        "risk_score": result["risk_score"],
        "decision": result["decision"]
    }
