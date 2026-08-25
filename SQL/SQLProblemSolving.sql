CREATE TABLE employees (
    emp_id INT,
    emp_name VARCHAR(30),
    department VARCHAR(20),
    salary INT,
    bonus INT,
    email VARCHAR(50),
    phone VARCHAR(15),
    experience INT
);

-- 1. Salary eligibility
SELECT emp_name,
       CASE
           WHEN salary >= 50000 THEN 'Eligible'
           ELSE 'Not Eligible'
       END AS eligibility
FROM employees;

-- 2. Experience classification
SELECT emp_name,
       CASE
           WHEN experience > 5 THEN 'Experienced'
           ELSE 'Junior'
       END AS experience_status
FROM employees;

-- 3. Display NULL if salary is 0
SELECT emp_name,
       NULLIF(salary, 0) AS salary
FROM employees;

-- 4. Replace NULL bonus with 0
SELECT emp_name,
       COALESCE(bonus, 0) AS bonus
FROM employees;

-- 5. Replace NULL email
SELECT emp_name,
       COALESCE(email, 'Email Not Available') AS email
FROM employees;

-- 6. Display first available contact information
SELECT emp_name,
       COALESCE(email, phone, 'No Contact') AS contact_information
FROM employees;

-- 7. Salary classification
SELECT emp_name,
       CASE
           WHEN salary >= 80000 THEN 'High'
           WHEN salary >= 50000 THEN 'Medium'
           ELSE 'Low'
       END AS salary_category
FROM employees;

-- 8. Experience classification
SELECT emp_name,
       CASE
           WHEN experience >= 10 THEN 'Senior'
           WHEN experience >= 5 THEN 'Intermediate'
           ELSE 'Junior'
       END AS experience_category
FROM employees;

-- 9. Calculate final salary
SELECT emp_name,
       salary + COALESCE(bonus, 0) AS final_salary
FROM employees;

-- 10. Final salary and classification
SELECT emp_name,
       salary + COALESCE(bonus, 0) AS final_salary,
       CASE
           WHEN salary + COALESCE(bonus, 0) >= 100000 THEN 'Very High'
           WHEN salary + COALESCE(bonus, 0) >= 70000 THEN 'High'
           WHEN salary + COALESCE(bonus, 0) >= 50000 THEN 'Medium'
           ELSE 'Low'
       END AS final_salary_category
FROM employees;