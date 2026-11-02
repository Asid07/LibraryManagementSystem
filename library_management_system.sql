-- Create Table

CREATE TABLE IF NOT EXISTS MEMBER(
    Member_ID INTEGER PRIMARY KEY,
    Member_Name TEXT,
    Email TEXT,
    Phone_No TEXT,
    Address TEXT,
    Join_Date TEXT
);

-- Sample Data

INSERT INTO MEMBER VALUES
(1,'Ali Khan','ali@gmail.com','03001234567','Islamabad','2026-01-10');

INSERT INTO MEMBER VALUES
(2,'Ahmed Raza','ahmed@gmail.com','03111234567','Rawalpindi','2026-01-15');

INSERT INTO MEMBER VALUES
(3,'Sara Noor','sara@gmail.com','03211234567','Lahore','2026-02-05');

INSERT INTO MEMBER VALUES
(4,'Fatima Ali','fatima@gmail.com','03331234567','Karachi','2026-02-20');

INSERT INTO MEMBER VALUES
(5,'Usman Tariq','usman@gmail.com','03451234567','Peshawar','2026-03-01');

-- Queries Used

SELECT * FROM MEMBER;

SELECT * FROM MEMBER
WHERE Member_ID = 1;

SELECT * FROM MEMBER
ORDER BY Member_Name;

SELECT COUNT(*)
FROM MEMBER
GROUP BY Address;

SELECT COUNT(*)
FROM MEMBER;

SELECT AVG(Member_ID)
FROM MEMBER;

SELECT MAX(Member_ID)
FROM MEMBER;

SELECT MIN(Member_ID)
FROM MEMBER;