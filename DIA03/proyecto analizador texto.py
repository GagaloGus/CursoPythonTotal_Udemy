# usuario ingrese un texto y tres letras a su eleccion
# devuelve:
# cuantas veces aparece cada letra en el texto
# cuantas palabras hay en total
# primera y ultima letra
# texto con las palabras invertidas
# aparece la palabra 'python'

texto_usuario = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut varius sagittis ex, in semper risus tempus vitae. Aliquam interdum semper lectus, in auctor erat hendrerit ac. Integer vel gravida sem. Donec venenatis bibendum gravida. Aenean dictum congue sem sit amet cursus. In ut magna vel felis rutrum maximus. Nunc gravida" #input("Escribe un texto aca: ")
letras = input("Escribe tres letras separadas por espacios: ").lower()
letras = letras.split(" ")
texto_separado = texto_usuario.split(" ")

# 1
print(f"Letras repetidas en el texto: {letras[0]}: {texto_usuario.lower().count(letras[0])} | {letras[1]}: {texto_usuario.lower().count(letras[1])} | {letras[2]}: {texto_usuario.lower().count(letras[2])}")

# 2
print(f"Hay {len(texto_separado)} palabras en el texto")

# 3
print(f"La primera letra es '{texto_usuario[0]}'")
print(f"La ultima letra es '{texto_usuario[-1]}'")

# 4
texto_reverse = texto_separado
texto_reverse.reverse()
texto_reverse = " ".join(texto_reverse)
print(f"El texto con las palabras invertidas es: {texto_reverse}")

# 5
print(f"La palabra 'python' esta?: {"python" in texto_separado}")