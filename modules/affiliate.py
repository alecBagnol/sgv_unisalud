import sqlite3
from modules.create_connect import create_or_connect as db_link
from modules.utils import dict_factory
from modules import vaccine_lot
from contextlib import closing
from datetime  import datetime


class Person:
    def __init__(self, person_id, first_name, last_name, address, phone, email, city, birth_date):
        self.__id = person_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address
        self.__phone = phone
        self.__email = email
        self.__city = city
        self.__birth_date = birth_date

    def set_id(self, person_id):
        self.__id = person_id
    def get_id(self):
        return self.__id

    def set_first_name(self, first_name):
        self.__first_name = first_name
    def get_first_name(self):
        return self.__first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name
    def get_last_name(self):
        return self.__last_name
    
    def set_address(self, address):
        self.__address = address
    def get_address(self):
        return self.__address
    
    def set_phone(self, phone):
        self.__phone = phone
    def get_phone(self):
        return self.__phone
    
    def set_email(self, email):
        self.__email = email
    def get_email(self):
        return self.__email
    
    def set_city(self, city):
        self.__city = city
    def get_city(self):
        return self.__city
    
    def set_birth_date(self, birth_date):
        self.__birth_date = birth_date
    def get_birth_date(self):
        return self.__birth_date


class Affiliate(Person):
    def __init__(self, 
                 person_id, 
                 first_name, 
                 last_name, 
                 address, 
                 phone, 
                 email, 
                 city, 
                 birth_date, 
                 affiliation_date):
        self.__affiliation_date = affiliation_date
        self.__vaccinated = False
        self.__disaffiliation_date = None
        super().__init__(person_id, first_name, last_name, address, phone, email, city, birth_date)
    
    def set_affiliation_date(self, affiliation_date):
        self.__affiliation_date = affiliation_date
    def get_affiliation_date(self):
        return self.__affiliation_date

    def set_vaccinated(self, vaccinated):
        self.__vaccinated = vaccinated
    def get_vaccinated(self):
        return self.__vaccinated

    def set_disaffiliation_date(self, disaffiliation_date):
        self.__disaffiliation_date = disaffiliation_date
    def get_disaffiliation_date(self):
        return self.__disaffiliation_date
    

"""
OVERVIEW: This module contains the means to create(add), search(find), manage
          affiliation information(affiliate/disaffiliate), and manage users'
          vaccination status(vaccinate).
"""
class AffiliateManager:

    """
        Description:
            This function add affiliates to the [affiliate] table. 
            It manages its feedback once created, being True if everything went ok in addition to a short confirmation reply, or False if something is not
            working as expected.

        Arguments:
            * affiliate_id: Affiliate's ID number.
            * first_name: Affiliate's fisrt and possible middle name.
            * last_name: Affiliate's last name.
            * address: Affiliate's address.
            * phone: Affiliate's phone number.
            * email: Affiliate's email address.
            * city: Affiliate's home city.
            * birth_date: Affiliate's birth date.
            * affiliation_date: Affiliate's affiliation date.
            * vaccinated=False: Affiliate's vaccination status, initialized as 
                                False (as required).
            * disaffiliation_date: Affiliate's disaffiliation date, initialized as 
                                none (as required). 
    """
    def add(self, affiliate: Affiliate):
        try:
            with db_link() as con:
                with closing(con.cursor()) as cur:
                    cur.execute("INSERT INTO affiliate VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                        affiliate.get_id(),
                        affiliate.get_first_name(),
                        affiliate.get_last_name(),
                        affiliate.get_address(),
                        affiliate.get_phone(),
                        affiliate.get_email(),
                        affiliate.get_city(),
                        affiliate.get_birth_date(),
                        affiliate.get_affiliation_date(),
                        affiliate.get_vaccinated(),
                        affiliate.get_disaffiliation_date()
                    ))
                    return True
        except sqlite3.IntegrityError:
            return False


    """
        Description:
            The find function finds..well actually it searches for affiliates data and
            confirms if there is an affiliate associated with the search...

        Arguments:
            * affiliate_id: Affiliate's ID number.
    """
    def find(self, affiliate_id):
        try:
            with db_link() as con:
                con.row_factory = dict_factory
                with closing(con.cursor()) as cur:
                    cur.execute("SELECT * from affiliate WHERE affiliate_id = (?)", (affiliate_id, ))
                    items = cur.fetchone()
                    return items
        
        except sqlite3.IntegrityError:
            return None


    """
        Description:
            It dissafiliates an user by its ID and dissafiliation date.

        Arguments:
            * affiliate_id: Affiliate's ID number.
            * date: This is the dissafiliation date, formatted as timestamp.
    """
    def disaffiliate(self, affiliate_id, date):
        try:
            with db_link() as con:
                with closing(con.cursor()) as cur:
                    cur.execute("UPDATE affiliate SET disaffiliation_date = (?), affiliation_date = NULL WHERE affiliate_id = (?)",(date, affiliate_id,))
                    return True
        except sqlite3.IntegrityError:
            return False


    """
        Description:
            This function is in a quest for trialing every possible flop while
            trying to change affiliate's vaccination status.

        Arguments:
            * affiliate_id: Affiliate's ID number.
        Return:
            0: User registrantion was successful.
            1: There was an error user could not be vaccinated. 
            2: There is no vaccination plan related to user with given id.
            3: User was already vaccinated.
            4: There was an error user could not be vaccinated. 
    """
    def vaccinate(self, affiliate_id):
        try:
            vaccinated = self.find(affiliate_id)
            if vaccinated:
                vaccinated = vaccinated['vaccinated']

            now = datetime.now()
            if not vaccinated:
                items = self.get_vaccination_schedule(affiliate_id)
                if items:
                    check_vaccine_lot = vaccine_lot.Vaccine_Lot()
                    if check_vaccine_lot.use_vaccine(items['vaccine_lot_id']):
                        self.update_status(affiliate_id, True)
                        return 0
                    else:
                        return 1
                else:
                    return 2
            else:
                return 3
        except sqlite3.IntegrityError:    
            return 4

    """
        Description:
            Grabs affiliates vaccination schedule... with column names and return an
            object with the information.

        Arguments:
            * affiliate_id: Affiliate's ID number.
    """
    def get_vaccination_schedule(self, affiliate_id):
        self.affiliate_id = affiliate_id
        try:
            with db_link() as con:
                con.row_factory = dict_factory
                with closing(con.cursor()) as cur:
                    cur.execute("SELECT * from VaccinationSchedule WHERE affiliate_id = (?)",(affiliate_id,))
                    items = cur.fetchone()
                    return items
        except sqlite3.IntegrityError:     
            return None
        