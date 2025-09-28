import pygame, sys, random

pygame.init()
WIDTH, HEIGHT = 800, 600   # ventana
MAP_WIDTH, MAP_HEIGHT = 8000, 8000  # mapa grande
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Río con Selva y Turbulencias")
clock = pygame.time.Clock()

# Colores
AZUL1 = (30, 144, 255)   # azul claro
AZUL2 = (20, 100, 200)   # azul oscuro
VERDE = (34, 139, 34)
SELVAS = [(0, 120, 0), (0, 100, 0), (0, 150, 50)]  # tonos de verde
TURBULENCIA = (0, 60, 120)

# Crear mapa base (verde = tierra)
mapa = pygame.Surface((MAP_WIDTH, MAP_HEIGHT))
mapa.fill(VERDE)

# Selva: árboles pequeños
for _ in range(5000):
    x = random.randint(0, MAP_WIDTH)
    y = random.randint(0, MAP_HEIGHT)
    radio = random.randint(5, 12)
    color_selva = random.choice(SELVAS)
    pygame.draw.circle(mapa, color_selva, (x, y), radio)

# Lista de turbulencias
turbulencias = []

# Dibujar río principal
centro = MAP_WIDTH // 2
ancho_rio = 300
y = 0
while y < MAP_HEIGHT:
    dx = random.choice([-150, -100, -50, 0, 50, 100, 150])
    centro = max(200, min(MAP_WIDTH-200, centro+dx))
    color_agua = random.choice([AZUL1, AZUL2])

    pygame.draw.circle(mapa, color_agua, (centro, y), ancho_rio//2)
    pygame.draw.circle(mapa, color_agua, (centro, y+200), ancho_rio//2)
    pygame.draw.rect(mapa, color_agua, (centro-ancho_rio//2, y, ancho_rio, 200))

    # Turbulencias
    if random.random() < 0.25:
        t_x = centro + random.randint(-100, 100)
        t_y = y + random.randint(50, 250)
        radio = random.randint(60, 120)
        pygame.draw.circle(mapa, TURBULENCIA, (t_x, t_y), radio)
        turbulencias.append(pygame.Rect(t_x-radio, t_y-radio, radio*2, radio*2))

    y += 200

# --- Cargar imágenes del navegante ---
try:
    navegante_rio1 = pygame.image.load("navegante_rio1.png").convert_alpha()
    navegante_rio2 = pygame.image.load("navegante_rio2.png").convert_alpha()
    navegante_rio1 = pygame.transform.scale(navegante_rio1, (90, 70))
    navegante_rio2 = pygame.transform.scale(navegante_rio2, (90, 70))
    print(" Navegantes cargados correctamente")
except Exception as e:
    print(" Error al cargar navegantes:", e)
    sys.exit()

imagenes_navegante = [navegante_rio1, navegante_rio2]
frame = 0  # control de animación

# 🚤 Velocidades
barco_vel = 2                 # normal
barco_vel_turbulencia = 1     # dentro de turbulencias
barco_vel_aceleron = 5        # cuando presiona espacio

def barco_en_agua(x, y):
    """Verifica si el centro del barco está en agua"""
    if 0 <= x < MAP_WIDTH and 0 <= y < MAP_HEIGHT:
        color = mapa.get_at((int(x), int(y)))
        return color[:3] in (AZUL1, AZUL2, TURBULENCIA)
    return False

def dentro_turbulencia(x, y):
    """Detecta si el barco está en una zona de turbulencia"""
    barco_rect = pygame.Rect(int(x-25), int(y-15), 50, 30)
    for t in turbulencias:
        if barco_rect.colliderect(t):
            return True
    return False

def encontrar_posicion_inicial():
    """Busca un punto válido en el agua"""
    while True:
        x = random.randint(200, MAP_WIDTH-200)
        y = random.randint(MAP_HEIGHT-800, MAP_HEIGHT-200)
        if barco_en_agua(x, y):
            return x, y

barco_x, barco_y = encontrar_posicion_inicial()

def main():
    global barco_x, barco_y, frame
    running = True
    contador_anim = 0  # control de cambio de sprite

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
        if dentro_turbulencia(barco_x, barco_y):
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

        if barco_en_agua(nuevo_x, nuevo_y):
            barco_x, barco_y = nuevo_x, nuevo_y

        # Animación (si se mueve alterna entre imágenes)
        if movio:
            contador_anim += 1
            if contador_anim % 10 == 0:  # cambia cada 10 frames
                frame = (frame + 1) % 2

        # Cámara
        cam_x = barco_x - WIDTH // 2
        cam_y = barco_y - HEIGHT // 2
        cam_x = max(0, min(MAP_WIDTH-WIDTH, cam_x))
        cam_y = max(0, min(MAP_HEIGHT-HEIGHT, cam_y))

        # Dibujar
        screen.blit(mapa, (-cam_x, -cam_y))
        screen.blit(imagenes_navegante[frame], 
                    (barco_x - cam_x - navegante_rio1.get_width()//2,
                     barco_y - cam_y - navegante_rio1.get_height()//2))

        pygame.display.flip()
        clock.tick(60)  



    pygame.quit()
    sys.exit()

main()
