from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import database.db_connector as db

db_connection = db.connect_to_database()

app = Flask(__name__)


@app.route('/')
def root():
    return render_template("main.j2")

# TODO - More Routes!


# Listener
if __name__ == "__main__":
    app.run(port=19742, debug=True)
