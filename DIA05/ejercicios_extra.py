#Ej 1
def devolver_distintos(num_1, num_2, num_3):
    numeros = [num_1, num_2, num_3]
    suma = sum(numeros)

    if(suma > 15):
        return max(numeros)
    elif(suma < 10):
        return min(numeros)
    else:
        numeros.remove(max(numeros))
        numeros.remove(min(numeros))
        return numeros[0]

#Ej 2
def descomponer_palabra(palabra:str):
    lista_letras = list(set(palabra.lower()))
    lista_letras.sort()
    return lista_letras

#Ej 3
def comprobar_doble_cero(*args):
    primer_cero = False
    for arg in args:
        if arg == 0:
            if not primer_cero:
                primer_cero = True
            else:
                return True
        else:
            primer_cero = False
    return False

#Ej 4
def contar_primos(numero):
    if numero < 2:
        return 0, []

    lista_primos = [2]
    for posible_primo in range(3, numero+1):
        es_primo = True
        #Itera por todos los numeros hasta llegar al posible primo - 1
        for n in range(2, posible_primo, 2):
            if posible_primo % n == 0: # Division da resto 0 = Es divisible (no es primo)
                es_primo = False
                break
        if es_primo:
            lista_primos.append(posible_primo)

    return len(lista_primos), lista_primos
    
def contar_primos_2(numero):
    primos = [2]
    iteracion = 3
    if numero < 2:
        return 0
    while iteracion <= numero:
        for n in range(3, iteracion, 2):
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion+=2
    return len(primos), primos


print(contar_primos(20))