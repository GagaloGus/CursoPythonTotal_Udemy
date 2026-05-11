def cambiar_letras(tipo:str):
    def mayus(texto:str):
        print(texto.upper())

    def minus(texto:str):
        print(texto.upper())

    if tipo == "may":
        return mayus
    elif tipo == "min":
        return minus

operacion = cambiar_letras("may")
operacion("Palabra")

def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print("Alo")
        funcion(palabra)
        print("Chau")

    return otra_funcion

# DECLARAR EL DECORADOR, no es recomendado
@decorar_saludo
def mayusculas_dec(texto:str):
    print(texto.upper())


def mayusculas(texto:str):
    print(texto.upper())

def minusculas(texto:str):
    print(texto.lower())

# MEJOR ASI
mayusculas_decoradas = decorar_saludo(mayusculas)
minusculas_decoradas = decorar_saludo(minusculas)

mayusculas("Python")
mayusculas_dec("Python")