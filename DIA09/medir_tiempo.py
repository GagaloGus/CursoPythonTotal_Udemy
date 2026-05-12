import time, timeit

# time es para pruebas de funciones que duren segundos o mas, timeit es mejor para funciones pequeñas

declaracion_for = """
prueba_for(100)
"""
setup_for = """
def prueba_for(numero):
    lista = []
    for num in range(1, numero+1):
        lista.append(num)
    return list
"""

declaracion_while = """
prueba_while(100)
"""
setup_while = """
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador+=1
    return lista
"""

declaracion_generar = """
prueba_generar(100)
"""
setup_generar = """
def prueba_generar(numero):
    return list(range(1, numero+1))
"""

duracion_for = timeit.timeit(declaracion_for, setup_for, number=50000)
duracion_while = timeit.timeit(declaracion_while, setup_while, number=50000)
duracion_generar = timeit.timeit(declaracion_generar, setup_generar, number=50000)

print(duracion_for)
print(duracion_while)
print(duracion_generar)