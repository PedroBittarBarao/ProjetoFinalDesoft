"""
Autores: Pedro Barão e Mia Machado.
Arquivo principal do jogo - rode-o para jogar 'Breakout'.

Aqui importamos todas as telas do jogo, ordenando elas dentro de um laço condicional (while state !== QUIT: ...)
Também importamos as dimensões da tela e os estados do jogo diretamente do arquivo config.py (configurações do jogo).

O módulo pygame é inicializado; a janela é criada; o estado inicial de jogo é estabelecido e um laço de repetição define a execução do jogo; o módulo pygame é finalizado. 
"""

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
        """
        if state == GAME:
            state = game_screen(window)
        """

# ===== Finalização =====
pygame.quit()

