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
def create_or_connect(db_file = "../db/EPS.db"):
    conn = None
    try:
        create = False
        if not os.path.isfile(db_file):
            print("Creating database")
            create = True
        else:
            print("Databe already created")
        conn = sqlite3.connect(db_file)
        if create:
            cursor = conn.cursor()
            sql_file = open("EPS.sql")
            sql_as_string = sql_file.read()
            cursor.executescript(sql_as_string)
        return conn
    except Error as e:
        print(e)
    return conn