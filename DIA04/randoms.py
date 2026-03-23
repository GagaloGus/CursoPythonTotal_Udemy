from random import *

rnd = randint(1, 50)
print(rnd)
rnd = uniform(1, 10)
print(rnd)
rnd = random() # random float entre 0 y 1
print(rnd)

colores = ["azul", "rojo", "verde", "amarillo"]
rnd = choice(colores) #elige elemento aleatorio de la lista
print(rnd)

shuffle(colores)
print(colores)