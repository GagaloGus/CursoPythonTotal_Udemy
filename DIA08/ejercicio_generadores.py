# ==== 1 ====
# generador infinito

def generador_infinito():
    x = 1
    while True:
        yield x
        x+=1
generador = generador_infinito()

# ==== 2 ====
# generador infinito de multiplos de 7

def generador_infinito_7():
    x = 7
    while True:
        yield x
        x+=7
generador = generador_infinito_7()

# ==== 3 ====
# Vidas
def generador_vidas():
    yield "Te quedan 3 vidas"
    yield "Te quedan 2 vidas"
    yield "Te queda 1 vida"
    yield "Game Over"
perder_vida = generador_vidas()