-- 1. Display employees who belong to IT, HR, or Sales
SELECT *
FROM employees
WHERE department IN ('IT', 'HR', 'Sales');

-- 2. Display employees who belong to Finance or Sales
SELECT *
FROM employees
WHERE department IN ('Finance', 'Sales');

-- 3. Display employees whose experience is between 3 and 7 years
SELECT *
FROM employees
WHERE experience BETWEEN 3 AND 7;

-- 4. Display employees whose age is between 25 and 30
SELECT *
FROM employees
WHERE age BETWEEN 25 AND 30;

-- 5. Display employees whose salary is NOT between 50000 and 70000
SELECT *
FROM employees
WHERE salary NOT BETWEEN 50000 AND 70000;

-- 6. Display employees whose names end with 'a'
SELECT *
FROM employees
WHERE emp_name LIKE '%a';

-- 7. Display employees whose names contain 'i'
SELECT *
FROM employees
WHERE emp_name LIKE '%i%';

-- 8. Display employees whose names have exactly 5 characters
SELECT *
FROM employees
WHERE emp_name LIKE '_____';

-- 9. Display employees whose salary is NULL
SELECT *
FROM employees
WHERE salary IS NULL;

-- 10. Display employees whose department is NOT NULL
SELECT *
FROM employees
WHERE department IS NOT NULL;