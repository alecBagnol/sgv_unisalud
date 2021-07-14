# -*- coding: utf-8 -*-
"""
    Created on Sat Apr 24 09:32:42 2021
    @author: Pipe Alvarez
"""

from modules import create_connect as db
from contextlib import closing
from modules import utils

class VaccinationPlan:
    def __init__(self, vaccination_plan_id, min_age, max_age, start_date, end_date):
        self.__vaccination_plan_id = vaccination_plan_id
        self.__min_age = min_age
        self.__max_age = max_age
        self.__start_date = start_date
        self.__end_date = end_date
    
    def set_vaccination_plan_id(self, vaccination_plan_id):
        self.__vaccination_plan_id = vaccination_plan_id
    def get_vaccination_plan_id(self):
        return self.__vaccination_plan_id

    def set_min_age(self, min_age):
        self.__min_age = min_age
    def get_min_age(self):
        return self.__min_age

    def set_max_age(self, max_age):
        self.__max_age = max_age
    def get_max_age(self):
        return self.__max_age
    
    def set_start_date(self, start_date):
        self.__start_date = start_date
    def get_start_date(self):
        return self.__start_date

    def set_end_date(self, end_date):
        self.__end_date = end_date
    def get_end_date(self):
        return self.__end_date

class VaccinationPlanManager:
    """
        Creates one instance of Vaccination Plan.
        
        Args:
            vaccination_plan_id: identification of the Vaccination Plan (int)
            minimum_age: minimum age of the Vaccination Plan (int)
            maximum_age: maximum age of the Vaccination Plan (int)
            start_date: start date of the Vaccination Plan (int)
            end_date: end date of the Vaccination Plan (int)
    """
    def create_vaccination_plan(self, vaccination_plan: VaccinationPlan):
        try:
            with db.create_or_connect() as con:
                with closing(con.cursor()) as cursor:
                    cursor.execute("SELECT * from VaccinationPlan WHERE (?) BETWEEN minimum_age AND maximum_age OR (?) BETWEEN minimum_age AND maximum_age", 
                                   (vaccination_plan.get_min_age(), vaccination_plan.get_max_age(),))
                    l = cursor.fetchall()
                    if len(l) != 0:
                        return False
                    cursor.execute("INSERT INTO VaccinationPlan (vaccination_plan_id , minimum_age, maximum_age, start_date, end_date) VALUES(?, ?, ?, ?, ?)", (
                            vaccination_plan.get_vaccination_plan_id(),
                            vaccination_plan.get_min_age(),
                            vaccination_plan.get_max_age(),
                            vaccination_plan.get_start_date(),
                            vaccination_plan.get_end_date()))
                    return True    
        except:
            return False

    """
        Consults the information of one instance of Vaccination Plan by vaccination_plan_id.

        Args:
            vaccination_plan_id: identification of the Vaccination Plan (int)
            
        Returns:
            a dictionay with the information of one instance of Vaccination Plan: the name of the field (key) with its corresponding value
    """  
    def consult_vaccination_plan(self, vaccination_plan_id):
        try:
            with db.create_or_connect() as con:
                with closing(con.cursor()) as cursor:
                    cursor.execute("SELECT * from VaccinationPlan WHERE vaccination_plan_id = (?)", (vaccination_plan_id,))
                    record = cursor.fetchone()
                    return utils.dict_factory(cursor, record)
        except:
            return {}