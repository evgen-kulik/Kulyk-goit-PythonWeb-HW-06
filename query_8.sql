--8. Знайти середній бал, який ставить певний викладач зі своїх предметів
SELECT t.fullname, d.name, ROUND(AVG(gr.grade), 2) AS average_grade
FROM grades gr
JOIN disciplines d ON d.id = gr.discipline_id
JOIN teachers t ON t.id = d.teacher_id
WHERE t.id = 3 AND d.id = 4

