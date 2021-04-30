from modules import create_connect as db
from contextlib import closing
from modules import utils
from modules.emails import email_manager
from datetime import datetime, timedelta, date

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
    conn = db()
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
        with db.create_or_connect() as con:
            with closing(con.cursor()) as cursor:
                cursor.execute("SELECT * FROM VaccineLot WHERE vaccine_lot_id = (?)",(vaccine_lot_id,))
                row = cursor.fetchone()
                return utils.dict_factory(cursor, row)
    except:
        return {}

def use_vaccine(vaccine_lot_id, amount, used_amount):
    con = db()
    cursor = con.cursor()

    cursor.execute("UPDATE vaccinelot SET amount = (?), amount_used = (?) WHERE vaccine_lot_id = (?)",(amount-1,amount_used+1,vaccine_lot_id,))

    con.commit()
    con.close() 

def delete_lot(vaccine_lot_id):
    try:
        con = db()
        cursor = con.cursor()
    
        cursor.execute("DELETE FROM vaccinelot WHERE vaccine_lot_id = (?)",(vaccine_lot_id,))
    
        con.commit()
        con.close()
    except IndexError:
        print("Lot id not found in data base")

