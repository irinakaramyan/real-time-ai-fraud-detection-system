from fastapi import FastAPI
from pydantic import BaseModel
from ml_model import predict_fraud

app = FastAPI()

# Request schema
class Transaction(BaseModel):
    amount: float
    country: str
    is_new_device: bool

@app.get("/")
def root():
    return {"message": "Fraud Detection API is running"}

@app.post("/predict")
def predict(transaction: Transaction):
    result = predict_fraud(
        amount=transaction.amount,
        country=transaction.country,
        is_new_device=transaction.is_new_device
    )
    return result
    
