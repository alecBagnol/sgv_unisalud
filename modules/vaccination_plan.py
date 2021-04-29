# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 09:32:42 2021

@author: Pipe Alvarez
"""

import create_connect as db

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
    conn = db.create_or_connect()
    cursor = conn.cursor()
    
    vacplan = id , minumum_age , maximum_age , start_date , end_date
    cursor.execute('''INSERT INTO VaccinationPlan(id , minumum_age , maximum_age , start_date , end_date) VALUES(?, ?, ?, ?, ?)''', vacplan)
    
    conn.commit()
    conn.close()
    
def vacplan_consult(idplan):
    """
    Consults the information of one instance of Vaccination Plan by idplan.
    
    Args:
        idplan: identification of the Vaccination Plan (int)
        
    Returns:
        a dictionay with the information of one instance of Vaccination Plan: the name of the field (key) with its corresponding value
    """
    conn = db.create_or_connect()
    cursor = conn.cursor()
        
    cursor.execute("SELECT * from VaccinationPlan WHERE idplan = (?)",(id,))
    records = cursor.fetchall()
    return {'idplan': records[0][0], 'minage': records[0][1], 'maxage': records[0][2], 'startdate': records[0][3], 
            'enddate': records[0][4]}
        
    conn.commit()
    conn.close()