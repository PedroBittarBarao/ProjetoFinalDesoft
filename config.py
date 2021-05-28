#Arquivo com configurações e constantes
from os import path

#Caminhos
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

#Janela
WIDTH = 420 # Largura 
HEIGHT = 600 # Altura 
FPS = 60 # Frames por segundo

#Tamanhos
BLOCK_WIDTH=28
BLOCK_HEIGHT=14
BALL_WIDTH=8
BALL_HEIGHT=8
BAT_WIDTH=50
BAT_HEIGHT=10

#Estados
INIT = 0
GAME = 1
QUIT = 2

#Posições
BALL_POS_0 = [WIDTH/2-BLOCK_WIDTH,535] #posição inicial da bola(horizontal,vertical)
BAT_POS_0 = [WIDTH/2-BLOCK_WIDTH,550] #posição inicial 'bat'(horizontal,vertical)

#Velocidades iniciais da bola
BALL_SPEED_HOR_BASE = -10
BALL_SPEED_VERT_BASE = -10

