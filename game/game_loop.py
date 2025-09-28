# game/game_loop.py
import pygame
import sys
import random

from config import ANCHO, ALTO, MAP_ANCHO, MAP_ALTO
from game.mapgen import generate_map
from game.assets import load_navegantes
from game.ship import (
    barco_en_agua,
    dentro_turbulencia,
    encontrar_posicion_inicial,
    barco_vel,
    barco_vel_turbulencia,
    barco_vel_aceleron,
)

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Río con Selva y Turbulencias")
    clock = pygame.time.Clock()

    # Generar mapa y turbulencias (misma lógica que antes)
    mapa, turbulencias = generate_map()

    # Cargar imágenes
    imagenes_navegante, navegante_rio1 = load_navegantes()

    # Estado inicial del barco
    barco_x, barco_y = encontrar_posicion_inicial(mapa)
    frame = 0
    contador_anim = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        vel_actual = barco_vel
        nuevo_x, nuevo_y = barco_x, barco_y

        # Detectar teclas
        keys = pygame.key.get_pressed()

        # 🚀 Acelerón con ESPACIO
        if keys[pygame.K_SPACE]:
            vel_actual = barco_vel_aceleron

        # Efecto de turbulencia (siempre más lento en turbulencia)
        if dentro_turbulencia(barco_x, barco_y, turbulencias):
            vel_actual = barco_vel_turbulencia
            nuevo_x += random.choice([-1, 0, 1])
            nuevo_y += random.choice([-1, 0, 1])

        # Movimiento del barco
        movio = False
        if keys[pygame.K_LEFT]:
            nuevo_x -= vel_actual
            movio = True
        if keys[pygame.K_RIGHT]:
            nuevo_x += vel_actual
            movio = True
        if keys[pygame.K_UP]:
            nuevo_y -= vel_actual
            movio = True
        if keys[pygame.K_DOWN]:
            nuevo_y += vel_actual
            movio = True

        if barco_en_agua(nuevo_x, nuevo_y, mapa):
            barco_x, barco_y = nuevo_x, nuevo_y

        # Animación (si se mueve alterna entre imágenes)
        if movio:
            contador_anim += 1
            if contador_anim % 10 == 0:  # cambia cada 10 frames
                frame = (frame + 1) % 2

        # Cámara
        cam_x = barco_x - ANCHO // 2
        cam_y = barco_y - ALTO // 2
        cam_x = max(0, min(MAP_ANCHO - ANCHO, cam_x))
        cam_y = max(0, min(MAP_ALTO - ALTO, cam_y))

        # Dibujar
        screen.blit(mapa, (-cam_x, -cam_y))
        screen.blit(
            imagenes_navegante[frame],
            (
                barco_x - cam_x - navegante_rio1.get_width() // 2,
                barco_y - cam_y - navegante_rio1.get_height() // 2,
            ),
        )

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
