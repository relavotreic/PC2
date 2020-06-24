# Crear una función para rellenar un arreglo tipo lista 2-D en el que se solicite el número de filas y
# columnas, se rellena el arreglo con número aleatorios.
# NOTA: No utilizar Numpy para esta pregunta
#  Nombre de función: crea_arreglo
#  Entradas: 2
# o filas
# o columnas
#  Salida:
# o Arreglo con números aleatorios
from random import randint as ri
def crea_arreglo(f,c):
    lista=[]
    # no se especifica si desea que ingrese  algun dato en el ejercicio
    for i in range (f):
        a=[0]*c
        lista.append(a)
        for j in range(c):
            lista[i][j]=ri(100,900)
    return lista