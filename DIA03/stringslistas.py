texto = "Hola jeff"
print(texto.upper())
print(texto.lower())
print(texto.title())

lista = ["El", "Huevo", "Mio"]
print("-".join(lista))



frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
frase_nueva = frase.replace("difícil", "fácil").replace("mala", "buena")
print(frase_nueva)

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)
print(frutas)