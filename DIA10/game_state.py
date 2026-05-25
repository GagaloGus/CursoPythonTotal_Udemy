"""Módulo para manejar el estado global del juego"""
import os
import random

# Variables globales privadas para tiempo
__TIEMPO_ACTUAL = 0
__TIEMPO_INICIO = 0

# Variables globales privadas para estado del juego
__VIDAS = 5
__PUNTAJE = 0
__ESTADO_JUEGO = "jugando"
__TIEMPO_FIN_JUEGO = 0

# Variables globales privadas para timing de eventos
__TIEMPO_ULTIMO_ENEMIGO = 0
__TIEMPO_ULTIMO_LANZAMIENTO = 0
__TIEMPO_ULTIMO_POWER_UP = 0
__INTERVALO_POWER_UP: int

# Constantes globales
DIMENSIONES = (1280,720)
FPS_CAP = 60
TIEMPO_SPAWN_BALA = 350
TIEMPO_SPAWN_ENEMIGO = 450
VIDAS_INICIALES = 5
DURACION_INVULNERABILIDAD = 1000
MASTER_VOLUME = 0.8
INTERVALO_POWER_UP = (10000, 20000)  # 10-20 segundos

# Estados del juego
ESTADO_JUGANDO = "jugando"
ESTADO_TERMINADO = "terminado"

# Rutas de archivos
RUTA_IMAGENES = os.path.join(os.path.dirname(__file__), "img")
RUTA_SONIDOS = os.path.join(os.path.dirname(__file__), "sounds")


# ==================== TIEMPO ====================
def actualizar_tiempo(nuevo_tiempo: int):
    """Actualiza el tiempo global del juego"""
    global __TIEMPO_ACTUAL
    __TIEMPO_ACTUAL = nuevo_tiempo

def actualizar_tiempo_inicio(tiempo_inicio: int):
    """Actualiza el tiempo de inicio del juego"""
    global __TIEMPO_INICIO
    __TIEMPO_INICIO = tiempo_inicio

def TIEMPO_ACTUAL() -> int:
    """Obtiene el tiempo actual del juego"""
    return __TIEMPO_ACTUAL

def TIEMPO_INICIO() -> int:
    """Obtiene el tiempo de inicio del juego"""
    return __TIEMPO_INICIO


# ==================== VIDAS ====================
def obtener_vidas() -> int:
    """Obtiene las vidas actuales"""
    return __VIDAS

def actualizar_vidas(nuevas_vidas: int):
    """Actualiza las vidas"""
    global __VIDAS
    __VIDAS = max(0, min(nuevas_vidas, VIDAS_INICIALES))  # Clampear entre 0 y VIDAS_INICIALES

def restar_vida():
    """Resta una vida"""
    global __VIDAS
    __VIDAS = max(0, __VIDAS - 1)

def sumar_vida():
    """Suma una vida (hasta el máximo)"""
    global __VIDAS
    __VIDAS = min(__VIDAS + 1, VIDAS_INICIALES)

def inicializar_vidas():
    """Reinicia las vidas al valor inicial"""
    global __VIDAS
    __VIDAS = VIDAS_INICIALES


# ==================== PUNTAJE ====================
def obtener_puntaje() -> int:
    """Obtiene el puntaje actual"""
    return __PUNTAJE

def actualizar_puntaje(nuevo_puntaje: int):
    """Actualiza el puntaje"""
    global __PUNTAJE
    __PUNTAJE = max(0, nuevo_puntaje)

def sumar_puntos(puntos: int):
    """Suma puntos al puntaje actual"""
    global __PUNTAJE
    __PUNTAJE += max(0, puntos)

def inicializar_puntaje():
    """Reinicia el puntaje a 0"""
    global __PUNTAJE
    __PUNTAJE = 0


# ==================== ESTADO DEL JUEGO ====================
def obtener_estado_juego() -> str:
    """Obtiene el estado actual del juego"""
    return __ESTADO_JUEGO

def cambiar_estado_juego(nuevo_estado: str):
    """Cambia el estado del juego"""
    global __ESTADO_JUEGO
    if nuevo_estado in [ESTADO_JUGANDO, ESTADO_TERMINADO]:
        __ESTADO_JUEGO = nuevo_estado
    else:
        print(f"Estado de juego inválido: {nuevo_estado}")

def is_jugando() -> bool:
    """Verifica si el juego está en estado jugando"""
    return __ESTADO_JUEGO == ESTADO_JUGANDO

def is_terminado() -> bool:
    """Verifica si el juego está terminado"""
    return __ESTADO_JUEGO == ESTADO_TERMINADO


# ==================== TIEMPO FIN JUEGO ====================
def obtener_tiempo_fin_juego() -> int:
    """Obtiene el tiempo en el que terminó el juego"""
    return __TIEMPO_FIN_JUEGO

def establecer_tiempo_fin_juego(tiempo: int):
    """Establece el tiempo en el que terminó el juego"""
    global __TIEMPO_FIN_JUEGO
    __TIEMPO_FIN_JUEGO = tiempo


# ==================== TIMING DE EVENTOS ====================
def obtener_tiempo_ultimo_enemigo() -> int:
    """Obtiene el tiempo del último enemigo generado"""
    return __TIEMPO_ULTIMO_ENEMIGO

def actualizar_tiempo_ultimo_enemigo():
    """Actualiza el tiempo del último enemigo generado"""
    global __TIEMPO_ULTIMO_ENEMIGO
    __TIEMPO_ULTIMO_ENEMIGO = TIEMPO_ACTUAL()

def obtener_tiempo_ultimo_lanzamiento() -> int:
    """Obtiene el tiempo del último lanzamiento de bala"""
    return __TIEMPO_ULTIMO_LANZAMIENTO

def actualizar_tiempo_ultimo_lanzamiento():
    """Actualiza el tiempo del último lanzamiento de bala"""
    global __TIEMPO_ULTIMO_LANZAMIENTO
    __TIEMPO_ULTIMO_LANZAMIENTO = TIEMPO_ACTUAL()


def obtener_tiempo_ultimo_power_up() -> int:
    """Obtiene el tiempo del último power-up generado"""
    return __TIEMPO_ULTIMO_POWER_UP

def actualizar_tiempo_ultimo_power_up():
    """Actualiza el tiempo del último power-up generado"""
    global __TIEMPO_ULTIMO_POWER_UP
    __TIEMPO_ULTIMO_POWER_UP = TIEMPO_ACTUAL()


def obtener_intervalo_power_up() -> int:
    """Obtiene el intervalo para el siguiente power-up"""
    return __INTERVALO_POWER_UP

def generar_nuevo_intervalo_power_up():
    """Genera un nuevo intervalo aleatorio para el power-up (10-20 segundos)"""
    global __INTERVALO_POWER_UP
    __INTERVALO_POWER_UP = random.randint(INTERVALO_POWER_UP[0], INTERVALO_POWER_UP[1])


# ==================== REINICIO DEL JUEGO ====================
def reiniciar_juego():
    """Reinicia todos los estados del juego"""
    global __VIDAS, __PUNTAJE, __ESTADO_JUEGO, __TIEMPO_FIN_JUEGO
    global __TIEMPO_ULTIMO_ENEMIGO, __TIEMPO_ULTIMO_LANZAMIENTO, __TIEMPO_ULTIMO_POWER_UP

    __VIDAS = VIDAS_INICIALES
    __PUNTAJE = 0
    __ESTADO_JUEGO = ESTADO_JUGANDO
    __TIEMPO_FIN_JUEGO = 0
    __TIEMPO_ULTIMO_ENEMIGO = 0
    __TIEMPO_ULTIMO_LANZAMIENTO = 0
    __TIEMPO_ULTIMO_POWER_UP = 0
    generar_nuevo_intervalo_power_up()

def estado_juego():
    """Función de prueba para verificar el estado del juego"""
    print(f"Vidas: {obtener_vidas()}")
    print(f"Puntaje: {obtener_puntaje()}")
    print(f"Estado del juego: {obtener_estado_juego()}")
    print(f"Tiempo actual: {TIEMPO_ACTUAL()}")
    print(f"Tiempo de inicio: {TIEMPO_INICIO()}")
    print(f"Tiempo del último enemigo: {obtener_tiempo_ultimo_enemigo()}")
    print(f"Tiempo del último lanzamiento: {obtener_tiempo_ultimo_lanzamiento()}")
    print(f"Tiempo del último power-up: {obtener_tiempo_ultimo_power_up()}")
    print(f"Intervalo para el siguiente power-up: {obtener_intervalo_power_up()}")

def variables_check_juego():
    """Función de prueba para verificar las variables del juego"""
    print(f"Vidas: {VIDAS_INICIALES}")
    print(f"Dimensiones: {DIMENSIONES}")
    print(f"FPS Cap: {FPS_CAP}")
    print(f"Tiempo de spawn bala: {TIEMPO_SPAWN_BALA}")
    print(f"Tiempo de spawn enemigo: {TIEMPO_SPAWN_ENEMIGO}")
    print(f"Duracion invulnerabilidad: {DURACION_INVULNERABILIDAD}")
    print(f"Volumen maestro: {MASTER_VOLUME}")
    print(f"Rutas:\n  Imagenes: {RUTA_IMAGENES}\n  Sonidos:  {RUTA_SONIDOS}")



if __name__ == "__main__":
    import main
    main.main()