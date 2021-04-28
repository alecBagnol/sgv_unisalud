CREATE TABLE IF NOT EXISTS Affiliate(
    affiliate_id integer PRIMARY KEY,
    first_name text,
    last_name text,
    address text,
    phone text,
    email text,
    city text,
    birth_date number,
    affiliation_date number,
    vaccinated boolean ,
    disaffiliation_date number
);

CREATE TABLE IF NOT EXISTS VaccineLot(
    vaccine_lot_id integer PRIMARY KEY,
    manufacturer text,
    vaccine_type text,
    amount number,
    used_amount number,
    dose number,
    temperature number,
    effectiveness number,
    protection_time number,
    expiration_date number,
    image_url text
);

CREATE TABLE IF NOT EXISTS VaccinationPlan(
    vaccination_plan_id integer PRIMARY KEY,
    minumum_age number,
    maximum_age number,
    start_date number,
    end_date number,
    city text
);

CREATE TABLE IF NOT EXISTS VaccinationSchedule(
    vaccination_schedule_id integer PRIMARY KEY,
    date_time number,
    affiliate_id number,
    vaccine_lot_id number,
    vaccination_plan_id number,
    FOREIGN KEY (affiliate_id) REFERENCES Affiliate (affiliate_id),
    FOREIGN KEY (vaccine_lot_id) REFERENCES VaccineLot (vaccine_lot_id),
    FOREIGN KEY (vaccination_plan_id) REFERENCES VaccinationPlan (vaccination_plan_id)
);