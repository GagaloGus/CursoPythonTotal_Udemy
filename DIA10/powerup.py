import pygame
from func import *

class PowerUp:
    """Clase que representa un power-up (pizza) que recupera vidas."""
    IMAGEN = getImage("pizza.png", (50, 50))
    DURACION_VISIBLE = 5000  # 5 segundos en milisegundos
    pygame.mixer.init()
    SONIDO_RECOGIDO = getSound("eat-tf2.mp3", 0.5 * game_state.MASTER_VOLUME)

    def __init__(self, x, y, img: pygame.Surface | None = None):
        self.x = x
        self.y = y
        self.img = img if img is not None else self.IMAGEN
        self.tiempo_spawn = pygame.time.get_ticks()

    def play_sfx(self):
        """Reproduce el sonido de recogida del power-up."""
        self.SONIDO_RECOGIDO.play()
        
    def draw(self, superficie: pygame.Surface):
        """Dibuja el power-up en la pantalla"""
        superficie.blit(self.img, (self.x, self.y))

    def rect(self):
        """Retorna el rectángulo de colisión del power-up"""
        return pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())

    def center(self):
        """Retorna las coordenadas del centro del power-up"""
        return self.x + self.img.get_width() // 2, self.y + self.img.get_height() // 2

    def is_expired(self, tiempo_actual: int) -> bool:
        """Verifica si el power-up ha expirado (pasaron 5 segundos)"""
        return tiempo_actual - self.tiempo_spawn >= self.DURACION_VISIBLE
