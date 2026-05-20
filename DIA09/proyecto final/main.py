import shutil, time, os, re, datetime
from pathlib import Path

RUTA_DIR = "DIA09/proyecto final/Mi_Gran_Directorio"
PATRON_N_SERIE = r"N[a-zA-Z]{3}-\d{5}"

def imprimir_resultado(dict_n_serie : dict, tiempo: float):
    valores_aplanados = [elemento for sublista in dict_n_serie.values() for elemento in sublista]

    string_n_serie = ""
    for archivo, lista_n_serie in dict_n_serie.items():
        string_n_serie += f"{archivo:15s} {" / ".join(lista_n_serie)}\n"

    print(f"""
----------------------------------------------------
Fecha de búsqueda: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}

ARCHIVO		NRO. SERIE
-------		----------
{string_n_serie}
Números encontrados: {len(valores_aplanados)}
Duración de la búsqueda: {tiempo:.5f} segundos
----------------------------------------------------
""")


def buscar_numeros_serie() -> dict[str, list[str]]:
    numeros_encontrados = {}

    for carpeta, subcarpetas, archivos in os.walk(RUTA_DIR):
        for archivo in archivos:
            patrones = re.findall(PATRON_N_SERIE, Path(carpeta, archivo).read_text())
            if len(patrones) > 0:
                numeros_encontrados[archivo] = patrones

    return numeros_encontrados

def main():
    tiempo_inicio = time.perf_counter()
    n_serie = buscar_numeros_serie()
    tiempo_fin = time.perf_counter()
    imprimir_resultado(n_serie, tiempo_fin - tiempo_inicio)

if __name__ == "__main__":
    main()