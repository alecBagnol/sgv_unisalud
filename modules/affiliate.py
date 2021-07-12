import sqlite3
from modules.create_connect import create_or_connect as db_link
from modules.utils import dict_factory
from modules import vaccine_lot
from contextlib import closing
from datetime  import datetime


# OVERVIEW  :This module contains the means to create(add), search(find), manage
#           affiliation information(affiliate/disaffiliate), and manage users'
#           vaccination status(vaccinate).

class Affiliate:
    def __init__(self):
        self.vaccinated = False
        self.disaffiliation_date = None

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
    def add(self,affiliate_id,first_name,last_name,address,phone,email,city,birth_date,affiliation_date):
        self.affiliate_id = affiliate_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone
        self.email = email
        self.city = city
        self.birth_date = birth_date
        self.affiliation_date = affiliation_date
        try:
            with db_link() as con:
                with closing(con.cursor()) as cur:
                    cur.execute("INSERT INTO affiliate VALUES (?,?,?,?,?,?,?,?,?,?,?)",(
                        self.affiliate_id,
                        self.first_name,
                        self.last_name,
                        self.address,
                        self.phone,
                        self.email,
                        self.city,
                        self.birth_date,
                        self.affiliation_date,
                        self.vaccinated,
                        self.disaffiliation_date
                    ))
                    print(f"Usuario {self.affiliate_id} añadido exitosamente.")
                    return True
        except sqlite3.IntegrityError:
            print(f"Usuario {self.affiliate_id} -  yá existe en la base de datos.")
            return False




    """
        Description:
            The find function finds..well actually it searches for affiliates data and
            confirms if there is an affiliate associated with the search...

        Arguments:
            * affiliate_id: Affiliate's ID number.
    """
    def find(self, affiliate_id):
        self.affiliate_id = affiliate_id
        try:
            with db_link() as con:
                con.row_factory = dict_factory
                with closing(con.cursor()) as cur:
                    cur.execute("SELECT * from affiliate WHERE affiliate_id = (?)",(self.affiliate_id,))
                    items = cur.fetchone()
                    self.first_name = items['first_name']
                    self.last_name = items['last_name']
                    self.address = items['address']
                    self.phone = items['phone']
                    self.email = items['email']
                    self.city = items['city']
                    self.birth_date = items['birth_date']
                    self.affiliation_date = items['affiliation_date']
                    self.vaccinated = items['vaccinated']
                    self.disaffiliation_date = items['disaffiliation_date']
                    return items
        
        except sqlite3.IntegrityError:
            print(f"No se encuentran usuarios asociados a la ID: {self.affiliate_id}.")
            return None




    """
        Description:
            It dissafiliates an user by its ID and dissafiliation date.

        Arguments:
            * affiliate_id: Affiliate's ID number.
            * date: This is the dissafiliation date, formatted as timestamp.
    """
    def disaffiliate(self, affiliate_id, date):
        self.affiliate_id = affiliate_id
        self.disaffiliation_date = date
        try:
            with db_link() as con:
                with closing(con.cursor()) as cur:
                    cur.execute("UPDATE affiliate SET disaffiliation_date = (?), affiliation_date = NULL WHERE affiliate_id = (?)",(self.disaffiliation_date,self.affiliate_id,))
                    print(f"El usuario con ID: {self.affiliate_id}, fué DESAFILIADO dada la fecha suministrada.")
                    return True
        except sqlite3.IntegrityError:
            return False




    """
        Description:
            This function affiliates again an user after being dissafiliated
            by the dissafiliation function.

        Arguments:
            * affiliate_id: Affiliate's ID number.
            * date: This is the new afiliation date, formatted as timestamp.
    """
    def affiliate(self, affiliate_id, date):
        self.affiliate_id = affiliate_id
        self.affiliation_date = date
        try:
            with db_link() as con:
                with closing(con.cursor()) as cur:
                    cur.execute("UPDATE affiliate SET affiliation_date = (?), disaffiliation_date = NULL WHERE affiliate_id = (?)",(self.affiliation_date,self.affiliate_id,))
                    print(f"El usuario con ID: {self.affiliate_id}, fué AFILIADO exitosamente en la fecha indicada.")
                    return True
        except sqlite3.IntegrityError:
            return False




    """
        Description:
            This function is in a quest for trialing every possible flop while
            trying to change affiliate's vaccination status.

        Arguments:
            * affiliate_id: Affiliate's ID number.
    """
    def vaccinate(self, affiliate_id):
        self.affiliate_id = affiliate_id
        try:
            vaccinated = self.find(self.affiliate_id)
            if vaccinated:
                self.vaccinated = vaccinated['vaccinated']

            now = datetime.now()
            if not vaccinated:
                items = self.get_vaccination_schedule(self.affiliate_id)
                if items:
                    # date_obj = datetime.fromtimestamp(items['date_time']).date()
                    # if date_obj == datetime.now().date():
                    # Tab the commented code to see if vaccionation date matches with the current date and time 
                    # if use_vaccine(items['vaccine_lot_id']):
                    if vaccine_lot.Vaccine_Lot().use_vaccine(items['vaccine_lot_id']):
                        self.update_status(affiliate_id, True)
                        print(f"Usuario [{affiliate_id}] - Registro de vacunación [EXITOSO] .")
                        return True
                    else:
                        print(f"Usuario [{affiliate_id}] ya ha sido vacunado.")

                else:
                    print(f"No existe un plan de vacunación relacionado al usuario con ID {affiliate_id}")
                    return None
            else:
                print(f"Usuario [{affiliate_id}] ya ha sido vacunado, intente con otro ID.")
                return False

        except sqlite3.IntegrityError:
            print(f"No existe un plan de vacunación relacionado al usuario con ID {affiliate_id}")     
            return None




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




    """
        Description:
            It actualy vaccinates the affiliate, its only purpose is to update the
            user's vaccination status once the other considerations have been tested.

        Arguments:
            * affiliate_id: Affiliate's ID number.
            * status: vaccination state, it gets a 1 when vaccinating affiliates.
    """
    def update_status(self, affiliate_id, status):
        self.affiliate_id = affiliate_id
        self.vaccinated = status
        try:
            with db_link() as con:
                with closing(con.cursor()) as cur:
                    cur.execute("UPDATE affiliate SET vaccinated = (?) WHERE affiliate_id = (?)",(self.vaccinated,self.affiliate_id,))
                    return True
        except sqlite3.IntegrityError:
            return False



