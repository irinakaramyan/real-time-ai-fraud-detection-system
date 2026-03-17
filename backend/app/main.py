from fastapi import FastAPI
from app.routes.transactions import router as transaction_router

app = FastAPI(title="Fraud Detection System")

app.include_router(transaction_router, prefix="/transactions", tags=["Transactions"])


@app.get("/")
def root():
    return {"message": "Fraud Detection System is running"}
