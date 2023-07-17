--9. Знайти список курсів, які відвідує студент
SELECT s.fullname, d.name
FROM students s
JOIN grades gr ON s.id = gr.student_id
JOIN disciplines d ON d.id = gr.discipline_id
WHERE s.id = 1
GROUP BY d.name
ORDER BY d.name;