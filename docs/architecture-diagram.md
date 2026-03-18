
```mermaid
flowchart TB
    U[User / Payment Channel] --> API[FastAPI API Layer]

    API --> K[Kafka Event Stream]

    K --> VAL[Validation Service]
    K --> RULE[Rule Engine Service]
    K --> FEAT[Feature Extraction Service]

    FEAT --> REDIS[Redis Feature Store]
    REDIS --> ML[ML Scoring Service]

    RULE --> DEC[Decision Engine]
    ML --> DEC
    VAL --> DEC

    DEC --> DB[(PostgreSQL)]
    DEC --> ALERT[Alert Service]
    DEC --> DASH[Fraud Monitoring Dashboard]

    ALERT --> DASH
