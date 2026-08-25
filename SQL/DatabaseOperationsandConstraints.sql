-- Create departments table
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL
);

-- Insert departments
INSERT INTO departments (dept_id, dept_name) VALUES
(101, 'Sales'),
(102, 'Marketing'),
(103, 'IT'),
(104, 'HR');

-- Create employee table
CREATE TABLE employee (
    eid INT UNIQUE,
    ename VARCHAR(100),
    dept VARCHAR(50),
    dept_id INT,
    salary DECIMAL(10,2),
    city VARCHAR(50),
    CONSTRAINT fk_employee_department
        FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- Insert 10 employee records
INSERT INTO employee (eid, ename, dept, dept_id, salary, city) VALUES
(1, 'Amit', 'Sales', 101, 55000, 'Mumbai'),
(2, 'Priya', 'Marketing', 102, 60000, 'Delhi'),
(3, 'Rahul', 'IT', 103, 75000, 'Bangalore'),
(4, 'Anita', 'Sales', 101, 52000, 'Pune'),
(5, 'Vijay', 'Marketing', 102, 48000, 'Chennai'),
(6, 'Sneha', 'HR', 104, 65000, 'Hyderabad'),
(7, 'Arjun', 'IT', 103, 70000, 'Kolkata'),
(8, 'Neha', 'Marketing', 102, 58000, 'Delhi'),
(9, 'Ravi', 'Sales', 101, 51000, 'Mumbai'),
(10, 'Kiran', 'HR', 104, 45000, 'Pune');

-- 1. Increase salary of Sales employees by 10%
UPDATE employee
SET salary = salary * 1.10
WHERE dept = 'Sales';

-- 2. Update city for employees with dept_id = 101
UPDATE employee
SET city = 'New York'
WHERE dept_id = 101;

-- 3. Update department for employees whose name starts with 'A'
UPDATE employee
SET dept = 'HR'
WHERE ename LIKE 'A%';

-- Delete employee with eid = 5
DELETE FROM employee
WHERE eid = 5;

-- Add project_name after dept_id
ALTER TABLE employee
ADD COLUMN project_name VARCHAR(100) AFTER dept_id;

-- Add aadhar_number at the beginning
ALTER TABLE employee
ADD COLUMN aadhar_number VARCHAR(12) FIRST;

-- Retrieve employees with salary greater than 50000
SELECT *
FROM employee
WHERE salary > 50000;

-- Retrieve names and departments of Marketing employees
SELECT ename, dept
FROM employee
WHERE dept = 'Marketing';

-- Calculate average salary for each department
SELECT dept, AVG(salary) AS average_salary
FROM employee
GROUP BY dept;

-- Verify employee table
SELECT * FROM employee;