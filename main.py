import sys
from os import system, name as os_name
from os.path import dirname, abspath
from modules import affiliate, vaccination_schedule
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
        2: ['Consultar Afiliado', vaccination_lot_menu],
        3: ['Actualizar Información de Afiliado', vaccination_plan_menu],
        4: ['Regresar al Menú Principal', main_menu],
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

def vaccination_schedule_menu():
    pass



if __name__ == '__main__':
    main_menu()


# input("Ingrese el NUMERO DE IDENTIFICACION del afiliado: ")
# input("Ingrese NOMBRES del afiliado: ")
# input("Ingrese APELLIDOS del afiliado: ")
# input("Ingrese DIRECCION del afiliado: ")
# input("Ingrese TELEFONO del afiliado: ")
# input("Ingrese CORREO ELECTRONICO del afiliado: ")
# input("Ingrese CIUDAD del afiliado: ")
# input("Ingrese FECHA de NACIMIENTO del afiliado: ")
# input("Ingrese FECHA de AFILIACION del afiliado: ")


# affiliates.add(1000333999,"Maria Camila","Rodriguez Romero","CL 95A 11A 25","3006998877","macaroro@email.com","Cali",3082000,23042021,False,None,None)