--Знайти які курси читає певний викладач (викладач_id = Y):
SELECT subjects.name
FROM subjects
WHERE subjects.teacher_id = Y;