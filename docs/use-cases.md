Use Case Specifications

1: Process Transaction
Actor: System  
Description: Processes incoming transaction and evaluates fraud risk  

Steps:
1. Receive transaction request
2. Validate input data
3. Store transaction in database
4. Execute rule-based checks
5. Run ML model prediction
6. Calculate risk score
7. Return decision

2: Detect Fraud
Actor: System  
Description: Identifies suspicious transactions  

Steps:
1. Analyze transaction attributes
2. Detect anomalies
3. Assign risk score
4. Flag transaction if necessary

3: Generate Alert
Actor: System  
Description: Creates alert for suspicious transactions  

Steps:
1. Identify high-risk transaction
2. Generate alert
3. Store alert in database
4. Notify dashboard

4: Review Alert
Actor: Fraud Analyst  
Description: Investigate suspicious transactions  

Steps:
1. View alert details
2. Analyze transaction data
3. Mark as fraud or legitimate
4. Update system status

5: View Dashboard
Actor: Admin / Analyst  
Description: Monitor system and fraud metrics  

Steps:
1. Access dashboard
2. View statistics and trends
3. Analyze fraud patterns
