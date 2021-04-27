CREATE TABLE IF NOT EXISTS Affiliates(
    id number PRIMARY KEY,
    first_name text,
    last_name text,
    address text,
    phone text,
    email text,
    city text,
    birth_date number,
    affiliation_date number,
    vaccinated boolean ,
    disaffiliation_date number,
    vaccination_schedule_id number
);

CREATE TABLE IF NOT EXISTS VaccineLot(
    id number PRIMARY KEY,
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
    id number PRIMARY KEY,
    minumum_age number,
    maximum_age number,
    start_date number,
    end_date number,
    city text
);

CREATE TABLE IF NOT EXISTS VaccinationSchedule(
    id number PRIMARY KEY,
    date_time number,
    affiliate_id number,
    vaccine_lot_id number,
    vaccination_plan_id number
);