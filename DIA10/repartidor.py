import pygame
from func import *


class Repartidor:
    """Clase que representa al repartidor del juego."""
    IMAGEN = getImage("repartidor.png", (80, 80))
    VELOCIDAD = 7
    POSICION_INICIAL = (360, 250)

    def __init__(self, img: pygame.Surface | None = None, vel: int | None = None):
        self.img = img if img is not None else self.IMAGEN
        self.vel = vel if vel is not None else self.VELOCIDAD
        self.x, self.y = self.POSICION_INICIAL
        self.cambio_x = 0
        self.cambio_y = 0
        self.es_invulnerable = False
        self.tiempo_ultimo_golpe = 0
        # Rastrear qué teclas de dirección están presionadas
        self.teclas_presionadas = {
            'LEFT': False,
            'RIGHT': False,
            'UP': False,
            'DOWN': False
        }

    def handle_key_down(self, key):
        """Procesa cuando se presiona una tecla de dirección"""
        if key == pygame.K_LEFT:
            self.teclas_presionadas['LEFT'] = True
            self.cambio_x = -self.vel
        elif key == pygame.K_RIGHT:
            self.teclas_presionadas['RIGHT'] = True
            self.cambio_x = self.vel
        elif key == pygame.K_UP:
            self.teclas_presionadas['UP'] = True
            self.cambio_y = -self.vel
        elif key == pygame.K_DOWN:
            self.teclas_presionadas['DOWN'] = True
            self.cambio_y = self.vel

    def handle_key_up(self, key):
        """Procesa cuando se suelta una tecla de dirección"""
        if key == pygame.K_LEFT:
            self.teclas_presionadas['LEFT'] = False
            # Solo poner cambio_x a 0 si no hay otra tecla horizontal presionada
            if not self.teclas_presionadas['RIGHT']:
                self.cambio_x = 0
            else:
                self.cambio_x = self.vel
        elif key == pygame.K_RIGHT:
            self.teclas_presionadas['RIGHT'] = False
            if not self.teclas_presionadas['LEFT']:
                self.cambio_x = 0
            else:
                self.cambio_x = -self.vel
        elif key == pygame.K_UP:
            self.teclas_presionadas['UP'] = False
            # Solo poner cambio_y a 0 si no hay otra tecla vertical presionada
            if not self.teclas_presionadas['DOWN']:
                self.cambio_y = 0
            else:
                self.cambio_y = self.vel
        elif key == pygame.K_DOWN:
            self.teclas_presionadas['DOWN'] = False
            if not self.teclas_presionadas['UP']:
                self.cambio_y = 0
            else:
                self.cambio_y = -self.vel
                
    def draw(self, superficie: pygame.Surface, tiempo_actual: int):
        """Dibuja al repartidor con efecto de parpadeo si está invulnerable"""
        if self.es_invulnerable:
            # Calcular tiempo transcurrido desde el último golpe
            tiempo_transcurrido = tiempo_actual - self.tiempo_ultimo_golpe
            # Crear efecto de parpadeo: alterna visibilidad cada 100 ms
            if (tiempo_transcurrido // 100) % 2 == 0:
                superficie.blit(self.img, (self.x, self.y))
        else:
            superficie.blit(self.img, (self.x, self.y))

    def rect(self):
        """Retorna el rectángulo de colisión del repartidor"""
        return pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())

    def center(self):
        """Retorna las coordenadas del centro del repartidor"""
        return self.x + self.img.get_width() // 2, self.y + self.img.get_height() // 2

    def set_velocity(self, cambio_x: int, cambio_y: int):
        """Establece la velocidad de movimiento del repartidor"""
        self.cambio_x = cambio_x
        self.cambio_y = cambio_y

    def update(self, dimensiones: tuple[int, int]):
        """Actualiza la posición del repartidor y aplica límites de pantalla"""
        self.x += self.cambio_x
        self.y += self.cambio_y

        # Evitar que el repartidor salga de la pantalla
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.x > dimensiones[0] - self.img.get_width():
            self.x = dimensiones[0] - self.img.get_width()
        if self.y > dimensiones[1] - self.img.get_height():
            self.y = dimensiones[1] - self.img.get_height()

    def reset(self):
        """Reinicia la posición del repartidor a la posición inicial"""
        self.x, self.y = self.POSICION_INICIAL

    def apply_invulnerability(self, tiempo_actual: int):
        """Aplica el estado de invulnerabilidad al repartidor"""
        self.es_invulnerable = True
        self.tiempo_ultimo_golpe = tiempo_actual

    def check_invulnerability(self, tiempo_actual: int, duracion: int):
        """Verifica si el tiempo de invulnerabilidad ha expirado"""
        if self.es_invulnerable and tiempo_actual - self.tiempo_ultimo_golpe >= duracion:
            self.es_invulnerable = False
