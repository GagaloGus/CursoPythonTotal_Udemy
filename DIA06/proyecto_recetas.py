from pathlib import Path
import os, shutil



def crear_estructura():
    dir_recetas = Path(os.getcwd(), 'Recetas')
    estructura ={
        'Carnes': ['Entrecot.txt', 'Pizza_carne.txt'], 
        'Ensaladas': ['Ensalada_griega.txt', 'Ensalada_mediterranea.txt'], 
        'Pastas': ['Canelones.txt', 'Macarrones.txt'], 
        'Postres': ['Tiramisu.txt', 'Tarta_3_chocolates.txt']
    }

    for key, value in estructura.items():
        os.makedirs(Path(dir_recetas, key), exist_ok=True)
        for archivo in value:
            path_archivo = Path(dir_recetas, key, archivo)
            with open(path_archivo, 'w') as txt:
                txt.write(f"{path_archivo.stem}!")
                txt.close()
        
# El programa da la bienvenida, muestra la ruta a la carpeta Recetas, informa cuantas recetas tiene
# le pide al usuario que elija entre: leer receta / crear receta / crear categoria / eliminar receta / eliminar categoria / finalizar programa
# 1 - Primero le pide que elija una categoria (carnes, ensaladas..), y que luego elija cual receta quiere, y que al final la mueste por consola
# 2 - Pide categoria y luego que escriba el nombre y el contenido de la receta
# 3 - Pide el nombre de la categoria y crea la carpeta con ese nombre
# 4 - lo mismo que la 1, pero en vez de leer la elimina
# 5 - Pide la categoria a eliminar
# 6 - Finaliza el programa

# Cada vez que exitosamente se haga una consulta, le pida una letra al usuario para continuar
# borre la consola cada vez que vuelve al menu

def pedir_opcion(titulo:str,consultas_disponibles:list[str])-> int:
    print(titulo)
    for i,value in enumerate(consultas_disponibles):
        print(f"  [{i+1}] -> {value}")

    while True:
        op = str(input("-> ")).strip()
        if not op.isdigit():
            print(f"{op} no es un numero!")
            continue
        if len(op) != 1:
            print(f"Escribe solo un numero!")
            continue

        op = int(op)
        if not op in range(1, len(consultas_disponibles)+1):
            print(f"El numero {op} no es una opcion valida!")
            continue
        print(f"\n[{consultas_disponibles[op-1].upper()}]")
        return op

def elegir_categoria(ruta) -> Path:
    carpetas = list(Path(ruta).iterdir())
    lista_categorias = [str(os.path.basename(c)) for c in carpetas]
    opcion = pedir_opcion("Elige una de las siguientes categorias", lista_categorias)

    return Path(ruta, carpetas[opcion-1])

def elegir_receta(ruta) -> Path:
    archivos = list(Path(ruta).iterdir())
    lista_archivos = [str(os.path.basename(c.stem)).replace("_", " ") for c in archivos]
    opcion = pedir_opcion("Elige entre las siguientes recetas", lista_archivos)

    return Path(ruta, archivos[opcion-1])

def mostrar_receta(ruta:Path):
    print(ruta.read_text())

def crear_receta(ruta:Path):
    archivo_receta = input("Escribe el nombre del archivo de la receta: ").strip()+".txt"
    print("Escribe el contenido de la receta:")
    x = input() 
    contenido_receta = []
    while x != '':  
        contenido_receta.append(x+"\n") 
        x = input()
    
    print(Path(ruta, archivo_receta))
    with open(Path(ruta, archivo_receta), "w") as f:
        f.writelines(contenido_receta)
        f.close()

def bucle_programa(nombre_usuario):
    dir_recetas = Path(os.getcwd(), 'Recetas')
    consultas = ["Leer receta", "Crear nueva receta", "Crear nueva categoria", "Eliminar receta", "Eliminar categoria", "Finalizar el programa"]
    while True:
        n_recetas = len(list(dir_recetas.glob('**/*.txt')))

        os.system('cls')
        print(f"Bienvenido al programa de recetas, {nombre_usuario}!!\nActualmente hay {n_recetas} recetas disponibles\nSi quieres acceder manualmente, la ruta a la carpeta es '{dir_recetas}'")
        
        opcion = pedir_opcion("Escribe el numero de la consulta que quieres realizar:",consultas)
        
        if opcion == 6:
            break
        elif opcion == 3: # crear categoria
            nueva_categoria = input("Escribe el nombre de la categoria: ").strip()
            os.makedirs(Path(dir_recetas, nueva_categoria), exist_ok=True)
            print(f"Categoria '{nueva_categoria}' creada con exito")
        else: #opciones que se necesitan especificar una categoria
            ruta_categoria = elegir_categoria(dir_recetas)
            if opcion == 5: 
                try:
                    os.rmdir(ruta_categoria)
                    print(f"Categoria '{ruta_categoria.stem}' borrada con exito")
                except:
                    print(f"No se pudo borrar la categoria '{ruta_categoria.stem}'")
            else: #opciones de recetas
                if opcion == 2:
                    crear_receta(ruta_categoria)     
                else:
                    if len(list(ruta_categoria.iterdir())) <= 0:
                        print(f"La categoria {ruta_categoria.stem} no tiene ninguna receta aun")
                    else:
                        ruta_receta = elegir_receta(ruta_categoria)
                        if opcion == 1:
                            mostrar_receta(ruta_receta)
                        elif opcion == 4:
                            try:
                                os.remove(ruta_receta)
                                print(f"Receta '{ruta_receta.stem}' borrada con exito")
                            except:
                                print(f"No se pudo borrar la receta '{ruta_receta.stem}'")

                            

        input("Presiona enter para continuar...")

def main():
    os.system('cls')
    nombre = input("Dime tu nombre: ").strip()
    bucle_programa(nombre)
    print("Gracias por usar el programa!")
    
main()