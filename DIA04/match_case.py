serie = "N-01"
match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe")

cliente = {'nombre': 'Fede', 'edad': 28}
pelicula = {'titulo': 'Matrix', 
            'ficha_tecnica':{
                'protagonista':'Keanu Reeves',
                'director':'Lana y Lilly Wachowski'}}

elementos = [cliente, pelicula, 'guayaba']
for e in elementos:
    match e:
        case {'nombre': _nombre, 'edad': _edad}:
            print(f"Es un cliente: {_nombre} ({_edad})")
        case {'titulo':_titulo, 'ficha_tecnica':{'protagonista': _prota, 'director': _director}}:
            print(f"Es una pelicula: {_titulo}, {_prota}, {_director}")
        case _:
            print("no se")