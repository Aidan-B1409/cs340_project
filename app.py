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
        form_fields = {'student_count': 'Student Count',
                       'ranking': 'Ranking',
                       'name': 'School Name',
                       'est_date': 'Established On',
                       'street_name': 'Street Name',
                       'street_num': 'Street #',
                       'zip_code': 'ZIP Code'}
        return render_template("university.j2", uni_info=results, form_fields=form_fields)
    if(request.method == 'POST'):
        if(request.form.get('university-submit')):
            student_count = request.form["student_count"]
            ranking = request.form["ranking"]
            name = request.form["name"]
            est_date = request.form["est_date"]
            street_name = request.form["street_name"]
            street_num = request.form["street_num"]
            zip_code = request.form["zip_code"]

            query = f"INSERT INTO university (student_count, ranking, name, est_date, street_name, street_num, zip_code) \
                VALUES ({int(student_count)}, {int(ranking)}, \"{name}\", \"{est_date}\", \"{street_name}\", {int(street_num)}, {int(zip_code)});"
            _ = db.execute_query(db_connection=db_connection, query=query)
            return redirect('/university')

@app.route('/faculty', methods=['POST', 'GET'])
def faculty():
    if(request.method == 'GET'):
        query = "SELECT * FROM faculty"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        form_fields = {'first_name': 'First Name',
                       'last_name': 'Last Name',
                       'dob': 'Date of Birth',
                       'street_name': 'Street Name',
                       'street_num': 'Street #',
                       'zip_code': 'ZIP Code',
                       'uni_name': 'University Name'}
        return render_template("faculty.j2", faculty_info=results, form_fields=form_fields)
    if(request.method == 'POST'):
        if(request.form.get('faculty-submit')):
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            date_of_birth = request.form["dob"]
            street_name = request.form["street_name"]
            street_number = request.form["street_num"]
            zip_code = request.form["zip_code"]
            uni_name = request.form["uni_name"]

            get_uni_id =  f"SELECT id FROM university WHERE name=\"{uni_name}\""
            uni_id_cursor = db.execute_query(db_connection=db_connection, query=get_uni_id)
            pid = uni_id_cursor.fetchone()['id']

            add_faculty = f"INSERT INTO faculty (first_name, last_name, date_of_birth, street_name, street_num, zip_code, pid)\
                VALUES (\"{first_name}\", \"{last_name}\", \"{date_of_birth}\", \"{street_name}\", {int(street_number)}, {int(zip_code)}, {pid})"
            
            _ = db.execute_query(db_connection=db_connection, query=add_faculty)
            return redirect('/faculty')

@app.route('/course', methods=['POST', 'GET'])
def course():
    if(request.method == 'GET'):
        query = "SELECT * FROM course"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        form_fields = {'course_code': 'Course Code',
                       'course_name': 'Course Name',
                       'course_desc': 'Course Description',
                       'start_date': 'Start Date',
                       'end_date': 'End Date',
                       'start_time': 'Start Time',
                       'end_time': 'End Time',
                       'uni_name': 'University Name',
                       'faculty_name': 'Instructor Last Name',
                       'major_name': 'Major Name'}
        return render_template("course.j2", course_info=results, form_fields=form_fields)

    if(request.method == 'POST'):
        if request.form.get('course-submit'):
            course_name = request.form["course_name"]
            course_code = request.form["course_code"]
            course_desc = request.form["course_desc"]
            start_date = request.form["start_date"]
            end_date = request.form["end_date"]
            start_time = request.form["start_time"]
            end_time = request.form["end_time"]
            uni_name = request.form["uni_name"]
            faculty_name = request.form["faculty_name"]
            major_name = request.form["major_name"]

            get_uni_id =  f"SELECT id FROM university WHERE name=\"{uni_name}\""
            uni_id_cursor = db.execute_query(db_connection=db_connection, query=get_uni_id)
            pid = uni_id_cursor.fetchone()['id']

            get_major_id = f"SELECT id FROM major WHERE name=\"{major_name}\""
            major_id_cursor = db.execute_query(db_connection=db_connection, query=get_major_id)
            cid = major_id_cursor.fetchone()['id']

            get_faculty_id = f"SELECT id FROM faculty WHERE last_name=\"{faculty_name}\""
            faculty_id_cursor = db.execute_query(db_connection=db_connection, query=get_faculty_id)
            eid = faculty_id_cursor.fetchone()['id']

            add_course = f"INSERT INTO course(course_code, course_name, course_description, start_date, end_date, start_time, end_time, pid, eid, cid)\
                VALUES (\"{course_code}\", \"{course_name}\", \"{course_desc}\", \"{start_date}\", \"{end_date}\", \"{start_time}\", \"{end_time}\", {pid}, {eid}, {cid})"
            _ = db.execute_query(db_connection=db_connection, query=add_course)
            return redirect("/course")

@app.route('/major', methods=['POST', 'GET'])
def major():
    if(request.method == 'GET'):
        query = "SELECT * FROM major"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        form_fields = {'uni_name': 'University Name',
                       'name': 'Major Name',
                       'major_code': 'Major Code',
                       'description': 'Description'}
        return render_template("major.j2", major_info=results, form_fields=form_fields)
    if(request.method == 'POST'):
        if request.form.get("major-submit"):
            name = request.form["name"]
            major_code = request.form["major_code"]
            description = request.form["description"]
            uni_name = request.form['uni_name']

            get_uni_id = f"SELECT id FROM university WHERE name=\"{uni_name}\""
            uni_id_cursor = db.execute_query(db_connection=db_connection, query=get_uni_id)
            pid = uni_id_cursor.fetchone()['id']

            add_major = f"INSERT INTO major (name, major_code, description, pid) VALUES (\"{name}\", {int(major_code)}, \"{description}\", {int(pid)})"
            _ = db.execute_query(db_connection=db_connection, query=add_major)
            return redirect('/major')

@app.route('/student', methods=['POST', 'GET'])
def student():
    if(request.method == 'GET'):
        query = "SELECT * FROM student"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        form_fields = {'first_name': 'First Name',
                       'last_name': 'Last Name',
                       'dob': 'Date Of Birth',
                       'gpa': 'GPA',
                       'street_name': 'Street Name',
                       'street_num': 'Street #',
                       'zip_code': 'ZIP Code',
                       'uni_name': 'University',
                       'major_name': 'Major Name'}
        return render_template("students.j2", student_info=results, form_fields=form_fields)
    if(request.method == 'POST'):
        if(request.form.get('student-submit')):
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            date_of_birth = request.form["dob"]
            gpa = request.form["gpa"]
            street_name = request.form["street_name"]
            street_number = request.form["street_num"]
            zip_code = request.form["zip_code"]

            uni_name = request.form["uni_name"]
            major_name = request.form["major_name"]

            get_uni_id =  f"SELECT id FROM university WHERE name=\"{uni_name}\""
            uni_id_cursor = db.execute_query(db_connection=db_connection, query=get_uni_id)
            pid = uni_id_cursor.fetchone()['id']

            get_major_id = f"SELECT id FROM major WHERE name=\"{major_name}\""
            major_id_cursor = db.execute_query(db_connection=db_connection, query=get_major_id)
            eid = major_id_cursor.fetchone()['id']

            add_student = f"INSERT INTO student (first_name, last_name, date_of_birth, gpa, street_name, street_num, zip_code, pid, eid)\
                VALUES (\"{first_name}\", \"{last_name}\", \"{date_of_birth}\", {float(gpa)}, \"{street_name}\", {int(street_number)}, {int(zip_code)}, {pid}, {eid})"
            
            _ = db.execute_query(db_connection=db_connection, query=add_student)
            return redirect('/student')

# Listener
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=19742, debug=True)
