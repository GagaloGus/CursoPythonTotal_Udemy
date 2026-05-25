import pygame
from game_state import TIEMPO_ACTUAL, TIEMPO_INICIO
from func import *


class Interfaz:
    """Maneja la interfaz de usuario del juego: vidas, puntaje, cronómetro y pantalla de fin."""

    def __init__(self, dimensiones: tuple[int, int]):
        self.dimensiones = dimensiones
        self.vida_img = getImage("heart.png", (40, 40))
        self.fuente = pygame.font.SysFont(None, 36)
        self.fuente_grande = pygame.font.SysFont(None, 80)

    def dibujar_interfaz_juego(self, superficie: pygame.Surface, vidas: int, puntaje: int, estado_juego: str, tiempo_fin_juego: int, estado_terminado: str):
        """Dibuja la interfaz durante el juego."""
        self.dibujar_vidas(superficie, vidas)
        self.dibujar_puntaje(superficie, puntaje)
        self.dibujar_cronometro(superficie, estado_juego, tiempo_fin_juego, estado_terminado)


    def dibujar_vidas(self, superficie: pygame.Surface, vidas: int):
        """Dibuja las vidas en la esquina superior izquierda."""
        for i in range(vidas):
            superficie.blit(self.vida_img, (10 + i * 50, 10))

    def dibujar_puntaje(self, superficie: pygame.Surface, puntaje: int):
        """Dibuja el puntaje en la esquina superior derecha."""
        texto_puntaje = self.fuente.render(f"Puntos: {puntaje}", True, (255, 255, 255))
        superficie.blit(texto_puntaje, (self.dimensiones[0] - texto_puntaje.get_width() - 10, 10))

    def calcular_tiempo_transcurrido(self,
                                    estado_juego: str, tiempo_fin_juego: int,
                                    estado_terminado: str) -> str:
        """Calcula el tiempo transcurrido en formato M:SS."""
        if estado_juego == estado_terminado:
            tiempo_ms = tiempo_fin_juego - TIEMPO_INICIO()
        else:
            tiempo_ms = TIEMPO_ACTUAL() - TIEMPO_INICIO()

        segundos_totales = tiempo_ms // 1000
        minutos = segundos_totales // 60
        segundos = segundos_totales % 60
        return f"{minutos}:{segundos:02d}"

    def dibujar_cronometro(self, superficie: pygame.Surface, estado_juego: str,
                          tiempo_fin_juego: int, estado_terminado: str):
        """Dibuja el cronómetro en la parte superior central."""
        tiempo_str = self.calcular_tiempo_transcurrido(
            estado_juego,
            tiempo_fin_juego,
            estado_terminado,
        )
        texto_tiempo = self.fuente.render(tiempo_str, True, (255, 255, 255))
        x = (self.dimensiones[0] - texto_tiempo.get_width()) // 2
        superficie.blit(texto_tiempo, (x, 10))

    def dibujar_pantalla_fin(self, superficie: pygame.Surface, puntaje: int,
                            tiempo_fin_juego: int, estado_juego: str,
                            estado_terminado: str):
        """Dibuja la pantalla de fin de juego con puntaje y tiempo."""
        fondo_oscuro = pygame.Surface(self.dimensiones)
        fondo_oscuro.set_alpha(128)
        fondo_oscuro.fill((0, 0, 0))
        superficie.blit(fondo_oscuro, (0, 0))

        texto_game_over = self.fuente_grande.render("GAME OVER", True, (255, 0, 0))
        x_game_over = (self.dimensiones[0] - texto_game_over.get_width()) // 2
        superficie.blit(texto_game_over, (x_game_over, self.dimensiones[1] // 2 - 100))

        texto_puntaje_final = self.fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
        x_puntaje = (self.dimensiones[0] - texto_puntaje_final.get_width()) // 2
        superficie.blit(texto_puntaje_final, (x_puntaje, self.dimensiones[1] // 2 + 50))

        tiempo_str = self.calcular_tiempo_transcurrido(
            estado_juego,
            tiempo_fin_juego,
            estado_terminado,
        )
        texto_tiempo_final = self.fuente.render(f"Tiempo: {tiempo_str}", True, (255, 255, 255))
        x_tiempo = (self.dimensiones[0] - texto_tiempo_final.get_width()) // 2
        superficie.blit(texto_tiempo_final, (x_tiempo, self.dimensiones[1] // 2 + 100))
