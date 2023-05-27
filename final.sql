CREATE DATABASE banks_portal;
USE banks_portal;

CREATE TABLE accounts (
    accountId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ownerName VARCHAR(45) NOT NULL,
    owner_ssn INT NOT NULL,
    balance DECIMAL(10,2) DEFAULT 0.00,
    account_status VARCHAR(45)
);

CREATE TABLE transactions (
    transactionId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    accountId INT NOT NULL,
    transactionType VARCHAR(45) NOT NULL,
    transactionAmount DECIMAL(10,2) NOT NULL
);

INSERT INTO accounts (ownerName, owner_ssn, balance, account_status)
VALUES
    ("Maria Jozef", 123456789, 10000.00, "active"),
    ("Linda Jones ", 987654321, 2600.00, "inactive"),
    ("John McGrail", 222222222, 100.50, "active"),
    ("Patty Luna", 111111111, 509.75, "inactive");

INSERT INTO transactions (accountId, transactionType, transactionAmount)
VALUES
    (1, "deposit", 650.98),
    (3, "withdraw", 899.97),
    (3, "deposit", 350.00);

DELIMITER //

CREATE PROCEDURE deposit(IN accountId INT, IN amount DECIMAL(10,2))
BEGIN
    INSERT INTO transactions (accountId, transactionType, transactionAmount)
    VALUES (accountId, "deposit", amount);

    UPDATE accounts SET balance = balance + amount WHERE accountId = accountId;
END //

CREATE PROCEDURE withdraw(IN accountID INT, IN amount DECIMAL(10,2))
BEGIN
    INSERT INTO transactions (accountId, transactionType, transactionAmount)
    VALUES (accountID, "withdraw", amount);

    UPDATE accounts SET balance = balance - amount WHERE accountId = accountID;
END //

DELIMITER ;