```mermaid diagram

flowchart TB

Client[Client UI] -->|HTTP + JWT| API[Flask API]

API --> Auth[Auth Service]
API --> Transactions[Transaction API]
API --> Alerts[Alerts API]
API --> Dashboard[Dashboard API]
API --> Customers[Customer API]

Transactions --> Detector[Fraud Detector]

Detector --> RuleEngine[Rule Engine]
Detector --> MLService[ML Service]

MLService --> IsolationForest[Isolation Forest]
MLService --> RandomForest[Random Forest]
MLService --> Scaler[Standard Scaler]

RuleEngine --> DB[(MySQL Database)]
MLService --> DB
Detector --> DB
API --> DB
