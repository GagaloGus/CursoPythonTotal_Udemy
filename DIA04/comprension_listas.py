palabra = "guayaba"

# FORMA EXTENDIDA 
lista = []
for letra in palabra:
    lista.append(letra)
print(lista)

# FORMA COMPACTA
lista = [letra for letra in palabra]
print(lista)

# Filtrado con if
lista = [n for n in range(0, 10) if n % 2 == 0]
print(lista)
lista = [n if n % 2 == 0 else 'impar' for n in range(0, 10)]
print(lista)

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(n-32)*(5/9) for n in temperatura_fahrenheit]
print(grados_celsius)