# Arquivo com configurações e constantes
from os import path

#caminhos
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

#Janela
WIDTH = 420 # Largura 
HEIGHT = 600 # Altura 
FPS = 60 # Frames por segundo

#tamanhos
BLOCK_WIDTH=28
BLOCK_HEIGHT=14
BALL_WIDTH=12
BALL_HEIGHT=12
BAT_WIDTH=50
BAT_HEIGHT=10

#estados
INIT = 0
GAME = 1
QUIT = 2

BAT_POS_0=[WIDTH/2-BLOCK_WIDTH,550]
