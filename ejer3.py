import numpy as np
def  mueve_col(n,p) :
    print("Arreglo 10 x 10 con números del 0 al 99 (ver detalle de impresión")
    a = np.arange(100).reshape(10, 10)              
    x=a.remove(axis=0)
    d=a.index(axis=-1)
    lui=a[:,p]
    return lui