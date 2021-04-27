import sqlite3
from sqlite3 import Error
import os.path

"""
Description:
    Creates connection to the database, if this function is called for the first
    time it creates the database and all its tables, otherwise just the connection
    is created. 

Return:
    this function returns the connection to the database, in case some error occurs 
    during the connection/creation of the database then None is returned.

Parameters:
    Database file path.
"""

DB_FILE = os.getcwd() + os.path.sep + "db" + os.path.sep + "EPS.db"
EPS_SQL = os.getcwd() + os.path.sep + "modules" + os.path.sep + "EPS.sql"

def create_or_connect():
    conn = None
    try:
        if not os.path.isfile(DB_FILE):
            print("Creating database")
        else:
            print("Connecting database")
        conn = sqlite3.connect(DB_FILE)
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()
        sql_file = open(EPS_SQL)
        sql_as_string = sql_file.read()
        cursor.executescript(sql_as_string)
        return conn
    except Error as e:
        print(e)
    return conn