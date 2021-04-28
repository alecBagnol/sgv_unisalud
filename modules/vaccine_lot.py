import sqlite3
import contextlib
from create_connect import create_or_connect as db_link

def new_lot(
        vaccine_lot_id,
        manufacturer,
        vaccine_type,
        amount,
        used_amount,
        dose,
        temperature,
        effectiveness,
        protection_time,
        expiration_date,
        image_url,
    ):
    conn = db_link()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO vaccinelot VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        (
            vaccine_lot_id,
            manufacturer,
            vaccine_type,
            amount,
            used_amount,
            dose,
            temperature,
            effectiveness,
            protection_time,
            expiration_date,
            image_url,
        )
                )
    
    conn.commit()
    conn.close()

def find_lot(vaccine_lot_id):
    try:
        con = db_link()
        cursor = con.cursor()

        cursor.execute("SELECT * FROM vaccinelot WHERE vacinne_lot_id = (?)",(vaccine_lot_id,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    
        con.commit()
        con.close()
    except IndexError:
        print("Lot id not found in data base")

def use_vaccine(vaccine_lot_id, amount, used_amount):
    con = db_link()
    cursor = con.cursor()

    cursor.execute("UPDATE vaccinelot SET amount = (?), amount_used = (?) WHERE vaccine_lot_id = (?)",(amount,amount_used,vaccine_lot_id,))

    con.commit()
    con.close()

def delete_lot(vaccine_lot_id):
    try:
        con = db_link()
        cursor = con.cursor()
    
        cursor.execute("DELETE FROM vaccinelot WHERE vaccine_lot_id = (?)",(vaccine_lot_id,))
    
        con.commit()
        con.close()
    except IndexError:
        print("Lot id not found in data base")

