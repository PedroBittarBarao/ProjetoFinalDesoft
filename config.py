# Arquivo com configurações e constantes
from os import path

#caminhos
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

#Janela
WIDTH = 400 # Largura 
HEIGHT = 600 # Altura 
FPS = 60 # Frames por segundo

#tamanhos
BLOCK_WIDTH=28
BLOCK_HEIGHT=14

#estados
INIT = 0
GAME = 1
QUIT = 2

