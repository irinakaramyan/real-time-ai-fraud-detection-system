## Database Schema

## Main Tables
- users
- accounts
- cards
- devices
- transactions
- risk_scores
- alerts
- audit_logs

## Table Descriptions

## users
Stores customer information.

## accounts
Stores bank account information linked to users.

## cards
Stores payment card information linked to accounts.

## devices
Stores device information used during transactions.

## transactions
Stores transaction details such as amount, merchant, location, time, and status.

## risk_scores
Stores calculated fraud scores, including rule-based score, ML score, and final score.

## alerts
Stores suspicious transaction alerts created by the system.

## audit_logs
Stores important actions and events for audit and monitoring purposes.

## Main Relationships
- One user can have multiple accounts.
- One user can have multiple devices.
- One account can have multiple cards.
- One account can have multiple transactions.
- One transaction has one risk score.
- One transaction may generate one or more alerts.
