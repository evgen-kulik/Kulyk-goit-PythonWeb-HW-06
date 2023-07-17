SELECT date_of 
FROM grades gr
JOIN students s ON s.id = gr.student_id
JOIN disciplines d ON d.id = gr.discipline_id
JOIN groups g ON g.id = s.group_id
WHERE g.id = 3 AND d.id = 3
ORDER BY gr.date_of DESC
LIMIT 1;
