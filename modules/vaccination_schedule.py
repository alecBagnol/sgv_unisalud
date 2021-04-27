from modules import create_connect as db

def create_vaccination_schedule(
        id,
        date_time,
        affiliate_id,
        vaccine_lot_id,
        vaccination_plan_id
    ):
    conn = db.create_or_connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO VaccinationSchedule VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (
        id,
        date_time,
        affiliate_id,
        vaccine_lot_id,
        vaccination_plan_id
    ))
    
    conn.commit()
    conn.close()

    