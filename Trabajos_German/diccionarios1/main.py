#UN DICCIONARIO ES UNA ESTRUCTURA DE DATOS
#LA CUAL USA PARES LLAVE-VALOR, NO USA ORDEN
#LAS LLAVES DEBEN SER OBJETOS INMUTABLES P.E.
#ENTEROS, CADENAS ETC P.E. NO LISTAS
#una forma de crear el diccionario con datos(puede estar 
#vacia inicialmente)
diccionario1 = { "arroz": 2100, "leche": 4000, "lentejas": 2500 }
#lectura
print("Precio arroz: ", diccionario1["arroz"])
print("Precio lentejas: ", diccionario1["lentejas"])
#escritura - cambiamos el valor de la llave leche
diccionario1["leche"] = 3000
print("Precio nuevo de la leche ", diccionario1["leche"])
#podemos crear nuevos pares llave-valor
diccionario1["panela"] = 4000
print("Precio panela ", diccionario1["panela"])
#podemos ver toda la estructura
print(diccionario1)

