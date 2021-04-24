CREATE TABLE Affiliate(
    id number PRIMARY KEY,
    name text,
    family_name text,
    direction text,
    phone text,
    email text,
    city text,
    birth_date number,
    affiliation_date number,
    vaccinated boolean ,
    disaffiliation_date number,
    vaccination_schedule_id number
);

CREATE TABLE VaccineLot(
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

CREATE TABLE VaccinationPlan(
    id number PRIMARY KEY,
    minumum_age number,
    maximum_age number,
    start_date number,
    end_date number
);

CREATE TABLE VaccinationSchedule(
    id number PRIMARY KEY,
    city text,
    vaccine_lot_id number,
    date_time number,
    affiliate_id number
);