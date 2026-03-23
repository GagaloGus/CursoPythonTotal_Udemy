diccionario = {"clave1":"valor1", "clave2":"valor2"}
print(diccionario)

cliente = {
    "nombre":"Guba",
    "apellido":"Uba",
    "peso":70,
    "talla":1.78
}

print(cliente)
cliente["nacionalidad"] = "Mamaguevo"
print(cliente)

tupla = (1,2,"asa", ["el1", "el2"], 1, 1)
print(tupla.count(1))
print(tupla.index("asa"))
print(tupla)
print(list(tupla))

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
print(sorteo)
sorteo.pop()
print(sorteo)
sorteo.add("Damián")
print(sorteo)