Use Cases
Actors
- User
- Financial Analyst
- System Administrator
- Fraud Detection System

Main Use Cases
1. Submit Transaction
Actor: User  
Description: The user submits transaction details to the system.

2. Analyze Transaction
Actor: Fraud Detection System  
Description: The system processes transaction data.

3. Calculate Risk Score
Actor: Fraud Detection System  
Description: The system calculates a risk score based on transaction data.

4. Predict Fraud Using ML Model
Actor: Fraud Detection System  
Description: The system uses a machine learning-based model to evaluate transaction risk.

5. Flag Suspicious Transaction
Actor: Fraud Detection System  
Description: The system flags transactions as suspicious if risk is high.

6. Review Flagged Transactions
Actor: Financial Analyst  
Description: The analyst reviews suspicious transactions.

7. Investigate Fraud Case
Actor: Financial Analyst  
Description: The analyst investigates flagged cases.

8. Store Transaction Data
Actor: Fraud Detection System  
Description: The system stores transaction data in the database.

9. Manage System Rules
Actor: System Administrator  
Description: The administrator updates fraud detection rules.

Simple Diagram 

- User → Submit Transaction  
- System → Analyze Transaction  
- System → Calculate Risk Score  
- System → Predict Fraud (ML Model)  
- System → Flag Suspicious Transaction  
- Financial Analyst → Review Flagged Transactions  
- Financial Analyst → Investigate Fraud Case  
- System Administrator → Manage System Rules  
