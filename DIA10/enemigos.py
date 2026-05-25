import pygame, math
from func import *

class Enemigo:
    """Clase base de enemigo que contiene atributos y comportamiento comunes."""

    def __init__(self, x, y, img: pygame.Surface, vel:int):
        self.x = x
        self.y = y
        self.img = img
        self.vel = vel

    def draw(self, superficie:pygame.Surface):
        superficie.blit(self.img, (self.x, self.y))

    def rect(self):
        return pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())

    def center(self):
        return self.x + self.img.get_width() // 2, self.y + self.img.get_height() // 2

    def move_towards(self, objetivo_x, objetivo_y):
        dx = objetivo_x - self.x
        dy = objetivo_y - self.y
        distancia = math.hypot(dx, dy)
        if distancia > 0:
            self.x += (dx / distancia) * self.vel
            self.y += (dy / distancia) * self.vel


class Perro(Enemigo):
    IMAGEN = getImage("dog.png", (70, 40)) # Imagen por defecto, se puede sobrescribir
    VELOCIDAD = 2

    def __init__(self, x, y, img: pygame.Surface | None = None, vel: int | None = None):
        super().__init__(x, y, img if img is not None else self.IMAGEN, vel if vel is not None else self.VELOCIDAD)

class Gato(Enemigo):
    IMAGEN = getImage("gatotomate.png", (40, 40)) # Imagen por defecto, se puede sobrescribir
    VELOCIDAD = 4

    def __init__(self, x, y, img: pygame.Surface | None = None, vel: int | None = None):
        super().__init__(x, y, img if img is not None else self.IMAGEN, vel if vel is not None else self.VELOCIDAD)