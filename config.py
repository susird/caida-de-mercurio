# config.py
import os

import pygame

BASE_DIR = os.path.dirname(__file__)
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

ANCHO = 800
ALTO = 600
MAP_ANCHO = 8000
MAP_ALTO = 8000

# Colores
AZUL1 = (30, 144, 255)   # azul claro
AZUL2 = (20, 100, 200)   # azul oscuro
VERDE = (34, 139, 34)
SELVAS = [(0, 120, 0), (0, 100, 0), (0, 150, 50)]
TURBULENCIA = (0, 60, 120)

# Nombres de archivos en assets/
NAVEGANTE_1 = "navegante_rio1.png"
NAVEGANTE_2 = "navegante_rio2.png"
VECTOR = pygame.math.Vector2 
