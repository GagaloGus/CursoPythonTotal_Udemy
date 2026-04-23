# crear una maquina de turnos para una farmacia
# las secciones son perfumeria, farmacia y maquillaje

# pregunta al cliente a donde quiere dirijirse y le da un num de turno correspondiente
# tienen que tener una letra y guion segun la seccion
# debe de tener algun tipo de decoracion el ticket antes y despues del codigo
# separar por modulos

import os

def loop_principal():
    print("De que seccion desea pedir turno?:\n 1- Perfumeria\n 2- Farmacia\n 3- Maquillaje")
    seleccion = 0
    while True:
        sel_raw = input("-> ")
        try:
            sel_raw = int(sel_raw)
            if sel_raw not in [1, 2, 3]:
                raise Exception(f"'{sel_raw}' no es una opcion valida")
            seleccion = sel_raw
            break
        except ValueError:
            print(f"'{sel_raw}' no es un numero")
        except Exception as e:
            print(e)

    print(f"Opcion elegida: {seleccion}")

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