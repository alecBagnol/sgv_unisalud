import sys
from os import system, name as os_name
import datetime
import time
import re
from modules import vaccination_plan, vaccination_schedule, vaccine_lot, affiliate


# OVERVIEW  :This file contains all the "Front_end" related functions.
#           These are the functions that builds and displays the context menus 
#           and also validates the information provided by users.
class Interface:
    def __init__(self):
        self.vaccination_scheduler = vaccination_schedule.VaccinationScheduleManager()
        self.vaccine_lot_manager = vaccine_lot.VaccineLotManager()
        self.vaccination_plan_manager = vaccination_plan.VaccinationPlanManager()
        self.affiliate_manager = affiliate.AffiliateManager()

    # UTILITY FUNCTIONS
    def refresh_console(self):
        system('cls' if os_name == 'nt' else 'clear')

    def exit_interface(self):
        self.refresh_console()
        exit()

    def print_menu(self, options, range_opt=0):
        print(f"------------------------------------------------------------------------------")
        print(f"                       [{options['title'][0]}]                  ")
        print(f"------------------------------------------------------------------------------")
        if range_opt:
            print(f"Seleccione una de las siguientes opciones:\n")
            for i in range_opt:
                print(f"            [{i}] {options[i][0]}")
            selection = self.validate_selection(len(range_opt))
            return selection

    def str_to_date(self, date_str):
        date_split = date_str.split('/')
        date_split = list(map(int, date_split))
        data_date = datetime.datetime(date_split[2],date_split[1],date_split[0]).timestamp()
        return data_date

    def validate_selection(self, num_range):
        validated = False
        selected = 0
        while not validated:
            selected = input(">> ")
            regex_str = f"[1-{num_range}]"
            regex = re.compile(r"{}".format(regex_str))
            validated = re.fullmatch(regex, selected)
            if not validated : 
                print(f"Por favor, seleccione una opci??n v??lida.")
        return int(selected)

    def input_validation(self, msg_intro, re_str, msg_alert,input_msg=""):
        validated = False
        data = None
        print("{}".format(msg_intro))
        while not validated:
            if input_msg:
                data = input(input_msg)
            else:
                data = input(">> ")
            regex = re.compile(r"{}".format(re_str))
            validated = re.fullmatch(regex, data)
            if not validated : 
                print("{}".format(msg_alert))
        return data

    def end_options_menu(self, end_options, eval_range, other_attr=None):
        print("------------------------------------------------------------------------------")
        for key, option in end_options.items():
            print(f"[{key}]{option[0]}", end="     ")
        print("")
        selected = self.validate_selection(eval_range)

        # other_attr must be a list of dicts with the form [{'key':'The key in end_options', 'args':'(arg, arg, ...)'}, ...]
        if other_attr:
            for attr_element in other_attr:
                if selected == attr_element['key']:
                    end_options[selected][1](*attr_element['args'])
                else:
                    end_options[selected][1]()
        else:
            end_options[selected][1]()


    # MAIN MENU UI 
    def main_menu(self):
        self.refresh_console()
        options = {
            'title':['MEN?? PRINCIPAL'],
            1: ['Gesti??n de afiliados', self.affiliates_menu],
            2: ['Gesti??n de Lotes de Vacunas', self.vaccination_lot_menu],
            3: ['Gesti??n de Planes de Vacunaci??n', self.vaccination_plan_menu],
            4: ['Gesti??n de Programaci??n de Vacunaci??n', self.vaccination_schedule_menu],
            5: ['Salir', self.exit_interface],
            'range' : [] }
        options['range'] = [i for i in range(1,len(options)-1)]

        selected = self.print_menu(options, options['range'])
        options[selected][1]()


    # VACCINE LOT UI MENU
    def add_vaccine_lot(self):
        user_attr = {
            0: {'text': 'N??mero de Lote: ', 'id': 'vaccine_lot_id', 'content': '', 'regex': '\d{1,12}', 'alert':'N??mero de Lote INV??LIDO, ingrese hasta 12 d??gitos.'},
            1: {'text': 'Fabricante: ', 'id': 'manufacturer', 'content': '', 'regex': '[a-zA-Z ????????????]+', 'alert':'Fabricante INV??LIDO, Fabricantes: Sinovac, Pfizer, Moderna, SputnikV, AstraZeneca, Sinopharm, Covaxim'},
            2: {'text': 'Tipo de Vacuna: ', 'id': 'vaccine_type', 'content': '', 'regex': '[a-zA-Z ????????????]+', 'alert':'Tipo de vacuna INV??LIDO. Tipos: Vector viral, ARN/ADN, Virus desactivado, En base a prote??nas'},
            3: {'text': 'Unidades Disponibles: ', 'id': 'amount', 'content': '', 'regex': '\d{1,6}', 'alert':'N??mero de Unidades INV??LIDO, ingrese hasta 6 d??gitos.'},
            4: {'text': 'Dosis: ', 'id': 'dose', 'content': '', 'regex': '\d{1,1}', 'alert':'N??mero de Dosis INV??LIDO, ingrese 1 solo d??gito.'},
            5: {'text': 'Temperatura de Almacenamiento: ', 'id': 'temperature', 'content': '', 'regex': '-?\d+\.?\d*', 'alert':'Temperatura INV??LIDA, ingrese hasta 2 d??gitos.'},
            6: {'text': 'Efectividad: ', 'id': 'effectiveness', 'content': '', 'regex': '\d{1,2}', 'alert':'Efectividad INV??LIDA, ingrese 2 d??gitos.'},
            7: {'text': 'Tiempo de Protecci??n: ', 'id': 'protection_time', 'content': '', 'regex': '\d{1,3}', 'alert':'Tiempo de protecci??n INV??LIDO, ingrese hasta 3 d??gitos.'},
            8: {'text': 'Fecha de Vencimiento: ', 'id': 'expiration_date', 'content': '', 'alert':'Por favor, ingrese la fecha con el formato DD/MM/AAAA'},
            9: {'text': 'Foto del Lote: ', 'id': 'image_url', 'content': ''}
        }

        def refresh():
            self.refresh_console()
            print("------------------------------------------------------------------------------")
            print("                   men?? de lote de vacunas > AGREGAR LOTE                     ")
            print("------------------------------------------------------------------------------")

        for index in range(len(user_attr)):
            refresh()
            for i in range(index+2):
                if index == i:
                    validated = False
                    input_text = ''
                    while not validated:
                        input_text = input(user_attr[index]['text'])
                        if i == 1:
                            if input_text in {"Sinovac", "Pfizer", "Moderna", "SputnikV", "AstraZeneca", "Sinopharm", "Covaxim"}:
                                validated = True
                        elif i == 2:
                            if input_text in {"Vector viral", "ARN/ADN", "Virus desactivado", "En base a prote??nas"}:
                                validated = True
                        elif i == 8:
                            try:
                                input_text = datetime.datetime.strptime(input_text, '%d/%m/%Y').timestamp()
                                validated = True
                            except ValueError:
                                validated = False
                        elif i == 9:
                            validated = True
                        else:
                            regex = re.compile(r"{}".format(user_attr[index]['regex']))
                            validated = re.fullmatch(regex, input_text)
                        if not validated : 
                            print(f"{user_attr[index]['alert']}")
                    if index in {0, 3, 4, 6, 7}:
                        input_text = int(input_text)
                    elif index in {5}:
                        input_text = float(input_text)

                    user_attr[index]['content'] = input_text
                else:
                    if i == index + 1 :
                        continue
                    elif i == 8:
                        print(f"{user_attr[i]['text']}{datetime.datetime.fromtimestamp(user_attr[i]['content']).date().strftime('%d/%m/%Y')}")
                    else:
                        print(f"{user_attr[i]['text']}{user_attr[i]['content']}")

        
        end_options = {
            2: ['Descartar', self.vaccination_lot_menu],
            3: ['Volver al men?? principal', self.main_menu],
            4: ['Salir', self.exit_interface]}

        print("------------------------------------------------------------------------------")
        print(f"[1]Agregar   [2]{end_options[2][0]}    [3]{end_options[3][0]}    [4]{end_options[4][0]}")
        selected = int(input('>> '))
        if selected == 1:
            res = self.vaccine_lot_manager.new_lot(vaccine_lot.VaccineLot(
                                    user_attr[0]['content'], user_attr[1]['content'], user_attr[2]['content'],
                                    user_attr[3]['content'], user_attr[4]['content'], user_attr[5]['content'],
                                    user_attr[6]['content'], user_attr[7]['content'], user_attr[8]['content'],
                                    user_attr[9]['content']))
            refresh()
            if res:
                print("\nLOTE DE VACUNAS AGREGADO CON ??XITO")
            else:
                print("\nOCURRI?? UN ERROR AGREGANDO EL LOTE DE VACUNAS INTENTELO DE NUEVO")
            time.sleep(3)
            self.vaccination_lot_menu()
        else:
            end_options[selected][1]()

    def get_vaccine_lot(self):
        def refresh():
            self.refresh_console()
            print("------------------------------------------------------------------------------")
            print("                   men?? de lote de vacunas > CONSULTA LOTE                    ")
            print("------------------------------------------------------------------------------")

        refresh()

        validated = False
        input_text = ''
        while not validated:
            regex = re.compile(r"{}".format('\d{1,12}'))
            input_text = input('Ingrese N??mero de Lote: ')
            validated = re.fullmatch(regex, input_text)
            if not validated : 
                print('N??mero de Lote INV??LIDO, ingrese hasta 12 d??gitos.')
        refresh()
        lot = self.vaccine_lot_manager.find_lot(int(input_text))

        if bool(lot):
            print(f"""
                N??mero de lote: {lot["vaccine_lot_id"]}
                Fabricante: {lot["manufacturer"]}
                Tipo de Vacuna: {lot["vaccine_type"]}
                Unidades Disponibles: {lot["amount"]}
                Unidades Usadas: {lot["used_amount"]}
                Dosis: {lot["dose"]}
                Temperatura: {lot["temperature"]}
                Efectividad: {lot["effectiveness"]}
                Tiempo de Protecci??n: {lot["protection_time"]}
                Fecha de Vencimiento: {datetime.datetime.fromtimestamp(lot["expiration_date"]).strftime("%d/%m/%Y")}
                Url Imagen: {lot["image_url"]}
            """)   
            print("------------------------------------------------------------------------------")
        else:
            print("NO HAY LOTE ASOCIADO AL IDENTIFICADOR")

        end_options = {
            1: ['Volver al men?? principal', self.main_menu],
            2: ['Salir', self.exit_interface]}
        self.end_options_menu(end_options, 2)

    def vaccination_lot_menu(self):
        self.refresh_console()
        options = {
            'title':['MEN?? DE GESTION LOTES DE VACUNAS'],
            1: ['Agregar Lote', self.add_vaccine_lot],
            2: ['Consultar Lote', self.get_vaccine_lot],
            3: ['Regresar al Men?? Principal', self.main_menu],
            4: ['Salir', self.exit_interface],
            'range' : [] }
        options['range'] = [i for i in range(1,len(options)-1)]

        selected = self.print_menu(options, options['range'])
        options[selected][1]()


    # VACCINATION PLAN UI MENU
    def create_vaccination_plan(self):
        plan_attr = {
            0: {'text':'N??mero de Identificaci??n del Plan: ', 'id': 'vaccination_plan_id', 'content': '', 'regex': '\d{1,2}', 'alert':'N??mero de Identificaci??n del plan INV??LIDO, ingrese hasta 2 d??gitos.'},
            1: {'text': 'Edad M??nima: ', 'id': 'minimum_age', 'content': '', 'regex': '\d{1,3}', 'alert':'Edad M??nima INV??LIDA, ingrese de 1 a 3 d??gitos.'},        
            2: {'text': 'Edad M??xima: ', 'id': 'maximum_age', 'content': '', 'regex': '\d{1,3}', 'alert':'Edad M??xima INV??LIDA, ingrese de 1 a 3 d??gitos.'},
            3: {'text': 'Fecha de Inicio del Plan: ', 'id': 'start_date', 'content': '', 'regex': '^(0[1-9]|1[0-9]|2[0-9]|3[0-1])/(0[1-9]|1[0-2])/(19[0-9]{2}|2[0-9]{3})$', 'alert':'Por favor, ingrese la fecha con el formato DD/MM/AAAA'},
            4: {'text': 'Fecha de Finalizaci??n del Plan: ', 'id': 'end_date', 'content': '', 'regex': '^(0[1-9]|1[0-9]|2[0-9]|3[0-1])/(0[1-9]|1[0-2])/(19[0-9]{2}|2[0-9]{3})$', 'alert':'Por favor, ingrese la fecha con el formato DD/MM/AAAA'}
        }
        
        for index in range(len(plan_attr)):
            self.refresh_console()
            print("------------------------------------------------------------------------------")
            print("                   men?? de plan de vacunaci??n > CREAR PLAN                    ")
            print("------------------------------------------------------------------------------")
            for i in range(index+1):
                if index == i:
                    validated = False
                    test_input = ''
                    while not validated:
                        regex = re.compile(r"{}".format(plan_attr[index]['regex']))
                        test_input = input(plan_attr[index]['text'])
                        validated = re.fullmatch(regex, test_input)
                        if not validated:
                            print(f"{plan_attr[index]['alert']}")

                    if index == 2 and int(test_input) < int(plan_attr[1]['content']):
                        while int(test_input) < int(plan_attr[1]['content']):
                            print("  ??Edad m??nima mayor que edad m??xima,ingrese nuevamente la edad m??xima para que tenga sentido!")
                            test_input = self.input_validation("", plan_attr[index]['regex'], plan_attr[index]['alert'], plan_attr[index]['text'])
                        plan_attr[index]['content'] = test_input

                    elif index == 4 and self.str_to_date(test_input) < self.str_to_date(plan_attr[3]['content']):
                        while self.str_to_date(test_input) < self.str_to_date(plan_attr[3]['content']):
                            print("  ??Fecha de inicio mayor que fecha de finalizaci??n,ingrese nuevamente la fecha de finalizaci??n.!")
                            test_input = self.input_validation("", plan_attr[index]['regex'], plan_attr[index]['alert'], plan_attr[index]['text'])
                        plan_attr[index]['content'] = test_input
                    else:
                        plan_attr[index]['content'] = test_input
                
                else:
                    print(f"{plan_attr[i]['text']}{plan_attr[i]['content']}")

        end_options = {
            2: ['Descartar', self.vaccination_plan_menu],
            3: ['Volver al men?? principal', self.main_menu],
            4: ['Salir', self.exit_interface]}

        print("------------------------------------------------------------------------------")
        print(f"[1]Agregar   [2]{end_options[2][0]}    [3]{end_options[3][0]}    [4]{end_options[4][0]}")
        selected = int(input('>> '))
        if selected == 1:
            plan_success = self.vaccination_plan_manager.create_vaccination_plan(
                vaccination_plan.VaccinationPlan(int(plan_attr[0]['content']), 
                                                 int(plan_attr[1]['content']), 
                                                 int(plan_attr[2]['content']), 
                                                 self.str_to_date(plan_attr[3]['content']), 
                                                 self.str_to_date(plan_attr[4]['content'])))
            if plan_success:
                print('Plan de vacaunaci??n creado exitosamente')
            else:
                print('Plan de vacunaci??n no creado: una de las edades se solapa con las edades de un plan de vacunaci??n ya existente')
            time.sleep(3)
            self.vaccination_plan_menu()
        else:
            end_options[selected][1]()

    def consult_vaccination_plan(self):
        def refresh():
            self.refresh_console()
            print("------------------------------------------------------------------------------")
            print("          men?? de plan de vacunaci??n > CONSULTAR PLAN DE VACUNACI??N           ")
            print("------------------------------------------------------------------------------")

        refresh()
        validated = False
        input_text = ''
        while not validated:
            regex = re.compile(r"{}".format('\d{1,2}'))
            input_text = input('Ingrese N??mero de Identificaci??n del Plan: ')
            validated = re.fullmatch(regex, input_text)
            if not validated : 
                print('N??mero de Identificaci??n del Plan INV??LIDO, ingrese hasta 2 d??gitos.')
        refresh()
        plan = self.vaccination_plan_manager.consult_vaccination_plan(int(input_text))
        
        if bool(plan):
            print(f"""
                N??mero de Identificaci??n del Plan: {plan["vaccination_plan_id"]}
                Edad M??nima: {plan["minimum_age"]}
                Edad M??xima: {plan["maximum_age"]}
                Fecha de Inicio del Plan: {datetime.datetime.fromtimestamp(plan["start_date"]).date().strftime("%d/%m/%Y")}
                Fecha de Finalizaci??n del Plan: {datetime.datetime.fromtimestamp(plan["end_date"]).date().strftime("%d/%m/%Y")}
            """)   
            print("------------------------------------------------------------------------------")
        else:
            print("PLAN DE VACUNACI??N NO EXISTENTE")

        end_options = {
            1: ['Volver al men?? principal', self.main_menu],
            2: ['Salir', self.exit_interface]}
        self.end_options_menu(end_options, len(end_options))

    def vaccination_plan_menu(self):
        self.refresh_console()

        options = {
            'title':['MEN?? DE PLAN DE VACUNACI??N'],
            1: ['Crear Plan de Vacunaci??n', self.create_vaccination_plan],
            2: ['Consultar Plan de Vacunaci??n', self.consult_vaccination_plan],
            3: ['Regresar al Men?? Principal', self.main_menu],
            4: ['Salir', self.exit_interface],
            'range' : [] }
        options['range'] = [i for i in range(1,len(options)-1)]
        selected = self.print_menu(options, options['range'])
        options[selected][1]()


    # VACCINATION SCHEDULE UI MENU 
    def create_vaccination_schedule(self):
        def refresh():
            self.refresh_console()
            print("------------------------------------------------------------------------------")
            print("                  men?? de programaci??n > CREAR PROGRAMACI??N                   ")
            print("------------------------------------------------------------------------------")

        refresh()
        validated = False
        input_text = ''
        while not validated:
            input_text = input('Fecha y Hora de Inicio (DD/MM/AAAA, HH:MM:SS): ')
            try:
                date = datetime.datetime.strptime(input_text, '%d/%m/%Y, %H:%M:%S')
                validated = True
            except ValueError:
                validated = False

            if not validated : 
                print(f"{'Por favor, ingrese la fecha con el formato DD/MM/AAAA, HH:MM:SS'}")
        
        refresh()
        print(f'Fecha y Hora de Inicio (DD/MM/AAAA, HH:MM:SS): {input_text}')
        end_options = {
            2: ['Descartar', self.vaccination_schedule_menu],
            3: ['Volver al men?? principal', self.main_menu],
            4: ['Salir', self.exit_interface]}

        print("------------------------------------------------------------------------------")
        print(f"[1]Crear   [2]{end_options[2][0]}    [3]{end_options[3][0]}    [4]{end_options[4][0]}")
        selected = int(input('>> '))
        if selected == 1:
            res = self.vaccination_scheduler.create_all_vaccination_schedule(date.timestamp())
            #refresh()
            if res:
                print("\nPROGRAMACI??N DE VACUNACI??N CREADA CON ??XITO")
            else:
                print("\nOCURRI?? UN ERROR CREANDO LA  PROGRAMACI??N INTENTELO DE NUEVO")

            time.sleep(8)
            self.vaccination_schedule_menu()
        else:
            end_options[selected][1]()

    def get_all_vaccination_schedule(self):
        def refresh():
            self.refresh_console()
            print("------------------------------------------------------------------------------")
            print("                men?? de programaci??n > CONSULTAR PROGRAMACI??N                 ")
            print("------------------------------------------------------------------------------")

        refresh()
        schedules = self.vaccination_scheduler.get_all()

        if len(schedules) >= 1:
            for schedule in schedules:
                print(f"""
                    Nombres: {schedule["affiliate"]["first_name"]}
                    Apellidos: {schedule["affiliate"]["last_name"]}
                    Documento de Identidad: {schedule["affiliate"]["affiliate_id"]}
                    Direcci??n: {schedule["affiliate"]["address"]}
                    Tel??fono: {schedule["affiliate"]["phone"]}
                    Correo: {schedule["affiliate"]["email"]}
                    Fecha de Nacimiento: {datetime.datetime.fromtimestamp(schedule["affiliate"]["birth_date"]).strftime("%d/%m/%Y")}
                    Ciudad: {schedule["affiliate"]["city"]}
                    Lote de Vacunas: {schedule["vaccine_lot"]["vaccine_lot_id"]}
                    Fecha y Hora de Vacunaci??n: {datetime.datetime.fromtimestamp(schedule["date_time"]).strftime("%d/%m/%Y, %H:%M:%S")}
                """)   
                print("------------------------------------------------------------------------------")
        else:
            print("NO HAY PROGRAMACI??N DE VACUNACI??N DISPONIBLE ")

        end_options = {
            1: ['Volver al men?? principal', self.main_menu],
            2: ['Salir', self.exit_interface]}

        print("------------------------------------------------------------------------------")
        print(f"[1]{end_options[1][0]}    [2]{end_options[2][0]}")
        selected = int(input('>> '))
        end_options[selected][1]()

    def get_vaccination_schedule(self):
        def refresh():
            self.refresh_console()
            print("------------------------------------------------------------------------------")
            print("            men?? de programaci??n > CONSULTAR PROGRAMACI??N AFILIADO            ")
            print("------------------------------------------------------------------------------")

        refresh()

        validated = False
        input_text = ''
        while not validated:
            regex = re.compile(r"{}".format('\d{1,12}'))
            input_text = input('Ingrese N??mero de Identificaci??n: ')
            validated = re.fullmatch(regex, input_text)
            if not validated : 
                print('N??mero de Identificaci??n INV??LIDO, ingrese hasta 12 d??gitos.')
        refresh()
        schedule = self.vaccination_scheduler.get_schedule(int(input_text))

        if bool(schedule):
            print(f"""
                Nombres: {schedule["affiliate"]["first_name"]}
                Apellidos: {schedule["affiliate"]["last_name"]}
                Documento de Identidad: {schedule["affiliate"]["affiliate_id"]}
                Direcci??n: {schedule["affiliate"]["address"]}
                Tel??fono: {schedule["affiliate"]["phone"]}
                Correo: {schedule["affiliate"]["email"]}
                Fecha de Nacimiento: {datetime.datetime.fromtimestamp(schedule["affiliate"]["birth_date"]).strftime("%d/%m/%Y")}
                Ciudad: {schedule["affiliate"]["city"]}
                Lote de Vacunas: {schedule["vaccine_lot"]["vaccine_lot_id"]}
                Fecha y Hora de Vacunaci??n: {datetime.datetime.fromtimestamp(schedule["date_time"]).strftime("%d/%m/%Y, %H:%M:%S")}
            """)   
            print("------------------------------------------------------------------------------")
        else:
            print("NO HAY PROGRAMACI??N DE VACUNACI??N DISPONIBLE ")

        end_options = {
            1: ['Volver al men?? principal', self.main_menu],
            2: ['Salir', self.exit_interface]}

        print("------------------------------------------------------------------------------")
        print(f"[1]{end_options[1][0]}    [2]{end_options[2][0]}")
        selected = int(input('>> '))
        end_options[selected][1]()

    def vaccination_schedule_menu(self):
        self.refresh_console()
        options = {
            'title':['MEN?? DE PROGRAMACI??N DE VACUNACI??N'],
            1: ['Crear Programaci??n de Vacunaci??n ', self.create_vaccination_schedule],
            2: ['Consultar Programaci??n', self.get_all_vaccination_schedule],
            3: ['Consultar Programaci??n de Afiliado', self.get_vaccination_schedule],
            4: ['Regresar al Men?? Principal', self.main_menu],
            5: ['Salir', self.exit_interface],
            'range' : [] }
        options['range'] = [i for i in range(1,len(options)-1)]

        selected = self.print_menu(options, options['range'])
        options[selected][1]()


    # AFFILIATES UI MENU
    def affiliates_menu(self):
        self.refresh_console()
        options = {
            'title':['MEN?? DE AFILIADOS'],
            1: ['Crear Afiliado', self.add_user],
            2: ['Consultar Afiliado', self.get_user_by_id],
            3: ['Vacunaci??n de Afiliado', self.vaccination_update_menu],
            4: ['Regresar al Men?? Principal', self.main_menu],
            5: ['Salir', self.exit_interface],
            'range' : [] }
        options['range'] = [i for i in range(1,len(options)-1)]

        selected = self.print_menu(options, options['range'])
        options[selected][1]()

    def add_user(self):

        user_attr = {
            0: {'text':'N??mero de Identificaci??n: ', 'id': 'affiliate_id', 'content': '', 'regex': '\d{1,12}', 'alert':'N??mero de Identificaci??n INV??LIDO, ingrese hasta 12 d??gitos.'},
            1: {'text': 'Nombres: ', 'id': 'first_name', 'content': '', 'regex': '[a-zA-Z ????????????]{1,26}', 'alert':'Nombre INV??LIDO, por favor use s??lo car??cteres alfab??ticos.[hasta 26 caract??res]'},
            2: {'text': 'Apellidos: ', 'id': 'last_name', 'content': '', 'regex': '[a-zA-Z ????????????]{1,26}', 'alert':'Apellido INV??LIDO, por favor use s??lo car??cteres alfab??ticos.[hasta 26 caract??res]'},
            3: {'text': 'Direcci??n: ', 'id': 'address', 'content': '', 'regex': '[\w| |\-|#]{1,256}', 'alert':'Direcci??n INV??LIDA, por favor use s??lo car??cteres alfanum??ricos.'},
            4: {'text': 'Tel??fono: ', 'id': 'phone', 'content': '', 'regex': '\d{7,10}', 'alert':'N??mero de Tel??fono INV??LIDO, ingrese 7 o 10 d??gitos.'},
            5: {'text': 'Email: ', 'id': 'email', 'content': '', 'regex': '(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', 'alert':'Correo electr??nico INV??LIDO, ingrese un correo de la forma correo@email.com'},
            6: {'text': 'Ciudad: ', 'id': 'city', 'content': '', 'regex': '[a-zA-Z ????????????]{1,20}', 'alert':'Ciudad INV??LIDA, por favor use s??lo car??cteres alfab??ticos.'},
            7: {'text': 'Fecha de Nacimiento: ', 'id': 'birth_date', 'content': '', 'regex': '^(0[1-9]|1[0-9]|2[0-9]|3[0-1])/(0[1-9]|1[0-2])/(19[0-9]{2}|2[0-9]{3})$', 'alert':'Por favor, ingrese la fecha con el formato DD/MM/AAAA'},
            8: {'text': 'Fecha de Afiliaci??n: ', 'id': 'affiliation_date', 'content': '', 'regex': '^(0[1-9]|1[0-9]|2[0-9]|3[0-1])/(0[1-9]|1[0-2])/(19[0-9]{2}|2[0-9]{3})$', 'alert':'Por favor, ingrese la fecha con el formato DD/MM/AAAA'}
        }

        for index in range(len(user_attr)):
            self.refresh_console()
            print("------------------------------------------------------------------------------")
            print("                     men?? de afiliados > CREAR AFILIADO                       ")
            print("------------------------------------------------------------------------------")
            for i in range(index+1):
                if index == i and not user_attr[index]['content']:
                    test_input = self.input_validation("", user_attr[index]['regex'], user_attr[index]['alert'], user_attr[index]['text'])
                    if index == 7 or index == 8:
                        test_input = self.str_to_date(test_input)
                        if index == 8 and user_attr[7]['content'] > test_input:
                            while user_attr[7]['content'] > test_input:
                                print("??Usuario afiliado antes de nacer? vuelve a ingresar la fecha de afiliaci??n.")
                                test_input = self.input_validation("", user_attr[index]['regex'], user_attr[index]['alert'], user_attr[index]['text'])
                                test_input = self.str_to_date(test_input)
                    elif index == 0:
                        test_input = int(test_input)

                    user_attr[index]['content'] = test_input
                else:
                    if i == 7 or i == 8:
                        print(f"{user_attr[i]['text']}{datetime.datetime.fromtimestamp(user_attr[i]['content']).date().strftime('%d/%m/%Y')}")
                    else:
                        print(f"{user_attr[i]['text']}{user_attr[i]['content']}")
            
                
        end_options = {
            2: ['Descartar', self.affiliates_menu],
            3: ['Volver al men?? principal', self.main_menu],
            4: ['Salir', self.exit_interface]}

        print("------------------------------------------------------------------------------")
        print(f"[1]Agregar   [2]{end_options[2][0]}    [3]{end_options[3][0]}    [4]{end_options[4][0]}")
        selected = int(input('>> '))
        if selected == 1:
            res = self.affiliate_manager.add(affiliate.Affiliate(user_attr[0]['content'], 
                                                                 user_attr[1]['content'], 
                                                                 user_attr[2]['content'], 
                                                                 user_attr[3]['content'], 
                                                                 user_attr[4]['content'], 
                                                                 user_attr[5]['content'], 
                                                                 user_attr[6]['content'], 
                                                                 user_attr[7]['content'], 
                                                                 user_attr[8]['content']))
            if res:
                print(f"Usuario {user_attr[0]['content']} a??adido exitosamente.")
            else:
                print(f"Usuario {user_attr[0]['content']} -  y?? existe en la base de datos.")

            time.sleep(3)
            self.affiliates_menu()
        else:
            end_options[selected][1]()

    def get_user_by_id(self):
        self.refresh_console()
        print("------------------------------------------------------------------------------")
        print("                   men?? de afiliados > CONSULTAR AFILIADO                     ")
        print("------------------------------------------------------------------------------")
        print("Por favor, ingrese el [N??mero de Identificaci??n] del afiliado.")
        validated = False
        affiliate_id = 0
        while not validated:
            affiliate_id = input(">> ")
            regex = re.compile(r"\d{1,12}")
            validated = re.fullmatch(regex, affiliate_id)
            if not validated : 
                print(f"N??mero de Identificaci??n INV??LIDO, ingrese hasta 12 d??gitos.\n")
        affiliate_id = int(affiliate_id)
        user_data = self.affiliate_manager.find(affiliate_id)
        if user_data:
            user_data = self.user_formatting(user_data)
            for key, data in user_data.items():
                print(f"                   {data['rename']}{data['formatted']}")
            affiliation = user_data['affiliation_date']['original']
        else:
            print(f"\nNo se encontr?? el usuario con el ID {affiliate_id}\n")
            end_options = {
                1: ['Nueva consulta', self.get_user_by_id],
                2: ['Atr??s', self.affiliates_menu],
                3: ['Volver al men?? principal', self.main_menu],
                4: ['Salir', self.exit_interface]}
            self.end_options_menu(end_options, 4)
        
        
        end_options = {
            1: ['Nueva consulta', self.get_user_by_id],
            2: ['Afiliar/Desafiliar', self.user_affiliation],
            3: ['Atr??s', self.affiliates_menu],
            4: ['Salir', self.exit_interface]}
        self.end_options_menu(end_options, 4, [{'key': 2, 'args':(affiliate_id, affiliation)}])

    def user_formatting(self, user_data):
        rename = {
            'affiliate_id': 'N??mero de Identificaci??n: ',       
            'first_name': 'Nombres: ',         
            'last_name': 'Apellidos: ',          
            'address': 'Direcci??n: ',             
            'phone': 'Tel??fono: ',                 
            'email': 'Email: ',                 
            'city': 'Ciudad: ',                   
            'birth_date': 'Fecha de Nacimiento: ',         
            'affiliation_date': 'Fecha de Afiliaci??n: ',   
            'vaccinated': '??Fu?? Vacunado?: ',         
            'disaffiliation_date': 'Fecha de Desafiliaci??n: '
        }
        data_formatted = {}
        for key, data in user_data.items():
            item_formatted = {'original':data}
            if key == 'birth_date' or key == 'affiliation_date' or key == 'disaffiliation_date':
                if data:
                    data = datetime.datetime.fromtimestamp(data).date().strftime('%d/%m/%Y')
            elif key == 'vaccinated':
                if data:
                    data = 'SI'
                else:
                    data = 'NO'
            item_formatted['formatted'] = data
            item_formatted['rename'] = rename[key]
            data_formatted[key] = item_formatted
        return data_formatted

    def user_affiliation(self, affiliate_id, affiliation):
        self.refresh_console()
        print("------------------------------------------------------------------------------")
        print("                  Gesti??n de afiliados > AFILIAR/DESAFILIAR                   ")
        print("------------------------------------------------------------------------------")

        re_str = "^(0[1-9]|1[0-9]|2[0-9]|3[0-1])/(0[1-9]|1[0-2])/(19[0-9]{2}|2[0-9]{3})$"
        validated = False
        new_date = 0
        if affiliation:
            new_date = self.input_validation("Ingrese la fecha de [DESAFILIACI??N].", re_str, "Por favor, ingrese la fecha con el formato DD/MM/AAAA")
            new_date = self.str_to_date(new_date)
            res = self.affiliate_manager.disaffiliate(affiliate_id, new_date)
            if res:
                print(f"El usuario con ID: {affiliate_id}, fu?? DESAFILIADO dada la fecha suministrada.")
            else:
                print(f"El usuario con ID: {affiliate_id}, NO fu?? DESAFILIADO intentelo de nuevo.")

            affiliation = 0
        else:
            new_date = self.input_validation("Ingrese la fecha de [AFILIACI??N].", re_str, "Por favor, ingrese la fecha con el formato DD/MM/AAAA")
            new_date = self.str_to_date(new_date)
            res = self.affiliate_manager.affiliate_(affiliate_id, new_date)
            if res:
                print(f"El usuario con ID: {affiliate_id}, fu?? AFILIADO exitosamente en la fecha indicada.")
            else:
                print(f"El usuario con ID: {affiliate_id}, NO fu?? AFILIADO intentelo de nuevo.")

            affiliation = new_date
        
        end_options = {
            1: ['Nueva consulta', self.get_user_by_id],
            2: ['Afiliar/Desafiliar', self.user_affiliation],
            3: ['Atr??s', self.affiliates_menu],
            4: ['Volver al men?? principal', self.main_menu],
            5: ['Salir', self.exit_interface]}
        self.end_options_menu(end_options, 5, [{'key': 2, 'args':(affiliate_id, affiliation)}])

    def vaccination_update_menu(self):
        self.refresh_console()
        print("------------------------------------------------------------------------------")
        print("                       men?? de afiliados > VACUNACI??N                         ")
        print("------------------------------------------------------------------------------")
        affiliate_id = self.input_validation("Ingrese el ID de la persona a vacunar.", "\d{1,12}", "N??mero de Identificaci??n INV??LIDO, ingrese hasta 12 d??gitos.\n")
        affiliate_id = int(affiliate_id)

        res = self.affiliate_manager.vaccinate(affiliate_id)
        if res == 0:
            print(f"Usuario [{affiliate_id}] - Registro de vacunaci??n [EXITOSO] .")
        elif res == 1:
            print(f"Error usuario [{affiliate_id}] no pudo ser vacunado intente nuevamente.")
        elif res == 2:
            print(f"No existe un plan de vacunaci??n relacionado al usuario con ID {affiliate_id}")
        elif res == 3:
            print(f"Usuario [{affiliate_id}] ya ha sido vacunado, intente con otro ID.")
        elif res == 4:
            print(f"No existe un plan de vacunaci??n relacionado al usuario con ID {affiliate_id}") 

        
        end_options = {
            1: ['Seguir Vacunando', self.vaccination_update_menu],
            2: ['Atr??s', self.affiliates_menu],
            3: ['Volver al men?? principal', self.main_menu],
            4: ['Salir', self.exit_interface]
        }
        self.end_options_menu(end_options, 4)
    

if __name__ == '__main__':
    main_interface = Interface()
    main_interface.main_menu()
    