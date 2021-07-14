from modules import create_connect as db
from contextlib import closing
from modules import utils
from modules.emails import email_manager
from datetime import datetime, timedelta, date

class VaccineLot:
    def __init__(self,
                 vaccine_lot_id,
                 manufacturer,
                 vaccine_type,
                 amount,
                 dose,
                 temperature,
                 effectiveness,
                 protection_time,
                 expiration_date,
                 image_url,):
            self.__vaccine_lot_id = vaccine_lot_id
            self.__manufacturer = manufacturer
            self.__vaccine_type = vaccine_type
            self.__amount = amount
            self.__dose = dose
            self.__temperature = temperature
            self.__effectiveness = effectiveness
            self.__protection_time = protection_time
            self.__expiration_date = expiration_date
            self.__image_url = image_url

    def set_vaccine_lot_id(self, vaccine_lot_id):
        self.__vaccine_lot_id = vaccine_lot_id
    def get_vaccine_lot_id(self):
        return self.__vaccine_lot_id

    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer
    def get_manufacturer(self):
        return self.__manufacturer

    def set_vaccine_type(self, vaccine_type):
        self.__vaccine_type = vaccine_type
    def get_vaccine_type(self):
        return self.__vaccine_type
    
    def set_amount(self, amount):
        self.__amount = amount
    def get_amount(self):
        return self.__amount

    def set_dose(self, dose):
        self.__dose = dose
    def get_dose(self):
        return self.__dose

    def set_temperature(self, temperature):
        self.__temperature = temperature
    def get_temperature(self):
        return self.__temperature
    
    def set_effectiveness(self, effectiveness):
        self.__effectiveness = effectiveness
    def get_effectiveness(self):
        return self.__effectiveness

    def set_protection_time(self, protection_time):
        self.__protection_time = protection_time
    def get_protection_time(self):
        return self.__protection_time

    def set_expiration_date(self, expiration_date):
        self.__expiration_date = expiration_date
    def get_expiration_date(self):
        return self.__expiration_date

    def set_image_url(self, image_url):
        self.__image_url = image_url
    def get_image_url(self):
        return self.__image_url

class VaccineLotManager:
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
    def new_lot(self, vaccine_lot : VaccineLot):
        try:
            with db.create_or_connect() as con:
                with closing(con.cursor()) as cursor:
                    cursor.execute("INSERT INTO vaccinelot VALUES (?,?,?,?,?,?,?,?,?,?,?)", (
                        vaccine_lot.get_vaccine_lot_id(),
                        vaccine_lot.get_manufacturer(),
                        vaccine_lot.get_vaccine_type(),
                        vaccine_lot.get_amount(),
                        0,
                        vaccine_lot.get_dose(),
                        vaccine_lot.get_temperature(),
                        vaccine_lot.get_effectiveness(),
                        vaccine_lot.get_protection_time(),
                        vaccine_lot.get_expiration_date(),
                        vaccine_lot.get_image_url(),
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
