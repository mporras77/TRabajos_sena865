import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db.db")



def insert():
    #se conecta a la base de datos
    con_bd = sqlite3.connect('db.db')
    #cursor a la db
    cursor_db = con_bd.cursor()
    #consultas
    sql = "INSERT INTO users(usuario, record) VALUES(?, ?)"
    cursor_db.execute(sql, ("Ricardo", 10000))
    con_bd.commit()
    #cierre del cursor
    cursor_db.close()


def select():
    #se conecta a la base de datos
    con_bd = sqlite3.connect('db.db')
    #cursor a la db
    cursor_db = con_bd.cursor()
    #consultas
    sql = "SELECT record FROM  users WHERE usuario=?"
    cursor_db.execute(sql, ("Ricardo",))
    fila = cursor_db.fetchone()
    #print(fila)
    if len(fila) > 0:
        print(fila[0])
        return
    print("El usuario no existe")
    
#insert()
select()

