import sqlite3
import contextlib
import sys
from modules.create_connect import create_or_connect as db_link

def add(
        affiliate_id,
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
    ):
    conn = db_link()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO affiliate VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        (
            affiliate_id,
            first_name,
            last_name,
            address,
            phone,
            email,
            city,
            birth_date,
            affiliation_date,
            vaccinated,
            disaffiliation_date
        )
    )
    
    conn.commit()
    conn.close()

def find(affiliate_id):
    con = db_link()
    cursor = con.cursor()

    cursor.execute("SELECT * from affiliate WHERE affiliate_id = (?)",(affiliate_id,))
    items = cursor.fetchall()
    for item in items:
        print(item)
    
    con.commit()
    con.close()

def disaffiliate(affiliate_id, date):
    con = db_link()
    cursor = con.cursor()

    cursor.execute("UPDATE affiliate SET disaffiliation_date = (?), affiliation_date = NULL WHERE affiliate_id = (?)",(date,affiliate_id,))
    items = cursor.fetchall()
    
    con.commit()
    con.close()

def affiliate(affiliate_id, date):
    con = db_link()
    cursor = con.cursor()

    cursor.execute("UPDATE affiliate SET affiliation_date = (?), disaffiliation_date = NULL WHERE affiliate_id = (?)",(date,affiliate_id,))
    items = cursor.fetchall()
    
    con.commit()
    con.close()
