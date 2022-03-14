-- VARIABLE PREFIX - `:`

-- UNIVERSITY PAGE QUERIES

-- Populate uni table with data from select query
SELECT * FROM university;

-- Search for a university by name 
SELECT * FROM university WHERE name = :name;

-- Update university (generally in our schema we're only expecting one of these)
-- This is a dumb and naieve way to change the table. Open to feedback. 
DELETE FROM university ;
INSERT INTO university (student_count, ranking, name, est_date, street_name, street_num, zip_code)
VALUES (:student_count, :ranking, :name, :est_date, :street_name, :street_num, :zip_code);


-- MAJOR PAGE QUERIES

-- Populate table
SELECT * FROM major;

-- Pick a major by name 
SELECT * FROM major WHERE name = :name;

-- Insert a new major (TODO: Dropdown menu for major picking)
INSERT INTO major (name, major_code, description)
VALUES (:name, :major_code, :description);


-- FACULTY PAGE QUERIES

-- Populate table
SELECT * FROM faculty;

-- Search faculty by name
SELECT * FROM faculty WHERE first_name = :first_name AND last_name = :last_name;

-- Insert new faculty member
INSERT INTO faculty (first_name, last_name, date_of_birth, street_name, street_num, zip_code)
VALUES (:first_name, :last_name, :date_of_birth, :street_name, :street_num, :zip_code)


-- STUDENT PAGE QUERIES

-- Populate table
SELECT * FROM student;

-- Search students by name
SELECT * FROM student WHERE first_name = :first_name AND last_name = :last_name;

-- Insert new student
INSERT INTO student (first_name, last_name, date_of_birth, street_name, street_num, zip_code)
VALUES (:first_name, :last_name, :date_of_birth, :street_name, :street_num, :zip_code)


-- CLASS PAGE QUERIES

-- Populate table
SELECT * FROM course;

-- Search for a course by name
SELECT * FROM course WHERE name = :name 

-- TODO - implement me on frontend
-- Search for a course by course c ode
SELECT * FROM course WHERE course_code = :course_code 

-- Insert a new course value. 

INSERT INTO course(course_code, course_name, course_description, start_date, end_date, start_time, end_time)
VALUES (:course_code, :course_name, :course_description, :start_date, :end_date, :start_time, :end_time)