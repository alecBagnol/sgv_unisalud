import sqlite3

# def crear_tabla_vaccinated_status():
#     con = sqlite3.connect('./db/db_unisalud.db')
#     cursor = con.cursor()
#     cursor.execute("""CREATE TABLE VaccinatedStatus (
#         UserId DATATYPE integer NOT NULL PRIMARY KEY,
#         FirstName DATATYPE text,
#         LastName DATATYPE text,
#         Address DATATYPE text,
#         PhoneNum DATATYPE integer,
#         Email DATATYPE text,
#         City DATATYPE text,
#         BirthDate DATATYPE integer,
#         AffilitionDate DATATYPE integer,
#         DisaffiliationDate DATATYPE integer,
#         VaccinatedStatus DATATYPE text,
#     )""")

def crear_tabla_afiliados():
    con = sqlite3.connect('./db/db_unisalud.db')
    cursor = con.cursor()

    cursor.execute("""CREATE TABLE afiliados (
        UserId DATATYPE integer NOT NULL PRIMARY KEY,
        FirstName DATATYPE text,
        LastName DATATYPE text,
        Address DATATYPE text,
        PhoneNum DATATYPE integer,
        Email DATATYPE text,
        City DATATYPE text,
        BirthDate DATATYPE integer,
        AffilitionDate DATATYPE integer,
        DisaffiliationDate DATATYPE integer,
        VaccinatedStatus DATATYPE text,
    )""")

    con.commit()
    con.close()