# Architecture Diagram

```mermaid
flowchart LR

    A[Customer / External Banking System] --> B[FastAPI API Gateway]

    B --> C[Transaction Processing Module]
    C --> D[(PostgreSQL)]
    C --> E[(Redis)]

    C --> F[Fraud Rules Engine]
    C --> G[ML Fraud Detection Model]

    F --> H[Risk Scoring and Decision Layer]
    G --> H

    H --> I{Decision Result}

    I -->|Approve| J[Store Approved Transaction]
    I -->|Review| K[Generate Alert]
    I -->|Block| L[Reject / Block Transaction]

    J --> M[Monitoring Dashboard]
    K --> M
    L --> M

    K --> N[Fraud Analyst Review]
    C --> O[Audit Logging Service]
    O --> D
