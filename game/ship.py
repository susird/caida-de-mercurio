# game/ship.py
import random
import pygame
from config import MAP_ANCHO, MAP_ALTO, AZUL1, AZUL2, TURBULENCIA

# 🚤 Velocidades (mantengo las mismas variables y valores)
barco_vel = 2                 # normal
barco_vel_turbulencia = 1     # dentro de turbulencias
barco_vel_aceleron = 5        # cuando presiona espacio

def barco_en_agua(x, y, mapa):
    """Verifica si el centro del barco está en agua"""
    if 0 <= x < MAP_ANCHO and 0 <= y < MAP_ALTO:
        color = mapa.get_at((int(x), int(y)))
        return color[:3] in (AZUL1, AZUL2, TURBULENCIA)
    return False

def dentro_turbulencia(x, y, turbulencias):
    """Detecta si el barco está en una zona de turbulencia"""
    barco_rect = pygame.Rect(int(x-25), int(y-15), 50, 30)
    for t in turbulencias:
        if barco_rect.colliderect(t):
            return True
    return False

def encontrar_posicion_inicial(mapa):
    """Busca un punto válido en el agua"""
    while True:
        x = random.randint(200, MAP_ANCHO-200)
        y = random.randint(MAP_ALTO-800, MAP_ALTO-200)
        if barco_en_agua(x, y, mapa):
            return x, y
