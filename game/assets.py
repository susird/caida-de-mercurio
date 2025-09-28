import os
import pygame
from config import ANCHO, ALTO

# ==============================
# Clase del fondo
# ==============================
class fondoInicio:
    size = pygame.Vector2(ANCHO, ALTO)
    coord = pygame.Vector2(0, 0)
    imagen = None  # No cargamos aún
    posicion = 0

    @classmethod
    def load(cls):
        """Carga la imagen del fondo después de inicializar pygame.display."""
        if cls.imagen is None:
            # Construir ruta absoluta a assets
            base_path = os.path.dirname(os.path.dirname(__file__))  # sube de game/ a raíz del proyecto
            archivo = os.path.join(base_path, "assets", "fondo_pixelado.png")
            if not os.path.exists(archivo):
                raise FileNotFoundError(f"No se encontró el archivo de fondo: {archivo}")

            # Cargamos y escalamos
            cls.imagen = pygame.transform.scale(
                pygame.image.load(archivo).convert_alpha(),
                (int(cls.size.x), int(cls.size.y))
            )

# ==============================
# Función para cargar navegantes
# ==============================
def load_navegantes():
    """Carga las imágenes del navegante y devuelve (lista_de_frames, primer_frame)."""
    base_path = os.path.dirname(os.path.dirname(__file__))
    ruta1 = os.path.join(base_path, "assets", "navegante_rio1.png")
    ruta2 = os.path.join(base_path, "assets", "navegante_rio2.png")

    if not os.path.exists(ruta1) or not os.path.exists(ruta2):
        raise FileNotFoundError("No se encontraron las imágenes de navegantes en /assets/")

    img1 = pygame.image.load(ruta1).convert_alpha()
    img2 = pygame.image.load(ruta2).convert_alpha()

    # 🔹 Escalar las imágenes al tamaño deseado
    ANCHO_NAVEGANTE, ALTO_NAVEGANTE = 90, 70
    img1 = pygame.transform.scale(img1, (ANCHO_NAVEGANTE, ALTO_NAVEGANTE))
    img2 = pygame.transform.scale(img2, (ANCHO_NAVEGANTE, ALTO_NAVEGANTE))

    return [img1, img2], img1
