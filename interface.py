import sys
from os import system, name as os_name
from os.path import dirname, abspath
import os.path
sys.path.append(os.getcwd() + os.path.sep + "modules")
import affiliate
import datetime
import time
import re

def refresh_console():
    system('cls' if os_name == 'nt' else 'clear')

def exit_interface():
    exit()

def print_menu(options, range_opt):
    print(f"------------------------------------------------")
    print(f"                [{options['title'][0]}]                  ")
    print(f"------------------------------------------------")
    print(f"Selecciones una de las siguientes opciones:")
    for i in range_opt:
        print(f"    [{i}] {options[i][0]}")

def main_menu():
    refresh_console()
    options = {
        'title':['MENÚ PRINCIPAL'],
        1: ['Gestión de afiliados', affiliates_menu],
        2: ['Gestión de Lotes de Vacunas', vaccination_lot_menu],
        3: ['Gestión de Planes de Vacunación', vaccination_plan_menu],
        4: ['Gestión de Agenda de Vacunación', vaccination_schedule_menu],
        5: ['Salir', exit_interface],
        'range' : [] }
    options['range'] = [i for i in range(1,len(options)-1)]

    print_menu(options, options['range'])

    selected = int(input(': '))
    options[selected][1]()

def vaccination_lot_menu():
    pass

def vaccination_plan_menu():
    pass

def create_vaccination_schedule():
    def refresh():
        refresh_console()
        print("------------------------------------------------")
        print("      menú de programación > CREAR PROGRAMACIÓN ")
        print("------------------------------------------------")

    refresh()
    validated = False
    input_text = ''
    while not validated:
        input_text = input('Fecha de Inicio (DD/MM/AAAA): ')
        try:
            date = datetime.datetime.strptime(input_text, '%d/%m/%Y')
            validated = True
        except ValueError:
            validated = False

        if not validated : 
            print(f"{'Por favor, ingrese la fecha con el formato DD/MM/AAAA'}")
    
    refresh()
    print(f'Fecha de Inicio (DD/MM/AAAA): {input_text}')
    end_options = {
        2: ['Descartar', vaccination_schedule_menu],
        3: ['Volver al menú principal', main_menu],
        4: ['Salir', exit_interface]}

    print("---------------------------------------------------------------------")
    print(f"[1]Crear   [2]{end_options[2][0]}    [3]{end_options[3][0]}    [4]{end_options[4][0]}")
    selected = int(input('>> '))
    if selected == 1:
        
        time.sleep(3)
        vaccination_schedule_menu()
    else:
        end_options[selected][1]()


def vaccination_schedule_menu():
    refresh_console()

    options = {
        'title':['MENÚ DE PROGRAMACIÓN DE VACUNACIÓN'],
        1: ['Crear programación de vacunación ', create_vaccination_schedule],
        2: ['Consultar Programación', None],
        3: ['Consultar Programación de Afiliado', None],
        4: ['Regresar al Menú Principal', main_menu],
        5: ['Salir', exit_interface],
        'range' : [] }
    options['range'] = [i for i in range(1,len(options)-1)]

    print_menu(options, options['range'])
    selected = int(input(': '))
    options[selected][1]()

def add_user():

    user_attr = {
        0: {'text':'Número de Identificacion: ', 'id': 'affiliate_id', 'content': '', 'regex': '\d{10,12}', 'alert':'Número de Identificacion INVÁLIDO, ingrese de 10 a 12 dígitos.'},
        1: {'text': 'Nombres: ', 'id': 'first_name', 'content': '', 'regex': '[a-zA-Z ñáéíóú]+', 'alert':'Nombre INVÁLIDO, por favor use sólo carácteres alfabéticos.'},
        2: {'text': 'Apellidos: ', 'id': 'last_name', 'content': '', 'regex': '[a-zA-Z ñáéíóú]+', 'alert':'Apellido INVÁLIDO, por favor use sólo carácteres alfabéticos.'},
        3: {'text': 'Dirección: ', 'id': 'address', 'content': '', 'regex': '[a-z0-9A-Z -#]+', 'alert':'Dirección INVÁLIDA, por favor use sólo carácteres alfanuméricos.'},
        4: {'text': 'Teléfono: ', 'id': 'phone', 'content': '', 'regex': '\d{7,10}', 'alert':'Número de Teléfono INVÁLIDO, ingrese de 7 o 10 dígitos.'},
        5: {'text': 'Email: ', 'id': 'email', 'content': '', 'regex': '(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', 'alert':'Correo electrónico INVÁLIDO, ingrese un correo de la forma correo@email.com'},
        6: {'text': 'Ciudad: ', 'id': 'city', 'content': '', 'regex': '[a-zA-Z ñáéíóú]+', 'alert':'Ciudad INVÁLIDA, por favor use sólo carácteres alfabéticos.'},
        7: {'text': 'Fecha de Nacimiento: ', 'id': 'birth_date', 'content': '', 'regex': '((([0-3]{1})([1-9]{1}))|(10)|(20)|(30))-(([0]{1}[1-9]{1})|(([1]{1})[0-2]{1}))-[1-2]{1}[0-9]{3}', 'alert':'Por favor, ingrese la fecha con el formato dd-mm-aaaa'},
        8: {'text': 'Fecha de Afiliación: ', 'id': 'affiliation_date', 'content': '', 'regex': '((([0-3]{1})([1-9]{1}))|(10)|(20)|(30))-(([0]{1}[1-9]{1})|(([1]{1})[0-2]{1}))-[1-2]{1}[0-9]{3}', 'alert':'Por favor, ingrese la fecha con el formato dd-mm-aaaa'}
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
        2: ['Descartar', affiliates_menu],
        3: ['Volver al menú principal', main_menu],
        4: ['Salir', exit_interface]}

    print("---------------------------------------------------------------------")
    print(f"[1]Agregar   [2]{end_options[2][0]}    [3]{end_options[3][0]}    [4]{end_options[4][0]}")
    selected = int(input('>> '))
    if selected == 1:
        affiliate.add(user_attr[0]['content'], user_attr[1]['content'], user_attr[2]['content'], user_attr[3]['content'], user_attr[4]['content'], user_attr[5]['content'], user_attr[6]['content'], user_attr[7]['content'], user_attr[8]['content'])
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


if __name__ == '__main__':
    main_menu()
    