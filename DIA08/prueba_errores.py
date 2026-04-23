"""Este programa sirve para probar errores"""

from modulos.paquetote import suma_y_resta

def try_catch():
    """Prueba try catch"""
    try:
        # codigo a probar
        n1 = input("Dime el numero 1: ")
        n2 = input("Dime el numero 2: ")
        print("Sumando "+n1+" "+n2)
        print(suma_y_resta.suma(int(n1), int(n2)))

    except TypeError:
        # codigo que se ejecuta si hay errores
        print("Estas intentando concatenar tipos distinos")
    except ValueError:
        # codigo que se ejecuta si hay errores
        print("Los valores no se pudieron sumar")
    else:
        # codigo que se ejecuta si no hay errores
        print("Todo funciono correctamente")
        pass
    finally:
        # codigo que siempre se ejecuta
        print("Gracias por usar la app!")


# PARA VERIFICAR SI ESTE ARCHIVO TIENE ERRORES, USAMOS <PYLINT>
# en la terminal: pylint <nombre archivo> -r (reporte) y (yes)