--7. Знайти оцінки студентів в окремій групі з певного предмета
SELECT g.name AS groupe, d.name AS discipline, gr.grade AS grades
FROM grades gr
JOIN disciplines d ON d.id = gr.discipline_id
JOIN students s ON s.id = gr.student_id
JOIN groups g ON s.group_id = g.id
WHERE g.id = 3 AND d.id = 4
ORDER BY g.name;