# Architecture Diagram

```mermaid
flowchart TD
    A[Customer] --> B[FastAPI Backend]

    B --> C[PostgreSQL]
    B --> D[Redis]

    B --> E[Fraud Rules]
    B --> F[ML Model]

    E --> G[Decision Engine]
    F --> G

    G --> H{Decision}

    H -->|Approve| I[Approved]
    H -->|Review| J[Alert]
    H -->|Block| K[Blocked]

    J --> L[Dashboard]
    I --> L
    K --> L
