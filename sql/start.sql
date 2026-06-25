use mydb;
alter DATABASE mydb READ ONLY = 0;
CREATE TABLE bin (
    id INT,
    name VARCHAR(50),
    age INT,
    sal DECIMAL(8, 2) -- Allows values up to 999,999.99
);

SELECT * From bin;
Rename table bin to stu;