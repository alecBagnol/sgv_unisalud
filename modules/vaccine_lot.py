from modules import create_connect as db
from contextlib import closing
from modules import utils
from modules.emails import email_manager
from datetime import datetime, timedelta, date

class Vaccine_Lot:
    """
        Description:
        Adds a new vaccine lot to the " VaccineLot" table, in case that any parameter is invalid it throws an expection, otherwise, returns true.

        Parameters:
        vaccine_lot_id: Primary key, lot's ID number.
        manufacturer: Manufacturer of the vaccines in the lot.
        vaccine_type: The type of the vaccines in the lot.
        amount: The amount of vaccines in the lot.
        used_amount: The amount of used vaccines in the lot, starts at 0.
        dose: The amount of doses that has to be applied per person.
        temperature: The temprature at which the lot has to be sotred.
        effectiveness: The effectiveness of the vaccine.
        protection_time: Trotection time of the vaccine.
        expiration_date: The date at which the vaccine expires.
        image_url: The url to the image of the lot.
    """

    def new_lot(
            self,
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


    """
        Description:
        Searches for a match for "vaccine_lot_id" in the data base and if succesfull returns a dictionary with the matched parameters, otherwise trhows an exception.

        Parameters:
        vaccine_lot_id: lot's ID number.
    """

    def find_lot(self, vaccine_lot_id):
        try:
            with db.create_or_connect() as con:
                with closing(con.cursor()) as cursor:
                    cursor.execute("SELECT * FROM VaccineLot WHERE vaccine_lot_id = (?)",(vaccine_lot_id,))
                    row = cursor.fetchone()
                    return utils.dict_factory(cursor, row)
        except:
            return {}

    """
        Description:
        Adds one to the used amount counter in the lot with the provided lot ID number, returns true if succesfull or throws an expection if not.

        Parameters:
        vaccine_lot_id: lot's ID number.
        used_amount: the amount of used vaccines in the lot.
    """

    def use_vaccine(self, vaccine_lot_id):
        try:
            with db.create_or_connect() as con:
                with closing(con.cursor()) as cursor:
                    cursor.execute("UPDATE VaccineLot SET used_amount = used_amount + 1 WHERE vaccine_lot_id = (?)",(vaccine_lot_id,))
                    return True
        except:
            return False
