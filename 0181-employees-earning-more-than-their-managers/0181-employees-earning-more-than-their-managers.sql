SELECT e.name AS Employee
FROM Employee e #creates a reference to the manager row
JOIN Employee m
ON e.managerId = m.id #links employee → manager
WHERE e.salary > m.salary; #condition


#e.managerId → the manager ID stored in the employee’s row
#m.id → the manager’s own employee ID