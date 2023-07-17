--12. Оцінки студентів у певній групі з певного предмета на останньому занятті
SELECT g.name AS [group], d.name AS discipline, gr.grade AS grade, gr.date_of AS last_lesson_date
FROM grades gr
JOIN students s ON s.id = gr.student_id
JOIN disciplines d ON d.id = gr.discipline_id
JOIN groups g ON g.id = s.group_id
--g.id та d.id в основному запиті та підзапиті повинні співпадати!
WHERE g.id = 2 AND d.id = 7 AND gr.date_of = (SELECT date_of
FROM grades gr
JOIN students s ON s.id = gr.student_id
JOIN disciplines d ON d.id = gr.discipline_id
JOIN groups g ON g.id = s.group_id
WHERE g.id = 2 AND d.id = 7
ORDER BY gr.date_of DESC
LIMIT 1);


--Працюючий код
--WHERE g.id = 3 AND d.id = 3
--ORDER BY gr.date_of DESC;