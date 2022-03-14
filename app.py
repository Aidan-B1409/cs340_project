from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_beerya'
app.config['MYSQL_PASSWORD'] = '1299'
app.config['MYSQL_DB'] = 'cs340_beerya'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

# our Routes
@app.route('/')
def root():
    return render_template("home.j2")

@app.route('/student', methods=["POST", "GET"])
def student():
    # Insert a person into the student table
    if request.method == "POST":
        if request.form.get("student-submit"):
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            date_of_birth = request.form["date_of_birth"]
            gpa = request.form["GPA"]
            street_name = request.form["street_name"]
            street_number = request.form["street_number"]
			zip_code = request.form["zip_code"]

            # If there are no null inputs
            else:
                query = "INSERT INTO student (first_name, last_name, date_of_birth, gpa, street_name, street_number, zip_code, university_id, major_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s. %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (first_name, last_name, date_of_birth, termed, gpa, street_name, street_number, zip_code, university_id, major_code))
                mysql.connection.commit()
                
            # redirect back to student page
            return redirect("/student")

    # Display student table
    if request.method == "GET":
	# Aiden code goes here


@app.route('/faculty', methods=["POST", "GET"])
def faculty():
     # Insert a worksite into the faculty table
    if request.method == "POST":
        if request.form.get("faculty-submit"):
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            date_of_birth = request.form["date_of_birth"]
            street_name = request.form["street_name"]
            street_number = request.form["street_number"]
			zip_code = request.form["zip_code"]

            # No null inputs allowed
            # If there are no null inputs
        else:
            query = "INSERT INTO faculty (first_name, last_name, date_of_birth, street_name, street_number, zip_code, university_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (first_name, last_name, date_of_birth, termed, gpa, street_name, street_number, zip_code, university_id))
            mysql.connection.commit()

        # Redirect back to faculty page
        return redirect("/faculty
		
    # Display faculty table
    if request.method == "GET":
	# Aiden code goes here

@app.route('/course', methods=["POST", "GET"])
def course():
    # Insert a course into the course table
    if request.method == "POST":
        if request.form.get("course-submit"):
            course_name = request.form["course_name"]
            course_code = request.form["course_code"]
            course_description = request.form["course_description"]
            start_date = request.form["start_date"]
            end_date = request.form["end_date"]
			start_time = request.form["start_time"]
			end_time = request.form["end_time"]

            else:
                query = "INSERT INTO course (course_code, course_name, course_description, start_date, end_date, start_time, end_time, university_id, faculty_id, major_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (course_code, course_name, course_description, start_date, end_date, start_time, end_time, university_id, faculty_id, major_code))
                mysql.connection.commit()

            # redirect back to course page
            return redirect("/course")

    # Display course table
	
@app.route('/major', methods=["POST", "GET"])
def major():
    # Insert a major into the major table
    if request.method == "POST":
        if request.form.get("major-submit"):
            name = request.form["name"]
            major_code = request.form["major_code"]
			description = request.form["description"]

            else:
                query = "INSERT INTO major (name, major_code, description, university_id) VALUES (%s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (name, major_code, description, university_id))
                mysql.connection.commit()

            # redirect back to major page
            return redirect("/major")

    # Display course table


@app.route('/university', methods=["POST", "GET"])
def university():
    # Insert auniversity into the university table
    if request.method == "POST":
        if request.form.get("university-submit"):
			student_count = request.form["student_count"]
			ranking = request.form["ranking"]
			name = request.form["name"]
			est_date = request.form["est_date"]
			street_name = request.form["street_name"]
			street_num = request.form["street_num"]
			zip_code =  request.form["zip_code"]

            else:
                query = "INSERT INTO university (student_count, ranking, name, est_date, street_name, street_num, zip_code) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (student_count, ranking, name, est_date, street_name, street_num, zip_code))
                mysql.connection.commit()

            # redirect back to university page
            return redirect("/university")

    # Display course table

