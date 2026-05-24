import pygame
from func import *


class Bala:
    """Clase que representa una bala del juego."""
    IMAGEN = getImage("tomate.png", (36, 36))
    VELOCIDAD = 5

    def __init__(self, x, y, vx, vy, img: pygame.Surface | None = None, vel: int | None = None):
        self.x = x
        self.y = y
        self.vel = vel if vel is not None else self.VELOCIDAD
        self.vx = vx * self.vel
        self.vy = vy * self.vel
        self.img = img if img is not None else self.IMAGEN

    def draw(self, superficie: pygame.Surface):
        superficie.blit(self.img, (self.x, self.y))

    def rect(self):
        return pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())

    def center(self):
        return self.x + self.img.get_width() // 2, self.y + self.img.get_height() // 2

    def update(self):
        """Actualiza la posición de la bala"""
        self.x += self.vx
        self.y += self.vy

    def is_out_of_bounds(self, dimensiones: tuple[int, int]):
        """Verifica si la bala salió de la pantalla"""
        if (self.x < -self.img.get_width() or
            self.x > dimensiones[0] or
            self.y < -self.img.get_height() or
            self.y > dimensiones[1]):
            return True
        return False
