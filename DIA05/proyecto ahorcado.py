# piensa en una palabra secreta, se la muestra al usuario con guiones
# si acierta, se cambian los guiones necesarios por la letra, si no pierde vida (maximo 6 vidas)

from random import *  # type: ignore

palabras_aleatorias = ["guayaba", "chihuahua", "silksong", "cacahuete", "enrique", "pitocaca", "elefante", "segismundo", "mamabicho"]
max_vidas = 6

def pedir_letra(letras_elegidas:list)->str:
    while True:
        letra_elegida = str(input("Elige una letra: ")).lower()
        
        if len(letra_elegida) != 1:
            print("Escribe solo una letra")
            continue

        if not letra_elegida.isalpha():
            print("Eso no es una letra!")
            continue

        if letra_elegida in letras_elegidas:
            print(f"La letra '{letra_elegida}' ya la dijiste")
            continue
        
        return letra_elegida



def mostrar_guiones(palabra:str, letras_elegidas:list)->str:
    res = "".join([letra if letra in letras_elegidas else "_" for letra in palabra])
    return f"{res} ({", ".join([letra for letra in letras_elegidas if letra not in palabra])})"


def validar_victoria(palabra:str, letras_elegidas:list)-> bool:
    # Si falta alguna letra en las letras elegidas, es que no las ha adivinado todas
    for l in list(set(palabra)):
        if l not in letras_elegidas:
            return False
    return True

def juego():
    print("-- Bienvenido al juego del ahorcado! --\n")
    palabra_secreta = choice(palabras_aleatorias).lower()
    vidas = max_vidas
    letras_elegidas = []
    while True:
        print(f"{mostrar_guiones(palabra_secreta, letras_elegidas)} // Vidas restantes: {vidas}\n")
        letra_elegida = pedir_letra(letras_elegidas)
        letras_elegidas.append(letra_elegida)

        correcto = letra_elegida in palabra_secreta
        if correcto:
            print(f"Acierto -> {letra_elegida}")
        else:
            print(f"Incorrecto -> {letra_elegida}")
            vidas-=1

        if validar_victoria(palabra_secreta, letras_elegidas):
            print(f"Has ganado!!!! La palabra era '{palabra_secreta}'")
            break

        if vidas <= 0:
            print(f"Te quedaste sin vidas... La palabra era '{palabra_secreta}'")
            break

        print("\n-----------------------------------\n")
juego()