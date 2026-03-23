from random import *

def todos_positivos(lista_num):
    for n in lista_num:
        if n < 0:
            return False
    return True

lista_numeros = [5, 6, 10, 0, -1]

def suma_menores(lista_num):
    suma = 0
    for n in lista_num:
        if n in range(0, 1001):
            suma+=n
    return suma

lista_numeros = [400, 13400, 2, 98, -500, 999]

def cantidad_pares(lista_num):
    cantidad = 0
    # otra forma usando sum, añade 1 por cada numero que sea par
    # return sum(1 for n in lista_numeros if n % 2 == 0)
    for n in lista_num:
        if n % 2 == 0:
            cantidad += 1
    return cantidad

lista_numeros = [400, 53, 13400, 98, -500, 999]

def lanzar_dados():
    return (randint(1,6), randint(1,6))

def evaluar_jugada(dado_1, dado_2):
    suma_dados = dado_1+dado_2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados in range(6, 10):
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
    
d1, d2 = lanzar_dados()
print(evaluar_jugada(d1, d2))

print("")

def reducir_lista(lista_num):
    nueva_lista = list(set(lista_num)) # elimina duplicados
    nueva_lista.remove(max(nueva_lista)) # elimina el mayor
    return nueva_lista

def promedio(lista_num):
    return sum(lista_num)/len(lista_num) # calcula la media

lista_numeros = [1, 4, 19, 1, 9, 4, 20, 5]
print(lista_numeros, reducir_lista(lista_numeros), promedio(lista_numeros))

print("")

def lanzar_moneda():
    return "Cara" if random() < 0.5 else "Cruz"

def probar_suerte(res_moneda, lista_num):
    if res_moneda == "Cara":
        print("La lista se autodestruirá")
        lista_num = []
    else:
        print("La lista fue salvada")
    return lista_num

print(probar_suerte(lanzar_moneda(), lista_numeros))