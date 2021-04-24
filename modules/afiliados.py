import sqlite3

# def agregar_ciudades(list):
    # con = sqlite3.connect('./db/db_unisalud.db')
    # cursor = con.cursor()
    
    # cursor.executemany("INSERT INTO cities VALUES (?, ?)",(list))
    
    # con.commit()
    # con.close()
# ciudades = [
    # (None, 'Bogota'),
    # (None, 'Manizales'),
    # (None, 'Medellin'),
    # (None, 'Palmira')
# ]
# agregar.agregar_ciudades(ciudades)
def agregar(id,first_name,last_name,address,phone,email,city_id,birth_date,opt_in_date,opt_out_date,doses_taken,vaccination_plan_id):
    con = sqlite3.connect('./db/db_unisalud.db')
    cursor = con.cursor()
    
    cursor.execute("INSERT INTO affiliates VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
        (
            id,
            first_name,
            last_name,
            address,
            phone,
            email,
            city_id,
            birth_date,
            opt_in_date,
            opt_out_date,
            doses_taken,
            vaccination_plan_id
        )
    )
    
    con.commit()
    con.close()

def buscar(id):
    con = sqlite3.connect('./db/db_unisalud.db')
    cursor = con.cursor()

    cursor.execute("SELECT * from affiliates WHERE id = (?)",(id,))
    items = cursor.fetchall()
    for item in items:
        print(item)
    
    con.commit()
    con.close()

def desafiliar(id, date):
    con = sqlite3.connect('./db/db_unisalud.db')
    cursor = con.cursor()

    cursor.execute("UPDATE affiliates SET opt_out_date = (?), opt_in_date = NULL WHERE id = (?)",(date,id,))
    items = cursor.fetchall()
    
    con.commit()
    con.close()

def afiliar(id, date):
    con = sqlite3.connect('./db/db_unisalud.db')
    cursor = con.cursor()

    cursor.execute("UPDATE affiliates SET opt_in_date = (?), opt_out_date = NULL WHERE id = (?)",(date,id,))
    items = cursor.fetchall()
    
    con.commit()
    con.close()
