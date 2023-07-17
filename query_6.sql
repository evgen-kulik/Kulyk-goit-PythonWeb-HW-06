--6. Знайти список студентів у певній групі
SELECT s.fullname
FROM students s
JOIN groups g ON s.group_id = g.id
WHERE g.id = 2
ORDER BY s.fullname;