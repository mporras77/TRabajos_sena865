#from login import * #aca se importan 
#todas las funciones, variables, clases etc del modulo
#import login #aca para acceder a la funcion login seria para
#login.login()
from login import login
from registro import registro

print("Por favor ingrese 1 para registrarse")
print("Por favor ingrese 2 para loguearse")

def bootstrap():
    menu_estado = input("Ingrese opción")
    if menu_estado == "1":
        registro()
    if menu_estado == "2":
        login()

bootstrap()





