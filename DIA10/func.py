import os
import pygame
import game_state

def getImage(nombre_archivo, escala: tuple[int, int]|None = None):
    """Función para cargar y escalar imágenes de manera sencilla."""
    imagen = pygame.image.load(os.path.join(game_state.RUTA_IMAGENES, nombre_archivo))
    if escala is not None:
        imagen = pygame.transform.scale(imagen, escala)
    return imagen

def getSound(nombre_archivo, volumen: float = 1):
    """Función para cargar sonidos de manera sencilla."""
    sonido = pygame.mixer.Sound(os.path.join(game_state.RUTA_SONIDOS, nombre_archivo))
    sonido.set_volume(volumen)
    return sonido