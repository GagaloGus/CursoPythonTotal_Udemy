import zipfile, time, os, shutil

carpeta_origen = "DIA09/comprimir/textos"

mi_zip = zipfile.ZipFile(f"{carpeta_origen}/archivo_comprimido.zip", "w")
mi_zip.write(f"{carpeta_origen}/textoA.txt")
mi_zip.write(f"{carpeta_origen}/textoB.txt")
mi_zip.write(f"{carpeta_origen}/textoC.txt")
mi_zip.close()
print("ZIP")

# shutil.make_archive(f"{carpeta_origen}/todo_comprimido", "zip", carpeta_origen) # Otra forma de comprimir una carpeta entera
time.sleep(1)

os.unlink(f"{carpeta_origen}/textoA.txt")
os.unlink(f"{carpeta_origen}/textoB.txt")
os.unlink(f"{carpeta_origen}/textoC.txt")
print("BORRAR")

time.sleep(1)

zip_abierto = zipfile.ZipFile(f"{carpeta_origen}/archivo_comprimido.zip", "r")
zip_abierto.extractall()
zip_abierto.close()
print("DESCOMPRIMIR")

# shutil.unpack_archive(f"{carpeta_origen}/todo_comprimido.zip", carpeta_origen, "zip")

time.sleep(1)

os.unlink(f"{carpeta_origen}/archivo_comprimido.zip")
print("BORRAR ZIP")