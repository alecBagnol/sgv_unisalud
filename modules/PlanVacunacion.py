# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 09:32:42 2021

@author: Pipe Alvarez
"""

import sqlite3
from sqlite3 import Error
from datetime import datetime, date, time

def planvac_sql_conexion():
    """
    Crea la conexión a la base de datos "PlanVacunacion".

    Retorna:
        una conexión (sqlite3) a la base de datos "PlanVacunacion" (db)
    """
    try:
        con = sqlite3.connect('PlanVacunacion.db')
        return con
    except Error:
        print(Error)

def planvac_crear_sql_tabla(con):
    """
    Crea la base de datos "PlanVacunacion".
    
    Args:
        con: conexión (sqlite3) a la base de datos "PlanVacunacion"    
    """
    cursor = con.cursor()
    cursor.execute("CREATE TABLE PlanVacunacion(idplan integer PRIMARY KEY, edadminima integer, edadmaxima integer, fechainicioplan text, fechafinplan text)")
    con.commit()
    
def planvac_solicitar_info():
    """
    Solicita los datos necesarios para una instancia de "PlanVacunacion".
    
    Retorna:
        los datos de una instancia de "PlanVacunacion" (tuple).
    """
    idplan = input("Identificación del Plan de Vacunación: ")
    idplan = idplan.ljust(2)
    edadminima = input("Edad mínima de los Afiliados del Plan de Vacunación: ")
    edadminima = edadminima.ljust(3)
    edadmaxima = input("Edad máxima de los Afiliados del Plan de Vacunación: ")
    edadmaxima = edadmaxima.ljust(3)
    fechainicioplan = input("Fecha de inicio del Plan de Vacunación (DD/MM/AAAA): ")
    fechainicioplan = fechainicioplan.ljust(10)
    fechafinplan = input("Fecha de finalización del Plan de Vacunación (DD/MM/AAAA): ")
    fechafinplan = fechafinplan.ljust(10)
    planvac = idplan, edadminima, edadmaxima, fechainicioplan, fechafinplan
    return planvac

def planvac_insertar_sql_tabla(con, planvac):
    """
    Inserta los datos de una instancia de "PlanVacunacion" en la base de datos "PlanVacunacion".
    
    Args:
        con: conexión (sqlite3) a la base de datos "PlanVacunacion"
        planvac: datos instancia de "PlanVacunacion" (tuple)      
    """
    cursor = con.cursor()
    cursor.execute('''INSERT INTO PlanVacunacion(idplan, edadminima, edadmaxima, fechainicioplan, fechafinplan) VALUES(?, ?, ?, ?, ?)''', planvac)
    con.commit()
    
def planvac_consultar_sql_tabla(con):
    """
    Consulta la información vigente de una instancia de "PlanVacunacion" con respecto al día actual.
    
    Args:
        con: conexión (sqlite3) a la base de datos "PlanVacunacion"
    Retorna:
        el estado actual de la instancia de "PlanVacunacion" (str).
    """
    try:
        cursor = con.cursor()
        planvac = input("Identificación del Plan de Vacunación a consultar: ")
        consultar = 'SELECT * FROM PlanVacunacion where idplan = ' + planvac
        cursor.execute(consultar)
        planvac_registros = cursor.fetchall()
        fecha_actual = date.today()
        fechainicioplan = datetime.strptime(planvac_registros[0][3], '%d/%m/%Y').date()
        fechafinplan = datetime.strptime(planvac_registros[0][4], '%d/%m/%Y').date()
        if (fechainicioplan - fecha_actual).days > 0:
            print('El Plan de Vacunación no ha iniciado.')
        elif (fechainicioplan - fecha_actual).days <= 0 and (fechafinplan - fecha_actual).days >= 0:
            print('El Plan de Vacunación está en curso y está dirigido para la población con edades entre ' 
                  + str(planvac_registros[0][1]) + ' y ' + str(planvac_registros[0][2]) + ' años.')
        else:
            print('El Plan de Vacunación ya terminó.')
        con.commit()
        return fechainicioplan, fechafinplan
    except IndexError:
        print('Identificación del Plan de Vacunación no existente')

def main():
    con = planvac_sql_conexion()
    try:
        planvac_crear_sql_tabla(con)
    except Error:
        pass
    #planvac = planvac_solicitar_info()
    #planvac_insertar_sql_tabla(con, planvac)
    planvac_consultar_sql_tabla(con)
    
main()