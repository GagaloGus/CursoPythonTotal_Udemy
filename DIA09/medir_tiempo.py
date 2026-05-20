import time, timeit

# time es para pruebas de funciones que duren segundos o mas, timeit es mejor para funciones pequeñas

def prueba_for(numero):
    lista = []
    for num in range(1, numero+1):
        lista.append(num)
    return list


def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador+=1
    return lista

def prueba_generar(numero):
    return list(range(1, numero+1))


duracion_for = timeit.timeit(lambda: prueba_for(100), number=50000)
duracion_while = timeit.timeit(lambda: prueba_while(100), number=50000)
duracion_generar = timeit.timeit(lambda: prueba_generar(100), number=50000)

print(duracion_for)
print(duracion_while)
print(duracion_generar)