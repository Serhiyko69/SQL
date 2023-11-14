-- Таблиця студентів
drop table if exists Students;
CREATE TABLE Students (
  id SERIAL PRIMARY KEY,
  fullname VARCHAR(150) NOT NULL,
  group_id INTEGER REFERENCES groups(id)
  	on delete cascade
);

-- Таблиця викладачів
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
  id SERIAL PRIMARY KEY,
  fullname VARCHAR(150) NOT NULL
);

-- Таблиця предметів
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
  id SERIAL PRIMARY KEY,
  name VARCHAR(175) NOT NULL,
  teacher_id INTEGER  REFERENCES teachers(id)
  	on delete cascade
);

-- Таблиця оцінок
drop table if exists grades;
CREATE TABLE grades (
  id SERIAL PRIMARY KEY,
  student_id INTEGER  REFERENCES students(id)
  on delete cascade,
  subject_id INTEGER  REFERENCES subjects(id)
  on delete cascade,
  grade INTEGER CHECK (grade >= 0 AND grade <= 100),
  grade_date DATE NOT NULL
);