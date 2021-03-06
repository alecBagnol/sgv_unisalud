from modules import create_connect as db
from contextlib import closing
from modules import utils
from modules.emails import email_manager
from datetime import datetime, timedelta, date

"""
    Vaccination Schedule

    Description:
        This class represents a vaccination schedule and all its properties.    
"""
class VaccinationSchedule:
    def __init__(self, date_time, affiliate_id, vaccine_lot_id, vaccination_plan_id):
        self.__date_time = date_time
        self.__affiliate_id = affiliate_id
        self.__vaccine_lot_id = vaccine_lot_id
        self.__vaccination_plan_id = vaccination_plan_id

    def set_date_time(self, date_time):
        self.__date_time = date_time
    def get_date_time(self):
        return self.__date_time
    
    def set_affiliate_id(self, affiliate_id):
        self.__affiliate_id = affiliate_id
    def get_affiliate_id(self):
        return self.__affiliate_id

    def set_vaccine_lot_id(self, vaccine_lot_id):
        self.__vaccine_lot_id = vaccine_lot_id
    def get_vaccine_lot_id(self):
        return self.__vaccine_lot_id
    
    def set_vaccination_plan_id(self, vaccination_plan_id):
        self.__vaccination_plan_id = vaccination_plan_id
    def get_vaccination_plan_id(self):
        return self.__vaccination_plan_id


"""
    Vaccination Schedule Manager

    Description:
        This class is in charge of managing vaccination schedules within database.
"""
class VaccinationScheduleManager:
    """
        Description:
            Creates a single row into VaccinationSchedule table as long as
            affiliate_id, vaccine_lot_id, vaccination_plan_id are foreing keys
            they need to be valid ids, in case a non valid id is given
            Exception will be thrown.

        Parameters:
            * vaccination_schedule_id: primary key id for the new row in VaccinationSchedule.
            * date_time: timestamp indicating exact date and time when the affiliate must be vaccinated. 
            * affiliate_id: id of the affiliated.
            * vaccine_lot_id: lot id of the vaccine that is going to be used. 
            * vaccination_plan_id: id of the plan associated to the vaccination schedule. 
    """
    def create_vaccination_schedule(
            self,
            vaccination_schedule: VaccinationSchedule
        ):
        try:
            with db.create_or_connect() as con:
                with closing(con.cursor()) as cursor:
                    cursor.execute("INSERT INTO VaccinationSchedule (date_time, affiliate_id, vaccine_lot_id, vaccination_plan_id) VALUES (?, ?, ?, ?)", (
                        vaccination_schedule.get_date_time(),
                        vaccination_schedule.get_affiliate_id(),
                        vaccination_schedule.get_vaccine_lot_id(),
                        vaccination_schedule.get_vaccination_plan_id(),
                    ))
                    return True
                    
        except:
            return False


    """
        Description:
            Calculates age given birth date.

        Parameters:
            birth date.
    """
    def __calculate_age(self, born):
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


    """
        Description:
            Creates all the vaccination schedule based on a given date_time, this function
            will assing an schedule to all the non vacinated affiliates that meets into a 
            vaccination plan age.

        Parameters:
            * date_time: date and time from when the vaccination schedule will start being set.
    """
    def create_all_vaccination_schedule(self, date_time):
        try:
            with db.create_or_connect() as con:
                with closing(con.cursor()) as cursor:
                    ans = True
                    cursor.execute("SELECT * from VaccineLot WHERE amount >= used_amount")
                    lots_tuple = cursor.fetchall()

                    if len(lots_tuple) == 0:
                        return

                    lots = []
                    for l in lots_tuple:
                        lots.append(list(l))

                    cursor.execute("SELECT * from VaccinationPlan WHERE (?) BETWEEN start_date AND end_date", (date_time, ))
                    date_obj = datetime.fromtimestamp(date_time)

                    plans = cursor.fetchall()
                    lots[0][3] -= lots[0][4]

                    messages = []
                    for plan in plans:
                        cursor.execute("SELECT * from Affiliate WHERE vaccinated = False AND disaffiliation_date IS NULL")
                        affiliates = cursor.fetchall()
                        for affiliate in affiliates:
                                age = self.__calculate_age(datetime.fromtimestamp(affiliate[7]))
                                if plan[1] <= age and age <= plan[2]:
                                    ans = ans and self.create_vaccination_schedule(VaccinationSchedule(date_obj.timestamp(), affiliate[0], lots[0][0], plan[0]))
                                    
                                    messages.append((affiliate[1], affiliate[5], date_obj.strftime("%m/%d/%Y, %H:%M:%S"), affiliate[6]))
                        
                                    date_obj += timedelta(minutes=30)
                                    lots[0][3] -= 1
                                    if not lots[0][3]:
                                        lots.pop(0)
                                        if not len(lots):
                                            break
                                        lots[0][3] -= lots[0][4]
                        if not len(lots):
                            break
                    email_manager.send_messages(messages)
                    return ans
        except:
            return False


    """
        Description:
            Gets all vaccination schedules that were created sorted based on date and time
            assigned.

        Returns:
            Dict containing all vaccination schedules.
    """
    def get_all(self):
        res = []
        try:
            with db.create_or_connect() as con:
                with closing(con.cursor()) as cursor:
                    cursor.execute("SELECT * from VaccinationSchedule ORDER BY date_time")
                    schedules = cursor.fetchall()

                    for schedule in schedules:
                        cursor.execute("SELECT * from Affiliate WHERE affiliate_id = (?)", (schedule[2],))
                        affiliate = utils.dict_factory(cursor, cursor.fetchone())
                        cursor.execute("SELECT * from VaccineLot WHERE vaccine_lot_id = (?)", (schedule[3],))
                        vaccine_lot = utils.dict_factory(cursor, cursor.fetchone())
                        cursor.execute("SELECT * from VaccinationPlan WHERE vaccination_plan_id = (?)", (schedule[4],))
                        vaccination_plan = utils.dict_factory(cursor, cursor.fetchone())
                        res.append({
                            "vaccination_schedule_id": schedule[0],
                            "date_time": schedule[1],
                            "affiliate": affiliate,
                            "vaccine_lot": vaccine_lot,
                            "vaccination_plan": vaccination_plan
                        })
                    
                    return res
        except:
            return []


    """
        Description:
            Gets vaccination schedule of a given affiliate.

        Parameters:
            * affiliate_id: Id of the affiliated.
        
        Returns:
            Vaccination plan for a given affiliated.
    """
    def get_schedule(self, affiliate_id):
        res = {}
        try:
            with db.create_or_connect() as con:
                with closing(con.cursor()) as cursor:
                    cursor.execute("SELECT * from VaccinationSchedule WHERE affiliate_id = (?)", (affiliate_id, ))
                    schedule = cursor.fetchone()

                    cursor.execute("SELECT * from Affiliate WHERE affiliate_id = (?)", (schedule[2],))
                    affiliate = utils.dict_factory(cursor, cursor.fetchone())
                    cursor.execute("SELECT * from VaccineLot WHERE vaccine_lot_id = (?)", (schedule[3],))
                    vaccine_lot = utils.dict_factory(cursor, cursor.fetchone())
                    cursor.execute("SELECT * from VaccinationPlan WHERE vaccination_plan_id = (?)", (schedule[4],))
                    vaccination_plan = utils.dict_factory(cursor, cursor.fetchone())

                    res = {
                        "vaccination_schedule_id": schedule[0],
                        "date_time": schedule[1],
                        "affiliate": affiliate,
                        "vaccine_lot": vaccine_lot,
                        "vaccination_plan": vaccination_plan
                    }
                    
                    return res
        except:
            return {}
