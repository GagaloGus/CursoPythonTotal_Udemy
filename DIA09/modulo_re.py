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