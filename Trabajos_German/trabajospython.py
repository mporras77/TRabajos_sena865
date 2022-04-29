#1---------------------------------------------------------------

"""
edad = int(input("ingrese su edad"))
edadFutura = int(input("ingrese numero"))
total = (edad + edadFutura)
print(total)

"""
#2----------------------------------------------------------------
"""
lado = int(input("ingrese diametros"))
total = lado **3
print(total)

"""
#3----------------------------------------------------------------
"""
producto = int(input("ingrese producto"))
total = producto + producto * 0.10
print (f"(prodcuto) - con 10% {total}")

"""
#4----------------------------------------------------------------

"""
producto = (input("ingrese producto"))
if producto == "arroz" or producto == "huevos":
    print("no hay iva")
    
elif producto == "carne" or producto == "salMarina":
    print("puede tener iva")
else:
    print ("no es valido")
    
"""
#5------------------------------------------------------------------

"""
print ("CALCULAR EL AREA DE UN TRIANGULO")
base=input("CUAL ES LA BASE: ")
altura=input("CUAL ES LA ALTURA: ")
area=int (base) * int (altura) / 2.0
print ("el resultado es: " + str (area))

"""

#6---------------------------------------------------------------

"""

import random
for x in range(10): 
    print (random.randint(0,100))
    
"""

#7-----------------------------------------------------------------

"""

import math
r=float(input("Ingrese el radio:"))
circumference=2*math.pi*r
area=math.pi*r*r
sarea=4*math.pi*r*r
volume=4/3*math.pi*r**3
print ( "Circunferencia:% .2f" % circumference)
print ( "Área del círculo:% .2f"% area)
print ( "Área de superficie de la bola:% .2f"% sarea)
print ( "Volumen de bola:% .2f" % volume)

"""

#8----------------------------------------------------------------

"""

n=int(input("Ingrese el valor final:"))
x=1
while x<=n:
    print(x)
    x=x+1 
    
"""

#9-----------------------------------------------------------------

"""

edad = int(input("Escribe tu edad: "))
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
    
"""

#10------------------------------------------------------------------




