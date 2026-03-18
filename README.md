# Real-Time AI Fraud Detection System

## Overview
This project is a real-time fraud detection system designed to monitor and analyze financial transactions.  
It combines rule-based logic and machine learning models to detect suspicious activities and classify transactions instantly.

## Key Features
- Real-time transaction processing
- Rule-based fraud detection engine
- Machine learning risk scoring
- Transaction classification (Approved / Review / Blocked)
- Scalable backend architecture
- Fraud alert generation

## System Workflow
1. Transaction is received via API
2. Data is validated and stored
3. Rule-based engine calculates initial risk
4. ML model predicts fraud probability
5. Final decision is made:
   - Approved
   - Review
   - Blocked
6. Results are stored and displayed in dashboard

## Technologies
- FastAPI (Backend API)
- PostgreSQL (Database)
- Redis (Caching / Streaming)
- Scikit-learn (Machine Learning)

## Architecture
See:
- docs/system-architecture.md
- docs/architecture-diagram.md

## Machine Learning Model
The system uses a supervised learning model trained on transaction data.  
Features include transaction amount, location, frequency, and user behavior patterns.

## Project Structure
