from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import database.db_connector as db

db_connection = db.connect_to_database()

app = Flask(__name__)


@app.route('/')
def root():
    # The keys of this dict are our routes!
    pages = {
        'student': 'Add new students to the school',
        'faculty': 'Add new facutly to the staff. Search for specific instructors by name.',
        'course': 'Add new coursees to the university. View currently available coursees.',
        'major': 'Add new majors to the university. Search for a major.',
        'university': 'Update information about the school'
    }
    return render_template("main.j2", pages=pages)

# TODO - More Routes!
@app.route('/university', methods=['POST', 'GET'])
def university():
    if(request.method == 'GET'):
        query = "SELECT * FROM university"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        return render_template("university.j2", uni_info=results)
    return render_template("university.j2")

@app.route('/faculty')
def faculty():
    if(request.method == 'GET'):
        query = "SELECT * FROM faculty"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        return render_template("faculty.j2", faculty_info=results)

@app.route('/course')
def course():
    if(request.method == 'GET'):
        query = "SELECT * FROM course"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        return render_template("course.j2", course_info=results)

@app.route('/major')
def major():
    if(request.method == 'GET'):
        query = "SELECT * FROM major"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        return render_template("major.j2", major_info=results)

@app.route('/student')
def student():
    if(request.method == 'GET'):
        query = "SELECT * FROM student"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        return render_template("students.j2", student_info=results)

# Listener
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=19742, debug=True)
