# COLLECTIONS
from collections import Counter, defaultdict, namedtuple, deque
numeros = [8,2,4,5,8,1,4,9,2,0,2,5,6,1,2,7,5,3,4]
print(Counter(numeros)) #devuelve un diccionario que cuenta cuanta cantidad de veces se repite un elemento en una lista

serie = Counter([1,1,1,1,1,2,2,2,2,3,3,3,4])
print(serie.most_common()) # lista de tupla, (x) <- parametro para que te devuelva cuantas tuplas quieres
print()


mi_dic = {"uno": "verde", "dos":"azul", "tres":"rojo"}
mi_dic = defaultdict(lambda: "nada", mi_dic) # Si no encuentra la key, le añade este valor al diccionario en vez de dar error
print(mi_dic["cuatro"]) # no es un diccionario, es un defaultdict
print()


persona_tuple = namedtuple("Persona", ["nombre", "edad", "peso"]) # Es como hacer una clase con sus atributos, pero en forma de tupla
ozuna = persona_tuple('Ozuna', 35, 80)
print(f"{ozuna.nombre} / {ozuna.edad}")


lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]) #deque, esta guay