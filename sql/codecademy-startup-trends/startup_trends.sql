SELECT location, AVG(employees)
FROM startups
GROUP BY 1
HAVING AVG(employees) > 500;
