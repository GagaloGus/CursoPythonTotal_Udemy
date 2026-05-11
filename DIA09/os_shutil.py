import os, shutil
import send2trash

ruta_dir = os.getcwd()
print(ruta_dir) #ruta del directorio donde se esta ejecutando este archivo
print(os.listdir()) #lista los archivos y carpetas en el directorio

shutil.move("DIA09/curso.txt", rf"{ruta_dir}/DIA09/dir") #mueve el archivo otro directorio
shutil.move("DIA09/dir/curso.txt", rf"{ruta_dir}/DIA09")

# os.unlink() # borra un archivo
# shutil.rmtree() # borra un directorio permanentemente
# send2trash.send2trash() # borra un directorio y lo manda a la papelera

#os.walk es un generador que recorre todo el arbol de archivos y carpetas
print(os.walk(ruta_dir))

for carpeta, subcarpetas, archivos in os.walk(ruta_dir):
    print(f"Carpeta-> {carpeta}")
    print(f"Las sub carpetas son:")
    for sub in subcarpetas:
        print(f"\t{sub}")
    print(f"Los archivos son:")
    for archivo in archivos:
        print(f"\t{archivo}")

    print("\n")
