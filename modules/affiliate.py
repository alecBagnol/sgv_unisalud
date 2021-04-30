import sqlite3
import sys
from modules.create_connect import create_or_connect as db_link
from modules.utils import dict_factory
from modules.vaccine_lot import use_vaccine, find_lot
from contextlib import closing
from datetime  import datetime
import time
import re


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
    try:
        with db_link() as con:
            with closing(con.cursor()) as cur:
                cur.execute("INSERT INTO affiliate VALUES (?,?,?,?,?,?,?,?,?,?,?)",(
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
                ))
                print(f"Usuario {affiliate_id} añadido exitosamente.")
                return True
    except sqlite3.IntegrityError:
        return False

def find(affiliate_id):
    try:
        with db_link() as con:
            con.row_factory = dict_factory
            with closing(con.cursor()) as cur:
                cur.execute("SELECT * from affiliate WHERE affiliate_id = (?)",(affiliate_id,))
                items = cur.fetchone()
                return items
    
    except sqlite3.IntegrityError:
        print(f"No se encuentran usuarios asociados a la ID: {affiliate_id}.")
        return None

def disaffiliate(affiliate_id, date):
    try:
        with db_link() as con:
            with closing(con.cursor()) as cur:
                cur.execute("UPDATE affiliate SET disaffiliation_date = (?), affiliation_date = NULL WHERE affiliate_id = (?)",(date,affiliate_id,))
                print(f"El usuario con ID: {affiliate_id}, fué DESAFILIADO dada la fecha suministrada.")
                return True
    except sqlite3.IntegrityError:
        return False

def affiliate(affiliate_id, date):
    try:
        with db_link() as con:
            with closing(con.cursor()) as cur:
                cur.execute("UPDATE affiliate SET affiliation_date = (?), disaffiliation_date = NULL WHERE affiliate_id = (?)",(date,affiliate_id,))
                print(f"El usuario con ID: {affiliate_id}, fué AFILIADO exitosamente en la fecha indicada.")
                return True
    except sqlite3.IntegrityError:
        return False

def vaccinate(affiliate_id):
    try:
        vaccinated = find(affiliate_id)
        if vaccinated:
            vaccinated = vaccinated['vaccinated']

        now = datetime.now()
        if not vaccinated:
            items = get_vaccination_schedule(affiliate_id)
            if items:
                date_obj = datetime.fromtimestamp(items['date_time']).date()
                if date_obj == datetime.datetime.now().date():
                    if use_vaccine(items['vaccine_lot_id']):
                        update_status(affiliate_id, True)
                        print(f"Usuario [{affiliate_id}] ha sido vacunado.")
                        # return True
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

def get_vaccination_schedule(affiliate_id):
    try:
        with db_link() as con:
            con.row_factory = dict_factory
            with closing(con.cursor()) as cur:
                cur.execute("SELECT * from VaccinationSchedule WHERE affiliate_id = (?)",(affiliate_id,))
                items = cur.fetchone()
                return items
    except sqlite3.IntegrityError:     
        return None

def update_status(affiliate_id, status):
    try:
        with db_link() as con:
            with closing(con.cursor()) as cur:
                cur.execute("UPDATE affiliate SET vaccinated = (?) WHERE affiliate_id = (?)",(status,affiliate_id,))
                return True
    except sqlite3.IntegrityError:
        return False





