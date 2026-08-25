CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(30),
    department VARCHAR(20),
    salary DECIMAL(10,2),
    experience INT,
    age INT
);

-- 1. Display employee name and salary after deducting ₹2,000
SELECT emp_name, salary, salary - 2000 AS salary_after_deduction
FROM employees;

-- 2. Display employee name, salary, and salary after a 15% increment
SELECT emp_name, salary, salary * 1.15 AS salary_after_increment
FROM employees;

-- 3. Display employee name, experience, and remaining years to complete 10 years
SELECT emp_name, experience, 10 - experience AS remaining_years
FROM employees;

-- 4. Display employees whose salary is less than or equal to ₹50,000
SELECT *
FROM employees
WHERE salary <= 50000;

-- 5. Display employees whose experience is exactly 5 years
SELECT *
FROM employees
WHERE experience = 5;

-- 6. Display employees whose age is greater than 30
SELECT *
FROM employees
WHERE age > 30;

-- 7. Display employees whose salary is not equal to ₹50,000
SELECT *
FROM employees
WHERE salary <> 50000;

-- 8. Display employees who belong to HR OR have salary greater than ₹70,000
SELECT *
FROM employees
WHERE department = 'HR'
   OR salary > 70000;

-- 9. Display employees whose salary is greater than ₹50,000
--    AND experience is less than 8 years
SELECT *
FROM employees
WHERE salary > 50000
  AND experience < 8;

-- 10. Display employees who belong to IT AND are older than 30
SELECT *
FROM employees
WHERE department = 'IT'
  AND age > 30;

-- 11. Display employees who belong to HR OR Sales
SELECT *
FROM employees
WHERE department = 'HR'
   OR department = 'Sales';