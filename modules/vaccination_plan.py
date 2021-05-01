# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 09:32:42 2021

@author: Pipe Alvarez
"""

from modules import create_connect as db
from contextlib import closing
from modules import utils

def create_vaccination_plan(vaccination_plan_id, min_age, max_age, start_date, end_date):
    """
    Creates one instance of Vaccination Plan.
    
    Args:
        vaccination_plan_id: identification of the Vaccination Plan (int)
        minimum_age: minimum age of the Vaccination Plan (int)
        maximum_age: maximum age of the Vaccination Plan (int)
        start_date: start date of the Vaccination Plan (int)
        end_date: end date of the Vaccination Plan (int)
    """
    try:
        with db.create_or_connect() as con:
            with closing(con.cursor()) as cursor:
                cursor.execute("SELECT * from VaccinationPlan WHERE (?) BETWEEN minimum_age AND maximum_age OR (?) BETWEEN minimum_age AND maximum_age", (min_age, max_age,))
                l = cursor.fetchall()
                if len(l) != 0:
                    return False
                cursor.execute("INSERT INTO VaccinationPlan (vaccination_plan_id , minimum_age, maximum_age, start_date, end_date) VALUES(?, ?, ?, ?, ?)", (
                        vaccination_plan_id,
                        min_age,
                        max_age,
                        start_date,
                        end_date))
                return True    
    except:
        return False
    
def consult_vaccination_plan(vaccination_plan_id):
    """
    Consults the information of one instance of Vaccination Plan by vaccination_plan_id.
    
    Args:
        vaccination_plan_id: identification of the Vaccination Plan (int)
        
    Returns:
        a dictionay with the information of one instance of Vaccination Plan: the name of the field (key) with its corresponding value
    """
    try:
        with db.create_or_connect() as con:
            with closing(con.cursor()) as cursor:
                cursor.execute("SELECT * from VaccinationPlan WHERE vaccination_plan_id = (?)", (vaccination_plan_id,))
                record = cursor.fetchone()
                return utils.dict_factory(cursor, record)
    except:
        return {}