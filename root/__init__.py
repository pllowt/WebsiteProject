import os
import sqlite3
from sqlite3 import Error
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)

# create database and connection to database
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

app.config['SECRET_KEY'] = 'mysecretkey'
# Get filepath OS independant
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'data.db')

db = create_connection(db_path)