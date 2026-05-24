import os
import pygame

RUTA_IMAGENES = os.path.join(os.path.dirname(__file__), "img")
RUTA_SONIDOS = os.path.join(os.path.dirname(__file__), "sounds")

def getImage(nombre_archivo, escala: tuple[int, int]|None = None):
    """Función para cargar y escalar imágenes de manera sencilla."""
    imagen = pygame.image.load(os.path.join(RUTA_IMAGENES, nombre_archivo))
    if escala is not None:
        imagen = pygame.transform.scale(imagen, escala)
    return imagen