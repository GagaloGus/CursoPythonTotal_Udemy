def generador_turnos():
    turno = 0
    while True:
        turno += 1
        if turno >= 100:
            turno = 0
        yield turno

g_turnos = list(generador_turnos() for i in range(10)) # Genera una lista de 10 generadores, ampliable

def seccion_handler(seccion:int):
    letra_seccion = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[seccion]
    turno = str(next(g_turnos[seccion])).zfill(2) # Rellena con un ceros hasta que el string alcance la longitud indicada
    return f"{letra_seccion}-{turno}"


def decorador_texto_turno(turno:str, seccion:int, secciones:list[str]):
    return f"""
╔╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╗
║                           ║
║      Su turno es el       ║
║         = {turno} =          ║
║         {secciones[seccion]}         ║
║                           ║
║  En breve sera atendido.. ║
║                           ║
╚╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╝
"""