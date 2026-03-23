# ARGS

def suma_cuadrados(*args):
    return sum(num ** 2 for num in args)

def suma_absolutos(*args):
    return sum(abs(num) for num in args)

def numeros_persona(nombre, *args):
    return f"{nombre}, la suma de tus números es {sum(args)}"

# KWARGS
# kwargs es como un diccionario !!
def suma(**kwargs):
    for clave, valor in kwargs.items():
        print(clave, valor)
    print(sum(kwargs.values()))
suma(x=3, y=5, z=6, w=10)

def cantidad_atributos(**kwargs):
    return len(kwargs)

def lista_atributos(**kwargs):
    return list(kwargs.values())

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}")
    for k, v in kwargs.items():
        print(f"{k}: {v}")