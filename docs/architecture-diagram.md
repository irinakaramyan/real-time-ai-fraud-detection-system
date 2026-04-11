```mermaid diagram

flowchart TB

%% ================= CLIENT =================
subgraph CLIENT["Client Layer (Frontend UI)"]
    UI1[Dashboard]
    UI2[Transactions Page]
    UI3[Alerts Panel]
    UI4[Submit Transaction Form]
end

%% ================= API =================
subgraph API["Backend Layer (Flask REST API)"]
    AUTH["Auth Service\n(JWT)"]
    TXN["Transaction API"]
    ALERT["Alerts API"]
    DASH["Dashboard API"]
    CUST["Customer API"]
end

%% ================= CORE SERVICES =================
subgraph SERVICES["Fraud Detection Engine"]
    ORCH["Fraud Detector (Orchestrator)"]
    RULE["Rule Engine"]
    ML["ML Scoring Service"]
end

%% ================= ML =================
subgraph ML_LAYER["Machine Learning Layer"]
    ISO["Isolation Forest"]
    RF["Random Forest"]
    SCALE["Standard Scaler"]
end

%% ================= DATABASE =================
subgraph DB["Data Layer (MySQL)"]
    USERS[(Users)]
    CUSTOMERS[(Customers)]
    TXNS[(Transactions)]
    ALERTS[(Fraud Alerts)]
    SCORES[(Risk Scores)]
    RULES[(Fraud Rules)]
end

%% ================= CONNECTIONS =================

CLIENT -->|HTTP + JWT| API

API --> AUTH
API --> TXN
API --> ALERT
API --> DASH
API --> CUST

TXN --> ORCH

ORCH --> RULE
ORCH --> ML

ML --> ISO
ML --> RF
ML --> SCALE

RULE --> SCORES
ML --> SCORES

ORCH --> ALERTS

API --> DB
SERVICES --> DB
