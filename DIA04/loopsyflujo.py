numero = 10
while numero >= 0:
    print(numero, end=" ")
    numero-=1

print("")
numero = 50
while numero >= 0:
    if(numero % 5 == 0):
        print(numero, end=" ")
    numero-= 1

print("")
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for n in lista_numeros:
    print(n, end=" ")
    if(n < 0):
        break

print("")
# lista del 2500 hasta el 2585
mi_lista = list(range(2500, 2586))

mi_lista = list(range(3, 301))

suma_cuadrados = 0
for num in range(1, 16):
    suma_cuadrados+= num**2

mis_tuples = list(enumerate(['a', 'b', 'c', 'd']))
print(mis_tuples)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for i, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {i}')

lista_indices = list(enumerate("Python"))
print(lista_indices)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for i, nombre in enumerate(lista_nombres):
    if(nombre[0].lower() == 'm'):
        print(i, end=" ")
print("")

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
zip_paises = list(zip(paises, capitales))
print(zip_paises)

numeros_es = ["uno", "dos", "tres", "cuatro", "cinco"]
numeros_en = ["one", "two", "three", "four", "five"]
numeros_fr = ["um", "dois", "três", "quatro", "cinco"]

zip_numeros = list(zip(numeros_es, numeros_en, numeros_fr))
print(zip_numeros)

lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
print(f"El valor maximo es {max(lista_numeros)} y el minimo es {min(lista_numeros)}")

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
rango = max(lista_numeros)-min(lista_numeros)
print(rango)

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())
print(edad_minima, ultimo_nombre)