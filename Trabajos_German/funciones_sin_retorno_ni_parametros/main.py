#esta función no tiene retorno explicito,
#sin embarcgo, las funciones asi no tenga
#retrum siempre devuelve none
#no siempre tiene que tener un retorno o parametro

gravedad = 9.8

def cambiar_gravedad():
    global gravedad
    gravedad = 7.2
    
cambiar_gravedad()
print(gravedad)