#Arquivo com configurações e constantes
from os import path

#Caminhos
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

#Janela
SW = 420 #Largura 
SH = 600 #Altura 
FPS = 60 #Frames por segundo

#Tamanhos
BALL_W = BALL_H = 8
BAT_W, BAT_H = (75, 10)
BLOCK_W, BLOCK_H = (28, 14)

#Estados
INIT = 0
GAME = 1
QUIT = 2



#Posições
BALL_POS_0 = [SW/2 - BLOCK_W, 535] #posição inicial da bola(horizontal,vertical)
BAT_POS_0 = [SW/2 - BAT_W, 550] #posição inicial 'bat'(horizontal,vertical)

#Velocidades iniciais da bola
BALL_SPEED_HOR_BASE = -14
BALL_SPEED_VERT_BASE = -15

