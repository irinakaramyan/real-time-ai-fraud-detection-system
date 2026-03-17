AI Fraud Detection System
A web-based system that detects suspicious financial transactions using rule-based logic and a basic machine learning-inspired model.

Overview
This project aims to identify potentially fraudulent transactions by analyzing transaction features such as amount and location.
The system combines simple rule-based logic with an ML-inspired scoring approach to classify transactions into different risk levels.

Features
- Transaction analysis  
- Risk scoring system  
- Fraud detection (Low / Medium / High)  
- ML-inspired prediction model  
- Structured system architecture  

Tech Stack
- Backend: Python, Flask  
- Frontend: HTML, CSS, JavaScript  
- Database: SQL  
- Tools: Git, GitHub  

Machine Learning Component
The system includes a basic ML-inspired model that evaluates transaction risk using simple features:

- Transaction amount  
- Transaction location  

The model assigns a risk score and classifies transactions into:
- Low Risk  
- Medium Risk  
- High Risk  

System Architecture
The system follows a three-layer architecture:

- Frontend (Presentation Layer)  
- Backend (Application Layer) 
- Database (Data Layer) 

How to Run
1. Install dependencies (Flask)  
2. Run the backend:
   ```bash
   python app.py
