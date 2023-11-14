--Знайти середній бал у групах з певного предмета (предмет_id = X):
SELECT groups.id AS group_id, AVG(grades.grade) AS avg_grade
FROM groups
JOIN students ON groups.id = students.group_id
JOIN grades ON students.id = grades.student_id
WHERE grades.subject_id = X
GROUP BY groups.id;