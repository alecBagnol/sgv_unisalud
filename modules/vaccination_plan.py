# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 09:32:42 2021

@author: Pipe Alvarez
"""

import sqlite3
from sqlite3 import Error
from create_connect import create_or_connect as db_link

def vacplan_insert(id , minumum_age , maximum_age , start_date , end_date):
    """
    Inserts the information needed to instantiate one Vaccination Plan.
    
    Args:
        idplan: identification of the Vaccination Plan (int)
        minage: minimum age of the Vaccination Plan (int)
        maxage: maximum age of the Vaccination Plan (int)
        startdate: start date of the Vaccination Plan (int)
        enddate : end date of the Vaccination Plan (int)
    """
    conn = db_link()
    cursor = conn.cursor()
    
    vacplan = id , minumum_age , maximum_age , start_date , end_date
    cursor.execute('''INSERT INTO VaccinationPlan(id , minumum_age , maximum_age , start_date , end_date) VALUES(?, ?, ?, ?, ?)''', vacplan)
    
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
        
        cursor.execute("SELECT * from VaccinationPlan WHERE idplan = (?)",(id,))
        records = cursor.fetchall()
        for record in records:
            print(record)
        
        conn.commit()
        conn.close()
    except IndexError:
        print('Invalid id for Vaccination Plan')