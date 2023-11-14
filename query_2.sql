--Знайти студента із найвищим середнім балом з певного предмета (предмет_id = X):
SELECT student_id, AVG(grade) AS avg_grade
FROM grades
WHERE subject_id = X
GROUP BY student_id
ORDER BY avg_grade DESC
LIMIT 1;