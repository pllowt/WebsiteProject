import os
import sqlite3
from sqlite3 import Error
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
# Get filepath, OS independant
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# remove the tracking as SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Create database
db = SQLAlchemy(app)

login_manager.login_view = 'login'