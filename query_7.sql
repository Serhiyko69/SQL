--Знайти оцінки студентів у окремій групі з певного предмета (група_id = Z, предмет_id = X):
SELECT grades.grade
FROM grades
JOIN students ON grades.student_id = students.id
WHERE students.group_id = Z AND grades.subject_id = X;