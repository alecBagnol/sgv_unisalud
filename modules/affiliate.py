import sqlite3
from contextlib import closing
import sys
from modules.create_connect import create_or_connect as db_link
from main import refresh_console, exit_interface, print_menu, main_menu
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



def add_user():

    user_attr = {
        0: {'text':'Número de Identificacion: ', 'id': 'affiliate_id', 'content': '', 'regex': '\d{10,12}', 'alert':'Número de Identificacion INVÁLIDO, ingrese de 10 a 12 números.'},
        1: {'text': 'Nombres: ', 'id': 'first_name', 'content': '', 'regex': '\d', 'alert':'Nombre INVÁLIDO, por favor use sólo carácteres alfabéticos.'},
        2: {'text': 'Apellidos: ', 'id': 'last_name', 'content': '', 'regex': '\d', 'alert':'Apellido INVÁLIDO, por favor use sólo carácteres alfabéticos.'},
        3: {'text': 'Dirección: ', 'id': 'address', 'content': '', 'regex': '\d', 'alert':'Dirección INVÁLIDA, por favor use sólo carácteres alfanuméricos.'},
        4: {'text': 'Teléfono: ', 'id': 'phone', 'content': '', 'regex': '\d', 'alert':'Número de Teléfono INVÁLIDO, ingrese de 10 a 12 números.'},
        5: {'text': 'Email: ', 'id': 'email', 'content': '', 'regex': '\d', 'alert':'Correo electrónico INVÁLIDO, ingrese un correo de la forma correo@email.com'},
        6: {'text': 'Ciudad: ', 'id': 'city', 'content': '', 'regex': '\d', 'alert':'Ciudad INVÁLIDA, por favor use sólo carácteres alfabéticos.'},
        7: {'text': 'Fecha de Nacimiento: ', 'id': 'birth_date', 'content': '', 'regex': '\d', 'alert':'Por favor, ingrese la fecha con el formato dd-mm-aaaa'},
        8: {'text': 'Fecha de Afiliación: ', 'id': 'affiliation_date', 'content': '', 'regex': '\d', 'alert':'Por favor, ingrese la fecha con el formato dd-mm-aaaa'}
    }

    for index in range(len(user_attr)):
        refresh_console()
        print("------------------------------------------------")
        print("      menú de afiliados > CREAR AFILIADO        ")
        print("------------------------------------------------")
        for i in range(index+1):
            if index == i:
                validated = False
                test_input = ''
                while not validated:
                    regex = re.compile(r"{}".format(user_attr[index]['regex']))
                    test_input = input(user_attr[index]['text'])
                    validated = re.fullmatch(regex, test_input)
                    if not validated : 
                        print(f"{user_attr[index]['alert']}")

                user_attr[index]['content'] = test_input
            else:
                print(f"{user_attr[i]['text']}{user_attr[i]['content']}")
    

    end_options = {
        2: ['Descartar', add_user],
        3: ['Volver al menú principal', main_menu],
        4: ['Salir', exit_interface]}

    print("---------------------------------------------------------------------")
    print(f"[1]Agregar   [2]{end_options[2][0]}    [3]{end_options[3][0]}    [4]{end_options[4][0]}")
    selected = int(input('>> '))
    if selected == 1:
        add(user_attr[0]['content'], user_attr[1]['content'], user_attr[2]['content'], user_attr[3]['content'], user_attr[4]['content'], user_attr[5]['content'], user_attr[6]['content'], user_attr[7]['content'], user_attr[8]['content'])
        time.sleep(3)
        affiliates_menu()
    else:
        end_options[selected][1]()

def affiliates_menu():

    refresh_console()

    options = {
        'title':['MENÚ DE AFILIADOS'],
        1: ['Crear Afiliado', add_user],
        2: ['Consultar Afiliado', None],
        3: ['Actualizar Información de Afiliado', None],
        4: ['Regresar al Menú Principal', main_menu],
        5: ['Salir', exit_interface],
        'range' : [] }
    options['range'] = [i for i in range(1,len(options)-1)]

    print_menu(options, options['range'])
    selected = int(input(': '))
    options[selected][1]()
