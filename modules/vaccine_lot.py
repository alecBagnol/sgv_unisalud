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
        dose,
        temperature,
        effectiveness,
        protection_time,
        expiration_date,
        image_url,
    ):
    try:
        with db.create_or_connect() as con:
            with closing(con.cursor()) as cursor:
                cursor.execute("INSERT INTO vaccinelot VALUES (?,?,?,?,?,?,?,?,?,?,?)", (
                    vaccine_lot_id,
                    manufacturer,
                    vaccine_type,
                    amount,
                    0,
                    dose,
                    temperature,
                    effectiveness,
                    protection_time,
                    expiration_date,
                    image_url,
                ))
                return True
    except:
        return False

def find_lot(vaccine_lot_id):
    try:
        with db.create_or_connect() as con:
            with closing(con.cursor()) as cursor:
                cursor.execute("SELECT * FROM VaccineLot WHERE vaccine_lot_id = (?)",(vaccine_lot_id,))
                row = cursor.fetchone()
                return utils.dict_factory(cursor, row)
    except:
        return {}

def use_vaccine(vaccine_lot_id):
    try:
        with db.create_or_connect() as con:
            with closing(con.cursor()) as cursor:
                cursor.execute("UPDATE VaccineLot SET amount_used = amount_used + 1 WHERE vaccine_lot_id = (?)",(vaccine_lot_id,))
                return True
    except:
        return False


