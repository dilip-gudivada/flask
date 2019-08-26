from flask import Flask, current_app
from flaskext.mysql import MySQL
from app import app
import pandas as pd


def db_connect():
    mysql = MySQL()
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'ready2go'
    app.config['MYSQL_DATABASE_DB'] = 'develop'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    mysql.init_app(app)
    conn = mysql.connect()
    cursor = conn.cursor()
    return cursor, conn
