def mi_funcion():
    return 4
def mi_generador():
    yield 4

g = mi_generador()
# print(next(g))
# print(next(g)) # Error porque no hay mas elementos

def lista_funcion():
    lista= []
    for i in range(1,5):
        lista.append(i*10)
    return lista

def lista_generador():
    for i in range(1,5):
        yield i *10

print(lista_funcion())
print(lista_generador())

g = lista_generador()
print(next(g))
print(next(g))

def proceso_generador():
    x = 1
    yield x
    x+= 1
    yield x
    x+= 1
    yield x

g = proceso_generador()
print(next(g))
print(next(g))
print(next(g))