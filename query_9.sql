--Знайти список курсів, які відвідує студент (студент_id = W):
SELECT subjects.name
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
WHERE grades.student_id = W;
