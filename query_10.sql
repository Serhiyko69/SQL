--Список курсів, які певному студенту читає певний викладач (студент_id = W, викладач_id = Y):
SELECT subjects.name
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
WHERE grades.student_id = 5 AND subjects.teacher_id = 2;
