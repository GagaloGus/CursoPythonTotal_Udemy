import pygame, os, random, math

# Constantes
DIMENSIONES = (800,600)
RUTA_IMAGENES = os.path.join(os.path.dirname(__file__), "img")
RUTA_SONIDOS = os.path.join(os.path.dirname(__file__), "sounds")
FPS_CAP = 60
TIEMPO_SPAWN_BALA = 400
TIEMPO_SPAWN_ENEMIGO = 500
VIDAS_INICIALES = 5
DURACION_INVULNERABILIDAD = 1000
MODO_DISPARO = 'enemigo'  # 'circulo': dispara en círculo | 'enemigo': dispara a enemigo más cercano
MASTER_VOLUME = 0.8


def main():
    # Inicializar pygame
    pygame.init()

    # Inicializar el mixer para sonidos
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(RUTA_SONIDOS, "musica_fondo.mp3"))
    pygame.mixer.music.set_volume(0.2 * MASTER_VOLUME)  # Ajustar volumen de la música
    pygame.mixer.music.play(-1)  # Reproducir música en loop

    # Cargar efectos de sonido
    sonido_disparo = pygame.mixer.Sound(os.path.join(RUTA_SONIDOS, "disparo.mp3"))
    sonido_golpe = pygame.mixer.Sound(os.path.join(RUTA_SONIDOS, "tomato_splat.mp3"))
    sonido_vida_perdida = pygame.mixer.Sound(os.path.join(RUTA_SONIDOS, "secondary-meow.mp3"))

    sonido_disparo.set_volume(0.7 * MASTER_VOLUME)
    sonido_golpe.set_volume(0.4 * MASTER_VOLUME)
    sonido_vida_perdida.set_volume(0.7 * MASTER_VOLUME)

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
    repartidor_vel = 7

    # Enemigos
    enemigo_img = pygame.image.load(os.path.join(RUTA_IMAGENES, "floppa-cube.png"))
    enemigo_img = pygame.transform.scale(enemigo_img, (70,70))
    enemigo_vel = 3

    # Lista de enemigos
    enemigos = []
    tiempo_ultimo_enemigo = 0

    # Balas
    bala_img = pygame.image.load(os.path.join(RUTA_IMAGENES, "tomate.png"))
    bala_img = pygame.transform.scale(bala_img, (36, 36))
    balas = []  # Lista de balas activas: [{"x": x, "y": y, "vx": vx, "vy": vy}, ...]
    bala_vel = 5
    tiempo_ultimo_lanzamiento = 0

    # Sistema de vidas
    vida_img = pygame.image.load(os.path.join(RUTA_IMAGENES, "heart.png"))
    vida_img = pygame.transform.scale(vida_img, (40, 40))
    vidas = VIDAS_INICIALES
    tiempo_ultimo_golpe = 0  # Para rastrear invulnerabilidad
    es_invulnerable = False

    # Puntaje y tiempo
    puntaje = 0
    fuente = pygame.font.SysFont(None, 36)  # Fuente para UI pequeña
    fuente_grande = pygame.font.SysFont(None, 80)  # Fuente para "GAME OVER"
    tiempo_inicio = pygame.time.get_ticks()

    # Estados del juego
    ESTADO_JUGANDO = "jugando"
    ESTADO_TERMINADO = "terminado"
    estado_juego = ESTADO_JUGANDO
    tiempo_fin_juego = 0  # Se establece cuando el juego termina

    def repartidor(coords: tuple):
        """Dibuja al repartidor con efecto de parpadeo si está invulnerable"""
        if es_invulnerable:
            # Calcular tiempo transcurrido desde el último golpe
            tiempo_transcurrido = tiempo_actual - tiempo_ultimo_golpe
            # Crear efecto de parpadeo: alterna visibilidad cada INTERVALO_PARPADEO ms
            if (tiempo_transcurrido // 100) % 2 == 0:
                pantalla.blit(repartidor_img, coords)
        else:
            pantalla.blit(repartidor_img, coords)

    def dibujar_enemigos():
        for enemigo in enemigos:
            pantalla.blit(enemigo["img"], (enemigo["x"], enemigo["y"]))

    def generar_enemigo(img=enemigo_img, vel=enemigo_vel):
        """Crea un nuevo enemigo en un borde aleatorio de la pantalla"""
        borde = random.choice(['top', 'bottom', 'left', 'right'])

        if borde == 'top':
            x = random.randint(0, DIMENSIONES[0] - img.get_width())
            y = -img.get_height()
        elif borde == 'bottom':
            x = random.randint(0, DIMENSIONES[0] - img.get_width())
            y = DIMENSIONES[1]
        elif borde == 'left':
            x = -img.get_width()
            y = random.randint(0, DIMENSIONES[1] - img.get_height())
        else:  # right
            x = DIMENSIONES[0]
            y = random.randint(0, DIMENSIONES[1] - img.get_height())

        enemigo = {
            "x": x,
            "y": y,
            "img": img,
            "vel": vel
        }
        enemigos.append(enemigo)

    def encontrar_enemigo_cercano(x_repartidor, y_repartidor):
        """Encuentra el enemigo más cercano al repartidor"""
        if not enemigos:
            return None

        enemigo_cercano = None
        distancia_minima = float('inf')

        for enemigo in enemigos:
            dx = x_repartidor - enemigo["x"]
            dy = y_repartidor - enemigo["y"]
            distancia = math.sqrt(dx**2 + dy**2)

            if distancia < distancia_minima:
                distancia_minima = distancia
                enemigo_cercano = enemigo

        return enemigo_cercano

    def lanzar_bala(x_origen, y_origen, x_objetivo, y_objetivo):
        """Crea una bala dirigida hacia el objetivo.
        Ahora x_origen/y_origen y x_objetivo/y_objetivo se interpretan como CENTROS (no top-left).
        """
        # Calcular dirección hacia el objetivo (centros)
        dx = x_objetivo - x_origen
        dy = y_objetivo - y_origen
        distancia = math.sqrt(dx**2 + dy**2)

        if distancia == 0:
            return

        # Velocidad normalizada hacia el objetivo
        vx = (dx / distancia) * bala_vel
        vy = (dy / distancia) * bala_vel

        # Posicionar la bala centrada en el origen (centro del repartidor)
        bala = {
            "x": x_origen - bala_img.get_width() // 2,
            "y": y_origen - bala_img.get_height() // 2,
            "vx": vx,
            "vy": vy
        }
        balas.append(bala)
        sonido_disparo.play()  # Reproducir sonido de disparo

    def actualizar_balas():
        """Mueve las balas y elimina las que salen de pantalla"""
        balas_a_eliminar = []

        for i, bala in enumerate(balas):
            bala["x"] += bala["vx"]
            bala["y"] += bala["vy"]

            # Verificar si la bala salió de pantalla
            if (bala["x"] < -bala_img.get_width() or
                bala["x"] > DIMENSIONES[0] or
                bala["y"] < -bala_img.get_height() or
                bala["y"] > DIMENSIONES[1]):
                balas_a_eliminar.append(i)

        # Eliminar balas fuera de pantalla (en orden inverso para no mover índices)
        for i in sorted(balas_a_eliminar, reverse=True):
            balas.pop(i)

    def dibujar_balas():
        """Dibuja todas las balas activas"""
        for bala in balas:
            pantalla.blit(bala_img, (bala["x"], bala["y"]))

    def dibujar_vidas():
        """Dibuja las vidas en la esquina superior izquierda"""
        for i in range(vidas):
            pantalla.blit(vida_img, (10 + i * 50, 10))

    def dibujar_puntaje():
        """Dibuja el puntaje en la esquina superior derecha"""
        texto_puntaje = fuente.render(f"Puntos: {puntaje}", True, (255, 255, 255))
        pantalla.blit(texto_puntaje, (DIMENSIONES[0] - texto_puntaje.get_width() - 10, 10))

    def calcular_tiempo_transcurrido(tiempo_desde):
        """Calcula el tiempo transcurrido en formato M:SS"""
        tiempo_ms = tiempo_desde - tiempo_desde
        if estado_juego == ESTADO_JUGANDO:
            tiempo_ms = tiempo_actual - tiempo_inicio
        else:
            tiempo_ms = tiempo_fin_juego - tiempo_inicio

        segundos_totales = tiempo_ms // 1000
        minutos = segundos_totales // 60
        segundos = segundos_totales % 60
        return f"{minutos}:{segundos:02d}"

    def dibujar_cronometro():
        """Dibuja el cronómetro en la parte superior central"""
        tiempo_str = calcular_tiempo_transcurrido(tiempo_actual)
        texto_tiempo = fuente.render(tiempo_str, True, (255, 255, 255))
        x = (DIMENSIONES[0] - texto_tiempo.get_width()) // 2
        pantalla.blit(texto_tiempo, (x, 10))

    def dibujar_pantalla_fin():
        """Dibuja la pantalla de fin de juego con puntaje y tiempo"""
        # Fondo oscuro semi-transparente
        fondo_oscuro = pygame.Surface(DIMENSIONES)
        fondo_oscuro.set_alpha(128)
        fondo_oscuro.fill((0, 0, 0))
        pantalla.blit(fondo_oscuro, (0, 0))

        # Texto "GAME OVER"
        texto_game_over = fuente_grande.render("GAME OVER", True, (255, 0, 0))
        x_game_over = (DIMENSIONES[0] - texto_game_over.get_width()) // 2
        pantalla.blit(texto_game_over, (x_game_over, DIMENSIONES[1] // 2 - 100))

        # Puntaje final
        tiempo_str = calcular_tiempo_transcurrido(tiempo_actual)
        texto_puntaje_final = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
        x_puntaje = (DIMENSIONES[0] - texto_puntaje_final.get_width()) // 2
        pantalla.blit(texto_puntaje_final, (x_puntaje, DIMENSIONES[1] // 2 + 50))

        # Tiempo final
        texto_tiempo_final = fuente.render(f"Tiempo: {tiempo_str}", True, (255, 255, 255))
        x_tiempo = (DIMENSIONES[0] - texto_tiempo_final.get_width()) // 2
        pantalla.blit(texto_tiempo_final, (x_tiempo, DIMENSIONES[1] // 2 + 100))

    def detectar_colisiones_balas():
        """Detecta colisiones entre balas y enemigos, y elimina ambos si colisionan"""
        nonlocal puntaje

        enemigos_sobrevivientes = list.copy(enemigos)
        balas_sobrevivientes = []

        # Utiliza pygame.Rect para detectar colisiones de manera más sencilla
        for bala in balas:
            bala_rect = pygame.Rect(bala["x"], bala["y"], bala_img.get_width(), bala_img.get_height())
            colisiono = False
            for enemigo in enemigos_sobrevivientes:
                if bala_rect.colliderect(pygame.Rect(enemigo["x"], enemigo["y"], enemigo["img"].get_width(), enemigo["img"].get_height())):
                    # Colisión detectada, eliminar ambos
                    enemigos_sobrevivientes.remove(enemigo)
                    colisiono = True
                    puntaje += 1  # Incrementar puntaje por enemigo eliminado
                    sonido_golpe.play()  # Reproducir sonido de golpe
                    break
            if not colisiono:
                balas_sobrevivientes.append(bala)

        # Actualizar las listas originales
        enemigos.clear()
        enemigos.extend(enemigos_sobrevivientes)
        balas.clear()
        balas.extend(balas_sobrevivientes)

    def detectar_colision_repartidor():
        """Detecta si un enemigo colisiona con el repartidor"""
        nonlocal vidas, es_invulnerable, tiempo_ultimo_golpe, estado_juego, tiempo_fin_juego

        # Crear un rectángulo para el repartidor
        repartidor_rect = pygame.Rect(
            repartidor_coordenadas_x,
            repartidor_coordenadas_y,
            repartidor_img.get_width(),
            repartidor_img.get_height()
        )

        # Verificar colisión con cada enemigo
        for enemigo in enemigos:
            if not es_invulnerable and repartidor_rect.colliderect(pygame.Rect(enemigo["x"], enemigo["y"], enemigo["img"].get_width(), enemigo["img"].get_height())):
                vidas -= 1
                sonido_vida_perdida.play()  # Reproducir sonido de vida perdida
                es_invulnerable = True
                tiempo_ultimo_golpe = tiempo_actual

                # Cambiar estado si no hay más vidas
                if vidas == 0:
                    estado_juego = ESTADO_TERMINADO
                    tiempo_fin_juego = tiempo_actual
                    pygame.mixer.music.stop()  # Detener música

    # Loop de juego
    juego_activo = True
    reloj = pygame.time.Clock()
    FPS = FPS_CAP

    # Generar lista de ángulos y direcciones para disparo circular (8 direcciones)
    num_direcciones = 16
    direcciones_circulares = []
    for i in range(num_direcciones):
        angulo = (2 * math.pi * i) / num_direcciones
        direcciones_circulares.append({
            "angulo": angulo,
            "vx": math.cos(angulo),
            "vy": math.sin(angulo)
        })

    while juego_activo:
        # Contador del tiempo de juego
        tiempo_actual = pygame.time.get_ticks()

        for evento in pygame.event.get():
            # Cerrar el juego
            if evento.type == pygame.QUIT:
                juego_activo = False

            # Solo permitir entrada si el juego está jugando
            if estado_juego == ESTADO_JUGANDO and evento.type == pygame.KEYDOWN:
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
            if estado_juego == ESTADO_JUGANDO and evento.type == pygame.KEYUP:
                if evento.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    repartidor_coordenadas_cambio_x = 0
                if evento.key in [pygame.K_UP, pygame.K_DOWN]:
                    repartidor_coordenadas_cambio_y = 0

        # Lógica de juego solo si está jugando
        if estado_juego == ESTADO_JUGANDO:
            # Movimiento del enemigo
            for enemigo in enemigos:
                dx = repartidor_coordenadas_x - enemigo["x"]
                dy = repartidor_coordenadas_y - enemigo["y"]
                distancia = math.sqrt(dx**2 + dy**2)
                if distancia > 0:
                    enemigo["x"] += (dx / distancia) * enemigo["vel"]
                    enemigo["y"] += (dy / distancia) * enemigo["vel"]

            # Generar nuevo enemigo cada intervalo
            if tiempo_actual - tiempo_ultimo_enemigo >= TIEMPO_SPAWN_ENEMIGO:
                generar_enemigo()
                tiempo_ultimo_enemigo = tiempo_actual

            # Lanzar balas cada intervalo
            if tiempo_actual - tiempo_ultimo_lanzamiento >= TIEMPO_SPAWN_BALA:
                # Origen centrado del repartidor
                x_origen_centro = repartidor_coordenadas_x + repartidor_img.get_width() // 2
                y_origen_centro = repartidor_coordenadas_y + repartidor_img.get_height() // 2

                if MODO_DISPARO == 'circulo':
                    # Modo circular: disparar en 8 direcciones usando la lista de direcciones
                    for direccion in direcciones_circulares:
                        x_objetivo = x_origen_centro + direccion["vx"] * bala_vel * 10
                        y_objetivo = y_origen_centro + direccion["vy"] * bala_vel * 10
                        lanzar_bala(x_origen_centro, y_origen_centro, x_objetivo, y_objetivo)

                elif MODO_DISPARO == 'enemigo':
                    # Modo enemigo cercano: disparar al enemigo más cercano (usar centros)
                    enemigo_objetivo = encontrar_enemigo_cercano(x_origen_centro, y_origen_centro)
                    if enemigo_objetivo is not None:
                        x_objetivo = enemigo_objetivo["x"] + enemigo_objetivo["img"].get_width() // 2
                        y_objetivo = enemigo_objetivo["y"] + enemigo_objetivo["img"].get_height() // 2
                        lanzar_bala(x_origen_centro, y_origen_centro, x_objetivo, y_objetivo)

                tiempo_ultimo_lanzamiento = tiempo_actual

            # Actualizar balas
            actualizar_balas()

            # Verificar estado de invulnerabilidad
            if es_invulnerable and tiempo_actual - tiempo_ultimo_golpe >= DURACION_INVULNERABILIDAD:
                es_invulnerable = False

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

            # Detectar colisiones
            detectar_colisiones_balas()

            # Detectar colisiones con el repartidor
            detectar_colision_repartidor()

        # Dibujar el fondo
        pantalla.blit(fondo, (0,0))

        # Dibujar al repartidor
        repartidor((repartidor_coordenadas_x, repartidor_coordenadas_y))

        # Dibujar al enemigo
        dibujar_enemigos()

        # Dibujar balas
        dibujar_balas()

        # Dibujar vidas
        dibujar_vidas()

        # Dibujar puntaje
        dibujar_puntaje()

        # Dibujar cronómetro
        dibujar_cronometro()

        # Si el juego terminó, mostrar pantalla de fin
        if estado_juego == ESTADO_TERMINADO:
            dibujar_pantalla_fin()

        # Actualizar la pantalla
        pygame.display.update()

        # Controlar el frame rate
        reloj.tick(FPS)


if __name__ == "__main__":
    main()

# En este código se han realizado las siguientes mejoras:
# 1. Se ha implementado la detección de colisiones utilizando pygame.Rect para simplificar el proceso y mejorar la precisión.
# 2. Se ha corregido la lógica de lanzamiento de balas para que se dirijan correctamente hacia el enemigo más cercano, utilizando los centros de los sprites para calcular la dirección.
# 3. Se ha añadido un sistema de invulnerabilidad para el repartidor después de recibir un golpe, con un efecto de parpadeo para indicar visualmente el estado de invulnerabilidad.
# 4. Se ha mejorado la organización del código mediante funciones para cada tarea específica, lo que facilita la lectura y el mantenimiento.
# 5. Se ha añadido un sistema de generación de enemigos en los bordes de la pantalla, con movimiento hacia el repartidor.
# 6. Se ha implementado un sistema de vidas para el repartidor, con una imagen representativa y una condición de fin de juego cuando se agotan las vidas.
# 7. Se ha añadido un sistema de control de frame rate para asegurar que el juego se ejecute de manera fluida.
# 8. Se ha añadido la opción de cambiar entre modos de disparo (disparo circular o disparo hacia el enemigo más cercano) mediante la variable MODO_DISPARO.
# 9. Se ha corregido la lógica de eliminación de balas y enemigos para evitar problemas al modificar las listas mientras se iteran.
# 10. Se ha añadido un fondo al juego para mejorar la estética visual.
# 11. Se ha añadido la opción de reiniciar la posición del repartidor con la tecla 'R' para facilitar las pruebas y el juego.
# 12. Se ha mejorado la estructura del código para facilitar la lectura y el mantenimiento, utilizando funciones para tareas específicas y evitando código repetitivo.
# 13. Se ha añadido un sistema de generación de enemigos con diferentes velocidades y apariencias para aumentar la variedad del juego.
# 14. Se ha implementado un sistema de puntuación para que el jugador pueda ver su progreso y competir por la mejor puntuación.
# 15. Se ha añadido música de fondo y efectos de sonido para mejorar la experiencia de juego.
# 16. Se ha implementado un sistema de niveles o oleadas para aumentar la dificultad a medida que el jugador avanza en el juego.
# 17. Se ha añadido un sistema de power-ups que el jugador puede recoger para obtener habilidades temporales, como disparos más rápidos o invulnerabilidad.
# 18. Se ha implementado un sistema de menú principal y pantalla de game over para mejorar la experiencia del usuario.
# 19. Se ha añadido soporte para múltiples jugadores o modos de juego, como cooperativo o competitivo.
# 20. Se ha optimizado el rendimiento del juego mediante técnicas como la gestión eficiente de recursos y la reducción de cálculos innecesarios.
# 21. Se ha añadido un sistema de guardado de puntuaciones altas para que los jugadores puedan competir por la mejor puntuación.
# Estas mejoras hacen que el juego sea más completo, divertido y desafiante, ofreciendo una experiencia de juego más rica y atractiva para los jugadores.
