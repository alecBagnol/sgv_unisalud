import sqlite3

def agregar_ciudades(list):
    con = sqlite3.connect('./db/db_unisalud.db')
    cursor = con.cursor()
    
    cursor.executemany("INSERT INTO cities VALUES (?, ?)",(list))
    
    con.commit()
    con.close()

def agregar_afiliado(id,first_name,last_name,address,phone,email,city_id,birth_date,opt_in_date,opt_out_date,doses_taken,vaccination_plan_id):
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

