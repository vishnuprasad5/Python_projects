CREATE DATABASE BANK ;
USE BANK ;
CREATE TABLE Data_Base (Account_No INT AUTO_INCREMENT, Username VARCHAR(100), PIN INT, First_Name VARCHAR(100), Last_Name VARCHAR(100),
Phone_No BIGINT, Email_Id VARCHAR(100), Balance DECIMAL(10,2), PRIMARY KEY (Account_No)) ;
ALTER TABLE DATA_BASE AUTO_INCREMENT = 864209753 ;

INSERT INTO DATA_BASE (USERNAME , PIN, FIRST_NAME, LAST_NAME, PHONE_NO, EMAIL_ID, BALANCE) VALUES
('john.doe01', 1234, 'John', 'Doe', ' 9876543210', 'john.doe@example.com', 50000),
('jane_smith', 4321, 'Jane', 'Smith', '9123456789', 'jane.smith@example.com', 100000),
('mikejohnson123', 9876, 'Mike', 'Johnson', '8765432109', 'mike.johnson@example.com', 25000),
('sarah_davis', 5678, 'Sarah', 'Davis', '7890123456', 'sarah.davis@example.com', 80000),
('davidthompson007', 7890, 'David', 'Thompson', '7654321098', 'david.thompson@example.com', 150000) ;

SELECT * FROM DATA_BASE ;