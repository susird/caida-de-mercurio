# game/mapgen.py
import pygame
import random
from config import MAP_ANCHO, MAP_ALTO, VERDE, SELVAS, AZUL1, AZUL2, TURBULENCIA

def generate_map():
    """Genera y devuelve (mapa, turbulencias) tal como en el archivo original."""
    mapa = pygame.Surface((MAP_ANCHO, MAP_ALTO))
    mapa.fill(VERDE)

    # Selva: árboles pequeños (igual que el original)
    for _ in range(5000):
        x = random.randint(0, MAP_ANCHO)
        y = random.randint(0, MAP_ALTO)
        radio = random.randint(5, 12)
        color_selva = random.choice(SELVAS)
        pygame.draw.circle(mapa, color_selva, (x, y), radio)

    turbulencias = []

    # Dibujar río principal y posibles turbulencias
    centro = MAP_ANCHO // 2
    ancho_rio = 300
    y = 0
    while y < MAP_ALTO:
        dx = random.choice([-150, -100, -50, 0, 50, 100, 150])
        centro = max(200, min(MAP_ANCHO - 200, centro + dx))
        color_agua = random.choice([AZUL1, AZUL2])

        pygame.draw.circle(mapa, color_agua, (centro, y), ancho_rio // 2)
        pygame.draw.circle(mapa, color_agua, (centro, y + 200), ancho_rio // 2)
        pygame.draw.rect(mapa, color_agua, (centro - ancho_rio // 2, y, ancho_rio, 200))

        # Turbulencias (misma probabilidad y tamaño que el original)
        if random.random() < 0.25:
            t_x = centro + random.randint(-100, 100)
            t_y = y + random.randint(50, 250)
            radio = random.randint(60, 120)
            pygame.draw.circle(mapa, TURBULENCIA, (t_x, t_y), radio)
            turbulencias.append(pygame.Rect(t_x - radio, t_y - radio, radio * 2, radio * 2))

        y += 200

    return mapa, turbulencias
