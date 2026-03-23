texto = "Esta es una prueba"
print(texto[3])
print(texto[-3])

res = texto.index("u", 6, 11)
res_reverse = texto.rindex("u")
print(res)
print(res_reverse)

res = texto.find("x") #En vez de dar error, da -1