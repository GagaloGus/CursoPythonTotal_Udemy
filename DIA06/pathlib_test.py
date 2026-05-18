from pathlib import Path, PureWindowsPath
import os

archivo = Path("DIA06/prueba.txt")
print(archivo.read_text()) # lee todo el texto sin tener que abrir ni cerrar
archivo.name # devuelve el nombre del archivo: 'prueba.txt'
archivo.suffix #devuelve la extension del archivo: '.txt'
archivo.stem #devuelve solo el nombre del archivo: 'prueba'

if not archivo.exists():
    'No existe'
else:
    'Existe'

ruta_windows = PureWindowsPath(archivo) # Convierte a ruta pura de windows

guia = Path(Path().home(),"España", 'Barcelona', "Sagrada_Familia.bat") # Se pueden convertir varios nombres a un path
guia.with_name("Marraquets.txt") # Reemplaza el archivo por otro del mismo directorio
guia.parent.parent.parent # permite ir al directorio padre del path
guia.relative_to(Path(Path().home(), "España")) # devuelve la ruta desde la ultima carpeta especificada -> Barcelona\Sagrada_Familia.bat

# iterar por el directorio EUROPA
guia = Path(os.getcwd(), "Europa")
for txt in guia.glob('**/*.txt'): #Glob recorre todos los archivos con esa terminacion
    print(txt)

# guia.glob('*.txt') -> Archivos en la carpeta guia que sean .txt
# guia.glob('**/*.txt') -> Archivos en la carpeta Y SUBCARPETAS de guia que sean .txt
