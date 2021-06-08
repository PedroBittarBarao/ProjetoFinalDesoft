# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import SW, SH, INIT, GAME, QUIT
from init_screen import init_screen
from game_screen import game_screen
from end_screen import end_screen

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((SW, SH))
pygame.display.set_caption('Breakout')


state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    elif state == QUIT:
        state = end_screen(window)

# ===== Finalização =====
pygame.quit()

