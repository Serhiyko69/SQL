import logging

from psycopg2 import DatabaseError

from connect import create_connection

if __name__ == '__main__':

#--Знайти 5 студентів із найбільшим середнім балом з усіх предметів
    query_1 = """
        SELECT student_id, AVG(grade) AS avg_grade
        FROM grades
        GROUP BY student_id
        ORDER BY avg_grade DESC
        LIMIT 5;"""

#--Знайти студента із найвищим середнім балом з певного предмета (предмет_id = X):
    query_2 = """
        SELECT student_id, AVG(grade) AS avg_grade
        FROM grades
        WHERE subject_id = X
        GROUP BY student_id
        ORDER BY avg_grade DESC
        LIMIT 1;
        """
#--Знайти середній бал у групах з певного предмета (предмет_id = X):
    query_3 = """
        SELECT groups.id AS group_id, AVG(grades.grade) AS avg_grade
        FROM groups
        JOIN students ON groups.id = students.group_id
        JOIN grades ON students.id = grades.student_id
        WHERE grades.subject_id = X
        GROUP BY groups.id;"""

#--Знайти середній бал на потоці (по всій таблиці оцінок):
    query_4 = """
        SELECT AVG(grade) AS avg_grade
        FROM grades;"""

#--Знайти які курси читає певний викладач (викладач_id = Y):
    query_5 = """
        SELECT subjects.name
        FROM subjects
        WHERE subjects.teacher_id = Y;"""

#--Знайти список студентів у певній групі (група_id = Z):
    query_6 = """SELECT *
        FROM students
        WHERE students.group_id = Z;"""

#--Знайти оцінки студентів у окремій групі з певного предмета (група_id = Z, предмет_id = X):
    query_7 = """
        SELECT grades.grade
        FROM grades
        JOIN students ON grades.student_id = students.id
        WHERE students.group_id = Z AND grades.subject_id = X;"""

#--Знайти середній бал, який ставить певний викладач зі своїх предметів (викладач_id = Y):
    query_8 = """
        SELECT AVG(grade) AS avg_grade
        FROM grades
        JOIN subjects ON grades.subject_id = subjects.id
        WHERE subjects.teacher_id = Y;"""

#--Знайти список курсів, які відвідує студент (студент_id = W):
    query_9 = """
        SELECT subjects.name
        FROM grades
        JOIN subjects ON grades.subject_id = subjects.id
        WHERE grades.student_id = W;"""

#--Список курсів, які певному студенту читає певний викладач (студент_id = W, викладач_id = Y):
    query_10 = """
        SELECT subjects.name
        FROM grades
        JOIN subjects ON grades.subject_id = subjects.id
        WHERE grades.student_id = 5 AND subjects.teacher_id = 2;"""



try:
    with create_connection() as conn:
        if conn is not None:
            c = conn.cursor()
            try:

                c.execute(query_1)
                result = c.fetchall()
                print(result)
                print(result)
            except DatabaseError as e:
                logging.error(e)
            finally:
                c.close()
        else:
            print("Error! cannot create the database connection.")
except RuntimeError as err:
    logging.error(err)