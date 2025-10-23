import pygame, sys
from config import ANCHO, ALTO
from ventanas.ventana import ventana
from game.game_loop import run_game

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Caída de Mercurio")

    clock = pygame.time.Clock()

    # Pantalla de inicio
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Dibujar la ventana y obtener el rectángulo del botón
        rect_boton = ventana(pantalla)
        pygame.display.flip()
        clock.tick(60)

        # Detectar clic sobre el botón "JUGAR"
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if rect_boton.collidepoint(evento.pos):
                esperando = False  # Salimos de la pantalla de inicio

    # Aquí empieza el juego normal
    run_game()
