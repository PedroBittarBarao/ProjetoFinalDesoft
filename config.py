"""
Arquivo com configurações e constantes.
"""

from os import path

#Caminhos
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

#Janela
SW = 540 #Largura 
SH = 600 #Altura 
FPS = 60 #Frames por segundo

#Tamanhos
BALL_W = BALL_H = 8
BAT_W, BAT_H = (45, 13)
BLOCK_W, BLOCK_H = (45, 18)

#Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Estados
INIT = 0
GAME = 1
QUIT = 2

BALL_SPEEDX_0 = 4
BALL_SPEEDY_0 = -3

