--5. Знайти, які курси читає певний викладач
SELECT t.fullname AS teacher_fullname, d.name AS discipline
FROM teachers t
JOIN disciplines d ON t.id = d.teacher_id
WHERE t.id = 5
ORDER BY teacher_fullname;