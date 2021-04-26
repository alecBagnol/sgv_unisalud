# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 09:32:42 2021

@author: Pipe Alvarez
"""

import sqlite3
from sqlite3 import Error
from datetime import datetime, date, time
from modules.create_connect import create_or_connect as db_link

def vacplan_insert(idplan, minage, maxage, startdate, enddate):
    """
    Inserts the information needed to instantiate one Vaccination Plan.
    
    Args:
        idplan: identification of the Vaccination Plan (int)
        minage: minimum age of the Vaccination Plan (int)
        maxage: maximum age of the Vaccination Plan (int)
        startdate: start date of the Vaccination Plan (str)
        enddate : end date of the Vaccination Plan (str)
    """
    conn = db_link()
    cursor = conn.cursor()
    vacplan = idplan, minage, maxage, startdate, enddate
    cursor.execute('''INSERT INTO vaccinationPlan(idplan, minage, maxage, startdate, enddate) VALUES(?, ?, ?, ?, ?)''', vacplan)
    conn.commit()
    conn.close()
    
def vacplan_consult(idplan):
    """
    Consults the infortmation of one instance of Vaccination Plan by idplan.
    
    Args:
        idplan: identification of the Vaccination Plan (int)
    """
    try:
        conn = db_link()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * from vaccinationPlan WHERE idplan = (?)",(idplan,))
        records = cursor.fetchall()
        for record in records:
            print(record)
        
        conn.commit()
        conn.close()
    except IndexError:
        print('Invalid idplan')