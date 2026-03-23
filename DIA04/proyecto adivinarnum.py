# 8 intentos para adivinar un numero entre el 1 al 100
#si se pasa, se indica
# si es menor o mayor, se dice que es incorrecto y se indica si esta por arriba o por abajo
# al ganar, se muestra tambien el numero de intentos

from random import *

rango_num = {'min': 0, 'max':100}
intentos_max = 8
intentos = 0
numero_aleatorio = randint(rango_num['min'], rango_num['max'])

print(f"He pensado en un numero entre el {rango_num['min']} y el {rango_num['max']}!!")
while intentos_max > intentos:
    print(f"Te quedan {intentos_max - intentos} intentos")
    numero_elegido = int(input(f"Elige un numero: ").strip())
    intentos+=1

    if(numero_elegido < rango_num['min'] or rango_num['max'] < numero_elegido):
        print(f"El numero {numero_elegido} se sale del rango !!")
    elif(numero_elegido < numero_aleatorio):
        print(f"El numero elegido esta por encima")
    elif(numero_elegido > numero_aleatorio):
        print(f"El numero elegido esta por debajo")
    else:
        print(f"Has ganado !!! Necesitaste {intentos} intentos")
        break
    print("")

if(numero_aleatorio != numero_elegido):
    print(f"No pudiste adivinarlo.. el numero secreto era {numero_aleatorio}")


