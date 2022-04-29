"""
Dado el arreglo [ [1, 3, 4], [6, 7, 9] ], 
recorra cada uno de sus elementos e imprimalos.
Usamos for anidados
"""
#para acceder a los elementos más internos
#requerimos de 2 indices, por tanto necesitamos
#dos ciclos for para hacer el recorrido
arreglo = [ [ [3, 5] ],  [ [56, 90] ]
for arreglo_interno in range(len(arreglo)):
   for indice in range(len(arreglo[arreglo_interno])):
       print(arreglo[arreglo_interno][indice])

