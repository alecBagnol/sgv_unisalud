import sqlite3
import contextlib
import sys
from modules.create_connect import create_or_connect as db_link

print("Module Affiliates added")

def add(
        id,
        first_name,
        last_name,
        address,
        phone,
        email,
        city,
        birth_date,
        affiliation_date,
        vaccinated=False,
        disaffiliation_date=None,
        vaccination_schedule_id=None
    ):
    conn = db_link()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO affiliates VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
        (
            id,
            first_name,
            last_name,
            address,
            phone,
            email,
            city,
            birth_date,
            affiliation_date,
            vaccinated,
            disaffiliation_date,
            vaccination_schedule_id
        )
    )
    
    conn.commit()
    conn.close()

def find(id):
    con = db_link()
    cursor = con.cursor()

    cursor.execute("SELECT * from affiliates WHERE id = (?)",(id,))
    items = cursor.fetchall()
    for item in items:
        print(item)
    
    con.commit()
    con.close()

def disaffiliate(id, date):
    con = db_link()
    cursor = con.cursor()

    cursor.execute("UPDATE affiliates SET disaffiliation_date = (?), affiliation_date = NULL WHERE id = (?)",(date,id,))
    items = cursor.fetchall()
    
    con.commit()
    con.close()

def affiliate(id, date):
    con = db_link()
    cursor = con.cursor()

    cursor.execute("UPDATE affiliates SET affiliation_date = (?), disaffiliation_date = NULL WHERE id = (?)",(date,id,))
    items = cursor.fetchall()
    
    con.commit()
    con.close()
