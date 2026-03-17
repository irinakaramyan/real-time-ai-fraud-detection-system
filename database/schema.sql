CREATE TABLE transactions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    amount DECIMAL(10,2),
    location VARCHAR(100),
    risk_level VARCHAR(50)
);
