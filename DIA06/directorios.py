import os
from pathlib import Path

ruta = os.getcwd() # get current working directory

os.chdir(f'{os.getcwd()}\\dir') # cambia el directorio donde vamos a trabajar

archivo = open('prueba_dir.txt')
print(archivo.read())
archivo.close()
os.makedirs("otra", exist_ok=True)

print(os.path.basename(ruta+"\\prueba_2.txt")) # devuelve el nombre del archivo, sin su ruta
print(os.path.dirname(ruta+"\\prueba_2.txt")) # devuelve la ruta del directorio del archivo
print(os.path.split(ruta+"\\prueba_2.txt")) # devuelve una tupla con la ruta del directorio y el nombre del archivo

os.rmdir("otra")

# path

directorio = Path('C:/Users/6003802/OneDrive - ViewNext/Escritorio/CursilloPython/DIA06/dir')
archivo = directorio/'prueba_dir_2.txt'

print((open(archivo)).read())