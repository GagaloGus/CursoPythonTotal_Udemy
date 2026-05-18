import re

texto = "Si necesitas ayuda llama al 658-598-9977 las 24 horas al servicio de ayuda online"

busqueda = re.search("nada", texto)
print(busqueda) # -> None (no hay coincidencias en el texto)

busqueda = re.search("ayuda", texto)
print(busqueda.span()) # (13, 18) -> (devuelve entre que caracteres se encuentra por primera vez el patron)

busqueda = re.findall("ayuda", texto)
print(busqueda) # ["ayuda","ayuda"] -> (veces que se encontro el patron)

for match in re.finditer("ayuda", texto):
    print(match.span()) # Devuelve todas las tuplas de donde empieza y acaban cada uno de los patrones encontrados

patron = r"\d{3}-\d{3}-\d{4}" # -> patron del estilo 000-000-0000
busqueda = re.search(patron, texto)
print(busqueda.group()) # 658-598-9977 -> (devuelve lo que hizo match)


patron = r"(\d{3})-(\d{3})-(\d{4})" # -> patron del estilo 000-000-0000
busqueda = re.search(patron, texto)
print(busqueda.group(1)) # 658 -> (devuelve el primer grupo del patron)

passwd = input("Introduce tu contraseña: ")
patron = r"\D{1}\w{7}" # un primer caracter que no sea numero, luego 7 caracteres alfanumericos
print(re.search(passwd,patron)) # None (si no hay nada) / No none (si lo encuentra)

texto = "No se atienden los lunes"
print(re.search("lunes|martes", texto)) # | es como un 'and'
print(re.search(r"...tien...", texto)) # cada . es un caracter mas que devuelve antes o despues
print(re.search(r"^\D", texto)) # ^ verifica si es el inicio del string
print(re.search(r"\D$", texto)) # ^ verifica si es el final del string
print(re.search(r"[^\s]+", texto)) # Busca todos los caracteres que no sean un espacio vacio, el + las agrupa por palabras en lista

# regex complejo, filtro de correo electronico basico
patron_correo = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+$"
# 1- ^ (El email debe comenzar en el inicio del string)
# 2- [a-zA-Z0-9._%+-] (caracter permitido -> [] // acepta letras minusculas, mayusculas, numeros y los caracteres)
# 3- + (Acepta uno o mas (juan / abc123))
# 4- @ (Pide que tenga una @)
# 5- [a-zA-Z0-9.-] (caracter permitido -> [] // acepta letras minusculas, mayusculas, numeros y los caracteres)
# 6- + (Acepta uno o mas (gmail / empresa-x))
# 7- (\.[a-zA-Z]{2,}) (Conjunto de un punto + letras minus y/o mayus que sean minimo 2 caracteres)
# 8- + (Acepta uno o mas (.com / .es / .co.uk))
# 9- $ (El string termina aqui)
