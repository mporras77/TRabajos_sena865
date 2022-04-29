
for i in range(100):
    print(i)
print("-------------------")

for i in range(20, 119):
    print(i)
print("-------------------")

for i in range(-30, 0):
    print(i)
print("-------------------")

for i in range(1, 51):
    print(4 * i)
print("-------------------")
nombre = "ADSI 865"
print(type(nombre))
print("-------------------")
numero = int(input("ingrese Nuemro"))
if numero /5:
    print(i)
print("-------------------")
lista = ["juan", "pedro", "maria"]
for nombre in lista:
    print("minombre es:", nombre)
print("-------------------")
ciudades = ["Toronto", "Cali", "Paris", "Pereira", "Buenos Aires"]
for ciudad in ciudades:
    if ciudad == "Cali" or ciudad == "Pereira":
        print(ciudad)
    else:
        print("no son colombianas:")
print("-------------------")
control = 0
while control < 10:
    print(control)
    control += 1 
print("------------------")
def imprimir_tabla(numero):
    
    LIMITE = 10
    
    contador = 1
    while contador <= LIMITE:
        resultado = contador * numero
        print("{} x {} = {}".format(numero, contador, resultado))
       
        contador = contador + 1


imprimir_tabla(5)
    
    
