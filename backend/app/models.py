from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from app.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    country = Column(String, nullable=True)
    device = Column(String, nullable=True)
    status = Column(String, default="approved")
    created_at = Column(DateTime, default=datetime.utcnow)
  
