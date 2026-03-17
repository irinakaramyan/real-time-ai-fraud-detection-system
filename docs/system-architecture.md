System Architecture

Architectural Style
The system follows a layered architecture with modular components.

High-Level Architecture

Client → API Layer → Service Layer → Data Layer / ML Module / Cache

Components

1. API Layer
- Handles HTTP requests
- Performs validation
- Routes requests to services

2. Service Layer
- Implements business logic
- Executes fraud detection rules
- Coordinates ML predictions

3. Database Layer (PostgreSQL)
- Stores transactional data
- Maintains audit logs
- Stores alerts and risk scores

4. Cache Layer (Redis)
- Stores real-time counters
- Enables fast anomaly detection

5. Machine Learning Module
- Predicts fraud probability
- Processes feature inputs

6. Decision Engine
- Combines rule-based and ML scores
- Produces final decision

Data Flow
1. Transaction received
2. Data stored in database
3. Rule engine evaluates transaction
4. ML model predicts fraud probability
5. Risk score calculated
6. Decision generated
7. Alert created if needed
