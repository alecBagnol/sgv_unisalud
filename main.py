import sys
from os import system, name as os_name
from os.path import dirname, abspath
from modules import affiliate, vaccination_schedule



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
        1: ['Gestión de afiliados', affiliate.affiliates_menu],
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

def vaccination_schedule_menu():
    pass



if __name__ == '__main__':
    main_menu()
