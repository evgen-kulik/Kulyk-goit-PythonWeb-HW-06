--10. Список курсів, які певному студенту читає певний викладач
SELECT s.fullname AS student, d.name AS discipline, t.fullname AS teacher
FROM students s
JOIN grades gr ON s.id = gr.student_id
JOIN disciplines d ON d.id = gr.discipline_id
JOIN teachers t ON d.teacher_id = t.id
WHERE s.id = 1 AND t.id = 5
GROUP BY d.name
ORDER BY d.name;