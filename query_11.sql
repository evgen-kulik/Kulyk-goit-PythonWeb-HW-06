--11. Середній бал, який певний викладач ставить певному студентові
SELECT s.fullname AS student, ROUND(AVG(gr.grade), 2) AS average_grade, t.fullname AS teacher
FROM students s
JOIN grades gr ON s.id = gr.student_id
JOIN disciplines d ON d.id = gr.discipline_id
JOIN teachers t ON d.teacher_id = t.id
WHERE s.id = 2 AND t.id = 1
ORDER BY d.name;