# Quita la cadena de caracteres especificados empezando por la izquierda, en el momento en el que aparece un caracter no especificado deja de borrar
print("_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(',:%_#'))

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 
frutas.insert(3,"naranja") # Inserta un elemento en el indice especificado
print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
# Devuelve true si no tienen ningun elemento en comun
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)

