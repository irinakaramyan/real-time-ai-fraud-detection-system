System Architecture

High-Level Overview

The system is designed as a modular real-time fraud detection platform that processes transactions, evaluates risk, and generates alerts.

Architecture Components

- Client / Transaction Simulator
- FastAPI Backend
- PostgreSQL Database
- Redis (Real-Time Processing)
- Fraud Rules Engine
- Machine Learning Model
- Decision Engine
- Alerts Module
- Dashboard (Frontend)

Data Flow

1. A transaction is sent to the backend via API.
2. The transaction is stored in PostgreSQL.
3. Redis performs real-time checks (velocity, counters).
4. The Rules Engine evaluates suspicious patterns.
5. The ML Model predicts fraud probability.
6. The Decision Engine calculates the final score.
7. The system classifies the transaction:
   - Approved
   - Under Review
   - Blocked
8. If suspicious, an alert is created.
9. The dashboard displays transactions and alerts.

Architectural Style

The system follows a modular monolithic architecture with clear separation of concerns:
- API Layer
- Business Logic Layer
- Data Layer
- ML Layer
