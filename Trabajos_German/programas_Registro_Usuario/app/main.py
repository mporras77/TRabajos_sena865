def registro(correo, contrasena, nombres, telefono, ciudad, edad):
    pass


def login(correo, contrasena):
    pass

def bienvebida(correo):
    pass

def login_incorrecto():
    pass

import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db.db")

print("---------------------------------------------------------------------------")

correo = input("ingrese correo: ")

contrasena = input("ingrese contraseña: ")

nombres = input("ingrese nombre y aprllido: ")

telefono = input("ingrese telefono: ")

ciudad = input("ingrese ciudad: ")

edad = input("ingrese edad: ")

registro = (correo,contrasena, nombres, telefono, ciudad, edad)
print("registro exitoso")

print("---------------------------------------------------------------------------")

def login():
    correo = input("ingrese correo: ")
    contrasena = input("ingrese contraseña: ")
    print("hola usuario. ", correo)
print("hola: ", nombres)
login(registro, contrasena)
print("---------------------------------------------------------------------------")

bienvebida = (correo, contrasena)
print("hola usuario: ", nombres) 
print("---------------------------------------------------------------------------")
def login_incorrecto():
    login_incorrecto(correo, contrasena)
    for correo in contrasena:
       correo = input("ingrese correo: ")
       contrasena = input("ingrese contraseña: ")
       print("correo y contraseña correctos")
    else:
        print("correo o contraseña incorrectos")

        
