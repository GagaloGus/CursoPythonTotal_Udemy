import pygame, os

DIMENSIONES = (800,600)
RUTA_IMAGENES = os.path.join(os.path.dirname(__file__), "img")


def repartidor(pantalla: pygame.Surface, coords: tuple, img: pygame.Surface):
    pantalla.blit(img, coords)

def main():
    # Inicializar pygame
    pygame.init()

    # Crear la pantalla
    pantalla = pygame.display.set_mode(DIMENSIONES)
    pygame.display.set_caption("Pizzer")

    # Cargar el icono
    icono = pygame.image.load(os.path.join(RUTA_IMAGENES, "pizzer.png"))
    pygame.display.set_icon(icono)

    # Fondo del juego
    fondo = pygame.image.load(os.path.join(RUTA_IMAGENES, "fondo.png"))
    fondo = pygame.transform.scale(fondo, DIMENSIONES)

    # Repartidor
    repartidor_img = pygame.image.load(os.path.join(RUTA_IMAGENES, "repartidor.png"))
    repartidor_img = pygame.transform.scale(repartidor_img, (80,80))
    repartidor_coordenadas_x = 360
    repartidor_coordenadas_y = 250
    repartidor_coordenadas_cambio_x = 0
    repartidor_coordenadas_cambio_y = 0
    repartidor_vel = 0.2

    # Loop de juego
    juego_activo = True
    while juego_activo:
        for evento in pygame.event.get():
            # Cerrar el juego
            if evento.type == pygame.QUIT:
                juego_activo = False

            # Tecla pulsada
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    repartidor_coordenadas_cambio_x = -repartidor_vel
                elif evento.key == pygame.K_RIGHT:
                    repartidor_coordenadas_cambio_x = repartidor_vel
                elif evento.key == pygame.K_UP:
                    repartidor_coordenadas_cambio_y = -repartidor_vel
                elif evento.key == pygame.K_DOWN:
                    repartidor_coordenadas_cambio_y = repartidor_vel
                elif evento.key == pygame.K_r:
                    # Reiniciar la posición del repartidor
                    repartidor_coordenadas_x = 360
                    repartidor_coordenadas_y = 250

            # Tecla soltada
            if evento.type == pygame.KEYUP:
                if evento.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    repartidor_coordenadas_cambio_x = 0
                if evento.key in [pygame.K_UP, pygame.K_DOWN]:
                    repartidor_coordenadas_cambio_y = 0

        # Rellenar la pantalla de un color
        # pantalla.fill((230,255,255))

        # Dibujar el fondo
        pantalla.blit(fondo, (0,0))

        # Mover al repartidor
        repartidor_coordenadas_x += repartidor_coordenadas_cambio_x
        repartidor_coordenadas_y += repartidor_coordenadas_cambio_y

        # Evitar que el repartidor salga de la pantalla
        if repartidor_coordenadas_x < 0:
            repartidor_coordenadas_x = 0
        if repartidor_coordenadas_y < 0:
            repartidor_coordenadas_y = 0
        if repartidor_coordenadas_x > DIMENSIONES[0] - repartidor_img.get_width():
            repartidor_coordenadas_x = DIMENSIONES[0] - repartidor_img.get_width()
        if repartidor_coordenadas_y > DIMENSIONES[1] - repartidor_img.get_height():
            repartidor_coordenadas_y = DIMENSIONES[1] - repartidor_img.get_height()

        # Dibujar al repartidor
        repartidor(pantalla, (repartidor_coordenadas_x, repartidor_coordenadas_y), repartidor_img)

        # Actualizar la pantalla
        pygame.display.update()

    # Salir de pygame
    pygame.quit()


if __name__ == "__main__":
    main()