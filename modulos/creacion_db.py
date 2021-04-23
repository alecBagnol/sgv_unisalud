import sqlite3

def crear_tabla_cities():
    con = sqlite3.connect('./db/db_unisalud.db')
    cursor = con.cursor()

    cursor.execute("""CREATE TABLE cities (
        id integer NOT NULL PRIMARY KEY,
        city_name text
    )""")

    con.commit()
    con.close()

def crear_tabla_vaccines():
    con = sqlite3.connect('./db/db_unisalud.db')
    cursor = con.cursor()
    
    cursor.execute("""CREATE TABLE vaccines (
        id integer NOT NULL PRIMARY KEY,
        lab text,
        type text,
        doses text,
        storege_temp integer,
        expiration_date integer,
        effectiveness real,
        protection_time integer
    )""")

    con.commit()
    con.close()

def crear_tabla_vaccine_lot():
    con = sqlite3.connect('./db/db_unisalud.db')
    cursor = con.cursor()
    
    cursor.execute("""CREATE TABLE vaccine_lot (
        id integer NOT NULL PRIMARY KEY,
        vaccine_id integer,
        quantity integer,
        doses_used_id integer,
        image_url text,
        FOREIGN KEY(vaccine_id)
            REFERENCES vaccines (id)
    )""")

    con.commit()
    con.close()

def crear_tabla_vaccination_plan():
    con = sqlite3.connect('./db/db_unisalud.db')
    cursor = con.cursor()
    
    cursor.execute("""CREATE TABLE vaccination_plan (
        id integer NOT NULL PRIMARY KEY,
        max_age integer,
        min_age integer,
        start_date integer,
        end_date integer
    )""")

    con.commit()
    con.close()

def crear_tabla_afiliados():
    con = sqlite3.connect('./db/db_unisalud.db')
    cursor = con.cursor()

    cursor.execute("""CREATE TABLE affiliates (
        id integer NOT NULL,
        first_name text,
        last_name text,
        address text,
        phone integer,
        email text,
        city_id integer,
        birth_date integer,
        opt_in_date integer,
        opt_out_date integer,
        doses_taken integer,
        vaccination_plan_id integer,
        PRIMARY KEY(id),
        FOREIGN KEY(vaccination_plan_id) 
            REFERENCES vaccination_plan (id),
        FOREIGN KEY(city_id)
            REFERENCES cities (id)
    )""")

    con.commit()
    con.close()

def crear_tabla_vaccination_schedule():
    con = sqlite3.connect('./db/db_unisalud.db')
    cursor = con.cursor()
    
    cursor.execute("""CREATE TABLE vaccination_schedule (
        vaccination_plan_id integer NOT NULL,
        city_id integer NOT NULL,
        vaccine_lot_id integer NOT NULL,
        affiliate_id integer NOT NULL,
        PRIMARY KEY(vaccination_plan_id, affiliate_id),
        FOREIGN KEY(vaccination_plan_id)
            REFERENCES vaccination_plan (id),
        FOREIGN KEY(affiliate_id)
            REFERENCES affiliates (id),
        FOREIGN KEY(vaccine_lot_id)
            REFERENCES vaccine_lot (id),
        FOREIGN KEY(city_id)
            REFERENCES cities (id)
    )""")

    con.commit()
    con.close()

def crear_tablas():
    crear_tabla_cities()
    crear_tabla_vaccines()
    crear_tabla_vaccine_lot()
    crear_tabla_vaccination_plan()
    crear_tabla_afiliados()
    crear_tabla_vaccination_schedule()