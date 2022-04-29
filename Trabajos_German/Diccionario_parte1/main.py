diccionario1 = {"arroz": 2100, "leche": 4000, "lentejas": 2500}
print("precio arroz: ", diccionario1 ["arroz"])
print("precio lentejas: ", diccionario1 ["lentejas"])

diccionario1["leche"] = 3000
print("precio nuevo de la leche: ", diccionario1 ["leche"])

diccionario1 ["panela"] = 4000
print("precio panela: ", diccionario1 ["panela"])

print(diccionario1)

print("----------------------------------------------------------------")

print(diccionario1["leche"])

print(diccionario1.get("leche"))

diccionario1.pop("leche")

print(diccionario1)