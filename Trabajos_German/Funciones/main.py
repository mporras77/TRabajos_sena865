
#funciones usamos la palabra reserva def
#Aca num es un parametro, no es un argumento
def cuadro(num):
    return num*num
#las funciones no se llaman solas, hay q llamarlas
#medianye su identificador, es decir su nombre
#aca los valores que se pasan a la función e¿se llama "ARGUMENTO"
valor1 = cuadro(12)
valor2 = cuadro(2)
print("cuadrado de 12: ", valor1)
print("cuadrado de 2: ", valor2)

#función que toma un numero y devuelve absoluto
def valor_absoluto(a):
    if a >= 0:
        return a
    else:
        return a*-1
    
valor3 = valor_absoluto(-15)
print("el asb de -15 es: ", valor3)
valor4 = valor_absoluto(7)
print("el asb de -15 es: ", valor4)
valor5 = valor_absoluto(0)
print("el asb de -15 es: ", valor5)
print("----------------------------------------------------------")
valor_con_libreria = asb(-15)
print("el abs de -15 con libreria es: ", valor_con_libreria)