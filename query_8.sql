
--Знайти середній бал, який ставить певний викладач зі своїх предметів (викладач_id = Y):
SELECT AVG(grade) AS avg_grade
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.teacher_id = Y;