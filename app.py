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
        'class': 'Add new classes to the university. View currently available classes.',
        'major': 'Add new majors to the university. Search for a major.',
        'university': 'Update information about the school'
    }
    return render_template("main.j2", pages=pages)

# TODO - More Routes!
@app.route('/university')
def university():
    return "This is the university route"

@app.route('/faculty')
def faculty():
    return "This is the faculty route"

@app.route('/class')
def class_page():
    return "This is the class route"

@app.route('/major')
def major():
    return "This is the major route"

@app.route('/student')
def student():
    return "This is the student route"

# Listener
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=19742, debug=True)
