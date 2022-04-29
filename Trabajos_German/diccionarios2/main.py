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
#existen dos formas de acceder a un valor en un diccionario
#con corchetes o con .get
#con corchetes
print("----------------------")
print(diccionario1["leche"])
#con .get
print(diccionario1.get("leche"))
#dorrado o eliminacion usamos .pop pasando la llave
#aca eliminamos la llave leche con su valor
diccionario1.pop("leche")
#verificamos si leche ha sido eliminada
print(diccionario1)

