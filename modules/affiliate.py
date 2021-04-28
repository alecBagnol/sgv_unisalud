import sqlite3
from contextlib import closing
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
    except sqlite3.IntegrityError as err:
        print(f"No se pudo agregar a {first_name}, su número de id ya está en la base de datos.")

def find(affiliate_id):
    try:
        with db_link() as con:
            with closing(con.cursor()) as cur:
                cur.execute("SELECT * from affiliate WHERE affiliate_id = (?)",(affiliate_id,))
                items = cur.fetchall()
                for item in items:
                    print(item)
    except sqlite3.IntegrityError as err:
        print(f"No se pudo encontrar al usuario con Id: {affiliate_id}.")

def disaffiliate(affiliate_id, date):
    try:
        with db_link() as con:
            with closing(con.cursor()) as cur:
                cur.execute("UPDATE affiliate SET disaffiliation_date = (?), affiliation_date = NULL WHERE affiliate_id = (?)",(date,affiliate_id,))

    except sqlite3.IntegrityError as err:
        print(f"No se pudo desafiliar al usuario con Id: {affiliate_id}.")

def affiliate(affiliate_id, date):
    try:
        with db_link() as con:
            with closing(con.cursor()) as cur:
                cur.execute("UPDATE affiliate SET affiliation_date = (?), disaffiliation_date = NULL WHERE affiliate_id = (?)",(date,affiliate_id,))
    except sqlite3.IntegrityError as err:
        print(f"No se pudo renovar afiliacion del usuario con Id: {affiliate_id}.")

