# crear una maquina de turnos para una farmacia
# las secciones son perfumeria, farmacia y maquillaje

# pregunta al cliente a donde quiere dirijirse y le da un num de turno correspondiente
# tienen que tener una letra y guion segun la seccion
# debe de tener algun tipo de decoracion el ticket antes y despues del codigo
# separar por modulos

import os
from secciones import seccion_handler, decorador_texto_turno

secciones = ["Perfumeria", "Farmacia", "Maquillaje"]

def loop_principal():
    print("De que seccion desea pedir turno?:")
    for i, s in enumerate(secciones):
        print(f" {i+1}- {s}")

    seleccion = 0
    while True:
        sel_raw = input("-> ")
        try:
            sel_raw = int(sel_raw)
            if sel_raw - 1 not in list(range(len(secciones))):
                raise Exception(f"'{sel_raw}' no es una opcion valida")
            seleccion = sel_raw - 1
            turno = seccion_handler(seleccion)
            print(decorador_texto_turno(turno, seleccion, secciones))
            break
        except ValueError:
            print(f"'{sel_raw}' no es un numero")
        except Exception as e:
            print(e)

    print(f"Opcion elegida: {secciones[seleccion]}")

def main():
    os.system("cls")
    while True:
        print("====== BIENVENIDO A LA FARMACIA ======")
        loop_principal()
        print("Gracias por usar esta maquina, le gustaria pedir otro turno? [s/n]: ", end="")
        otro_num = input().lower() == 's'
        if not otro_num:
            break

    print("===== FIN DEL PROGRAMA =====")

if __name__ == "__main__":
    main()