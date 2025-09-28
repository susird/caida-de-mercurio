import pygame
from config import ANCHO, ALTO
from game.assets import fondoInicio  # ⬅ Importamos la clase del fondo

# ==============================
# Función para renderizar texto con borde
# ==============================
def render_con_borde(texto, fuente, color_texto, color_borde):
    texto_surface = fuente.render(texto, True, color_texto)
    borde_surface = fuente.render(texto, True, color_borde)
    superficie = pygame.Surface((texto_surface.get_width() + 4, texto_surface.get_height() + 4), pygame.SRCALPHA)
    for dx, dy in [(-2,0),(2,0),(0,-2),(0,2), (-2,-2),(2,-2),(-2,2),(2,2)]:
        superficie.blit(borde_surface, (dx+2, dy+2))
    superficie.blit(texto_surface, (2, 2))
    return superficie

# ==============================
# Ventana de inicio
# ==============================
def ventana(ventana):
    CREMA = (255, 243, 196)
    NEGRO = (0, 0, 0)
    NARANJA = (255, 180, 70)

    # Aseguramos que el fondo esté cargado
    fondoInicio.load()

    # Dibujar fondo
    ventana.blit(fondoInicio.imagen, (fondoInicio.coord.x, fondoInicio.coord.y))

    # Fuente personalizada
    fuente_titulo = pygame.font.Font("fonts/VT323-Regular.ttf", 64)
    fuente_subtitulo = pygame.font.Font("fonts/VT323-Regular.ttf", 28)
    fuente_boton = pygame.font.Font("fonts/VT323-Regular.ttf", 36)

    # Render textos con borde
    texto_titulo = render_con_borde("CAÍDA DE MERCURIO", fuente_titulo, CREMA, NEGRO)
    texto_subtitulo = render_con_borde("Aventura en aguas envenenadas", fuente_subtitulo, CREMA, NEGRO)

    ventana.blit(texto_titulo, (ANCHO//2 - texto_titulo.get_width()//2, 80))
    ventana.blit(texto_subtitulo, (ANCHO//2 - texto_subtitulo.get_width()//2, 160))

    # Botón
    boton_ancho, boton_alto = 200, 60
    boton_x = ANCHO // 2 - boton_ancho // 2
    boton_y = ALTO - 150
    rect_boton = pygame.Rect(boton_x, boton_y, boton_ancho, boton_alto)

    pygame.draw.rect(ventana, NARANJA, rect_boton, border_radius=10)
    texto_boton = fuente_boton.render("JUGAR", True, NEGRO)
    ventana.blit(texto_boton, (rect_boton.centerx - texto_boton.get_width()//2,
                               rect_boton.centery - texto_boton.get_height()//2))

    return rect_boton  # Retornamos el rectángulo para detectar clic en main.py
