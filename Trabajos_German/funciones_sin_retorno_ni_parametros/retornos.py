#función con diferentes opciones de retorno
#fumción que retorne el conciente entre 2
#numeros naurales. no trsbajara con divisor 0
#ni con 0, ni con numeros negativos
#aca el primier parametro siempre sera el dividendo
#y el otro sera el divisor.
#el orden de los parametros importan a la hora de
#llamar la función
def conciente(dividendo, divisor):
    #evaluamos si alguno de los parametros es
    #menor que 1. 0 sea que sea natural
    #guarda
    if dividendo <1 or divisor <1:
        #el retorno marca el fin de la función
        #despues del retorno no se ejecuta ninguna
        return "El dividendo deber ser un natural"

    return dividendo / divisor

div = int(input("ingrese divisor"))
divid = int(input("ingrese dividiendo"))
valor = conciente(divid, div)
print(valor)