# Leer
mi_archivo = open('prueba.txt') # solo lectura
for linea in mi_archivo:
    print(f"linea -> {linea}")
mi_archivo.close()

# Escribir
registro_ultima_sesion = ["Federico\t", "20/12/2021\t", "08:17:32 hs\t", "Sin errores de carga"]

archivo = open('prueba_2.txt', 'w')
archivo.writelines(registro_ultima_sesion)
archivo.close()
archivo = open('prueba_2.txt', 'r')
print(archivo.read())
archivo.close()

# 'r' -> lectura solo / 'w' -> sobrescritura del archivo / 'a' -> añadir texto al archivo

def abrir_leer(ruta_archivo):
    archivo = open(ruta_archivo)
    return archivo.read()

def sobrescribir(ruta_archivo):
    archivo = open(ruta_archivo, "w")
    archivo.write("contenido eliminado")

    archivo.close()

def registro_error(ruta_archivo):
    with open(ruta_archivo, 'a') as a:
        a.write("se ha registrado un error de ejecución")
        a.close()
