from modules import create_connect as db
from modules import utils
from datetime import datetime, timedelta, date

"""
    Description:
        Creates a single row into VaccinationSchedule table as long as
        affiliate_id, vaccine_lot_id, vaccination_plan_id are foreing keys
        they need to be valid ids, in case a non valid id is given
        Exception will be thrown.


    Parameters:
        vaccination_schedule_id: primary key id for the new row in VaccinationSchedule.

        date_time: timestamp indicating exact date and time when the affiliate must be
                   vaccinated. 

        affiliate_id: id of the affiliated.

        vaccine_lot_id: lot id of the vaccine that is going to be used. 
        
        vaccination_plan_id: id of the plan associated to the vaccination schedule. 
"""
def create_vaccination_schedule(
        date_time,
        affiliate_id,
        vaccine_lot_id,
        vaccination_plan_id
    ):
    conn = db.create_or_connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO VaccinationSchedule (date_time, affiliate_id, vaccine_lot_id, vaccination_plan_id) VALUES (?, ?, ?, ?)", (
        date_time,
        affiliate_id,
        vaccine_lot_id,
        vaccination_plan_id,
    ))
    
    conn.commit()
    conn.close()
    

"""
    Description:
        Calculates age given birth date.

    Parameters:
        birth date.
"""
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


"""
    Description:
        Creates all the vaccination schedule based on a given date_time, this function
        will assing an schedule to all the non vacinated affiliates that meets into a 
        vaccination plan age.

    Parameters:
        date_time: date and time from when the vaccination schedule will start being set.
"""
def create_all_vaccination_schedule(date_time):
    conn = db.create_or_connect()
    cursor = conn.cursor()
 
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

    for plan in plans:
        cursor.execute("SELECT * from Affiliate WHERE vaccinated = False")
        affiliates = cursor.fetchall()
        for affiliate in affiliates:
                age = calculate_age(datetime.fromtimestamp(affiliate[7]))
                if plan[1] <= age and age <= plan[2]:
                    create_vaccination_schedule(date_obj.timestamp(), affiliate[0], lots[0][0], plan[0])
                    
                    ###############
                    #sending email#
                    ###############
        
                    date_obj += timedelta(minutes=30)
                    lots[0][3] -= 1
                    if not lots[0][3]:
                        lots.pop(0)
                        if not len(lots):
                            return
                        lots[0][3] -= lots[0][4]

    conn.commit()
    conn.close()


"""
    Description:
        Gets all vaccination schedules that were created sorted based on date and time
        assigned.

    Returns:
        Dict containing all vaccination schedules.
"""
def get_all():
    res = []
    conn = db.create_or_connect()
    cursor = conn.cursor()
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

    conn.commit()
    conn.close()
    return res


"""
    Description:
        Gets vaccination schedule of a given affiliate.

    Parameters:
        affiliate_id: Id of the affiliated.
    
    Returns:
        Vaccination plan for a given affiliated.
"""
def get_schedule(affiliate_id):
    res = {}
    conn = db.create_or_connect()
    cursor = conn.cursor()
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

    conn.commit()
    conn.close()
    return res