-- 1. Ensure we are using the correct database
USE test_db;

-- 2. Safely delete the table if it already exists
DROP TABLE IF EXISTS products;

-- 3. Create a brand new products table
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10, 2),
    stock_quantity INT
);

-- 4. Insert three items into your store inventory
INSERT INTO products (product_name, price, stock_quantity) 
VALUES 
('Wireless Mouse', 29.99, 50),
('Mechanical Keyboard', 89.99, 15),
('Gaming Monitor', 249.50, 8);

-- 5. View your entire inventory list
SELECT * FROM products;
