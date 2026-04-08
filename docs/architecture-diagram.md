# 🛡️ AI Fraud Detection System

A full-stack, real-time financial fraud detection platform built with Python (Flask), MySQL, and Machine Learning. Combines rule-based heuristics with an Isolation Forest + Random Forest ensemble to score, flag, and alert on suspicious transactions.

---

## 📐 System Architecture

```mermaid
flowchart TB
    subgraph CLIENT["🌐 Client Layer (Browser)"]
        direction LR
        UI1[Dashboard]
        UI2[Transactions]
        UI3[Alerts]
        UI4[Submit Transaction]
    end

    subgraph API["⚙️ Flask REST API Layer"]
        direction LR
        A1["/api/auth"]
        A2["/api/transactions"]
        A3["/api/alerts"]
        A4["/api/dashboard"]
        A5["/api/customers"]
    end

    subgraph SERVICES["🔍 Fraud Detection Services"]
        direction TB
        FD["Fraud Detector\n(Orchestrator)"]
        RE["Rule Engine\n(6 Active Rules)"]
        ML["ML Service\n(Isolation Forest + RF)"]
        FD --> RE
        FD --> ML
    end

    subgraph MLMODELS["🤖 ML Models (scikit-learn)"]
        direction LR
        ISO["Isolation Forest\n(Unsupervised)"]
        RFC["Random Forest\n(Supervised)"]
        SCL["Standard Scaler\n(Feature Normalization)"]
    end

    subgraph DB["🗄️ MySQL Database"]
        direction LR
        T1[(users)]
        T2[(customers)]
        T3[(transactions)]
        T4[(fraud_alerts)]
        T5[(risk_scores)]
        T6[(fraud_rules)]
    end

    CLIENT -- "HTTP + JWT" --> API
    API --> SERVICES
    ML --> MLMODELS
    SERVICES --> DB
    API --> DB
```

---

## 🔄 Fraud Detection Flow

```mermaid
flowchart LR
    TXN["📥 Incoming\nTransaction"] --> VAL["Validate &\nStore"]
    VAL --> RULE["Rule Engine\n──────────\n• Large Amount >$10K\n• Unusual Hours 1am–5am\n• High Frequency >5/hr\n• International Location\n• Round Amount\n• Amount Deviation 3σ"]
    VAL --> MLPIPE["ML Pipeline\n──────────\n1. Extract 10 Features\n2. Normalize (Scaler)\n3. Isolation Forest Score\n4. Random Forest Prob."]
    RULE -- "Rule Score (0–1)\nWeight: 40%" --> COMBINE
    MLPIPE -- "ML Score (0–1)\nWeight: 60%" --> COMBINE
    COMBINE["Combined Risk Score\n= 0.4×Rule + 0.6×ML"] --> DECIDE

    DECIDE{Risk Score?}
    DECIDE -- "< 0.50" --> APPROVED["✅ APPROVED"]
    DECIDE -- "0.50 – 0.79" --> FLAGGED["⚠️ FLAGGED\n+ Alert Generated"]
    DECIDE -- "≥ 0.80" --> BLOCKED["🚫 BLOCKED\n+ Critical Alert"]

    FLAGGED --> ALERT["Fraud Alert\n(severity: medium/high)"]
    BLOCKED --> ALERT2["Fraud Alert\n(severity: critical)"]
    ALERT --> DB2[(fraud_alerts\nrisk_scores)]
    ALERT2 --> DB2
```

---

## 🗃️ Database Schema

```mermaid
erDiagram
    USERS {
        int id PK
        varchar username
        varchar email
        varchar password_hash
        varchar role
        boolean is_active
        datetime created_at
    }

    CUSTOMERS {
        int id PK
        varchar customer_id
        varchar name
        varchar email
        varchar country
        varchar city
        float avg_transaction_amount
        int total_transactions
        varchar risk_level
        datetime created_at
    }

    TRANSACTIONS {
        int id PK
        varchar transaction_id
        int customer_id FK
        float amount
        varchar currency
        varchar merchant_name
        varchar merchant_category
        varchar location
        varchar ip_address
        varchar card_type
        varchar transaction_type
        datetime timestamp
        varchar status
        boolean is_fraud
        boolean is_reviewed
    }

    FRAUD_ALERTS {
        int id PK
        varchar alert_id
        int transaction_id FK
        varchar alert_type
        varchar severity
        text description
        text risk_factors
        boolean is_resolved
        int resolved_by FK
        datetime resolved_at
        datetime created_at
    }

    RISK_SCORES {
        int id PK
        int transaction_id FK
        float rule_score
        float ml_score
        float combined_score
        varchar risk_level
        text rule_violations
        text ml_features
        datetime created_at
    }

    FRAUD_RULES {
        int id PK
        varchar rule_name
        text description
        varchar rule_type
        float threshold
        float weight
        boolean is_active
        datetime created_at
    }

    CUSTOMERS ||--o{ TRANSACTIONS : "makes"
    TRANSACTIONS ||--o{ FRAUD_ALERTS : "triggers"
    TRANSACTIONS ||--o{ RISK_SCORES : "has"
    USERS ||--o{ FRAUD_ALERTS : "resolves"
```

---

## 🧠 ML Feature Engineering

| # | Feature | Description |
|---|---------|-------------|
| 1 | `amount` | Raw transaction amount |
| 2 | `hour` | Hour of day (0–23) |
| 3 | `day_of_week` | Day of week (0=Mon) |
| 4 | `is_international` | Location ≠ customer country |
| 5 | `is_unusual_hour` | Between 1am–5am |
| 6 | `recent_count` | Transactions in last hour |
| 7 | `amount_deviation` | Z-score from customer avg |
| 8 | `is_round_amount` | Amount is whole number |
| 9 | `is_high_risk_cat` | Gambling / Crypto / Transfer |
| 10 | `customer_risk_level` | Customer flagged as high-risk |

---

## 🚦 Fraud Rules Engine

| Rule | Trigger | Weight |
|------|---------|--------|
| `LARGE_AMOUNT` | Amount > $10,000 | 35% |
| `HIGH_FREQUENCY` | > 5 transactions/hour | 30% |
| `INTERNATIONAL_TRANSACTION` | Location ≠ home country | 25% |
| `AMOUNT_DEVIATION` | 3× above customer average | 25% |
| `UNUSUAL_HOURS` | Transaction at 1am–5am | 20% |
| `ROUND_AMOUNT` | Round number > $1,000 | 15% |
| `RAPID_TRANSACTIONS` | 3+ transactions in 5 min | 25% |
| `HIGH_RISK_MERCHANT` | Gambling / Crypto / Adult | 20% |

---

## 📁 Project Structure

```
AI_FD/
├── app/
│   ├── __init__.py              # Flask app factory
│   ├── models/
│   │   └── models.py            # SQLAlchemy ORM models (6 tables)
│   ├── services/
│   │   ├── rule_engine.py       # Rule-based fraud detection
│   │   ├── ml_service.py        # ML model inference service
│   │   └── fraud_detector.py    # Detection orchestrator
│   ├── api/
│   │   ├── auth.py              # POST /api/auth/login
│   │   ├── transactions.py      # GET/POST /api/transactions
│   │   ├── alerts.py            # GET/PUT  /api/alerts
│   │   ├── dashboard.py         # GET /api/dashboard/stats
│   │   └── customers.py         # GET /api/customers
│   ├── templates/
│   │   └── index.html           # Single-page frontend (SPA)
│   └── static/
│       ├── css/style.css
│       └── js/app.js
├── ml/
│   ├── train_model.py           # Model training script
│   └── models/                  # Saved .pkl model files
│       ├── fraud_model.pkl      # Isolation Forest
│       ├── rf_classifier.pkl    # Random Forest
│       └── scaler.pkl           # StandardScaler
├── config.py                    # App + DB + ML configuration
├── setup_db.py                  # DB init + seed + model training
├── simulate.py                  # Live transaction simulator
├── run.py                       # App entry point
└── requirements.txt
```

---

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Setup database, seed data, and train ML models (~1-2 min)
python setup_db.py

# 3. Start the server
python run.py

# 4. Open http://localhost:5000
#    Login: admin / admin123

# 5. (Optional) Simulate live transactions in a second terminal
python simulate.py --count 30 --fraud-rate 0.4
```

---

## 🔌 REST API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/auth/login` | Authenticate, receive JWT token |
| `GET` | `/api/auth/me` | Get current user profile |
| `GET` | `/api/transactions` | List transactions (paginated, filterable) |
| `POST` | `/api/transactions` | Submit & analyze a new transaction |
| `PUT` | `/api/transactions/:id/review` | Mark transaction as reviewed |
| `GET` | `/api/alerts` | List fraud alerts (filterable by severity) |
| `PUT` | `/api/alerts/:id/resolve` | Resolve a fraud alert |
| `GET` | `/api/alerts/stats` | Alert counts by severity |
| `GET` | `/api/dashboard/stats` | Main KPI statistics |
| `GET` | `/api/dashboard/transactions/trend` | 7-day transaction trend |
| `GET` | `/api/dashboard/risk-distribution` | Risk score distribution |
| `GET` | `/api/dashboard/top-alerts` | Top 10 unresolved alerts |
| `GET` | `/api/customers` | List customers |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python 3.13, Flask 3.0 |
| **ORM** | Flask-SQLAlchemy 3.1 + SQLAlchemy 2.0 |
| **Database** | MySQL 8.0 (via PyMySQL) |
| **Authentication** | Flask-JWT-Extended (JWT Bearer tokens) |
| **ML Models** | scikit-learn (Isolation Forest + Random Forest) |
| **Data Processing** | NumPy, Pandas |
| **Frontend** | HTML5, Bootstrap 5, Chart.js, Vanilla JS |
| **CORS** | Flask-CORS |

---

## 👤 Default Credentials

| Role | Username | Password |
|------|----------|----------|
| Admin | `admin` | `admin123` |
| Analyst | `analyst` | `analyst123` |
