import shutil, timeit, os, re, datetime
from pathlib import Path

RUTA_DIR = "DIA09/proyecto final/Mi_Gran_Directorio"
PATRON_N_SERIE = r"N[a-zA-Z]{3}-\d{5}"

def imprimir_resultado():
    fecha_hoy = datetime.datetime.now()
    print(f"""
----------------------------------------------------
Fecha de búsqueda: {fecha_hoy.day}/{fecha_hoy.month}/{fecha_hoy.year}

ARCHIVO		NRO. SERIE
-------		----------
texto1.txt	Nter-15496
texto25.txt	Ngba-85235

Números encontrados: 2
Duración de la búsqueda: 1 segundos
----------------------------------------------------

""")


def main():
    numeros_encontrados = {}

    for carpeta, subcarpetas, archivos in os.walk(RUTA_DIR):

        print(f"Carpeta-> {carpeta}")
        print(f"Los archivos son:")
        for archivo in archivos:
            print(f"\t{archivo}")
            archivo_abrir = Path(carpeta, archivo)
            patrones = re.findall(PATRON_N_SERIE,archivo_abrir.read_text())
            if len(patrones) > 0:
                numeros_encontrados[archivo] = patrones

    print(numeros_encontrados)

if __name__ == "__main__":
    #main()
    imprimir_resultado()