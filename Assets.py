#Arquivo para carregar assets
import pygame
import os
from config import BLOCK_WIDTH,BLOCK_HEIGHT, BALL_WIDTH,BALL_HEIGHT, BAT_WIDTH,BAT_HEIGHT, IMG_DIR,SND_DIR,FNT_DIR

BACKGROUND='background'
BLOCK_IMG_RED='block_img_red'
BLOCK_IMG_GRN='block_img_grn'
BLOCK_IMG_BLU='block_img_blu'
BLOCK_IMG_YLW='block_img_ylw'
BALL_IMG='ball_img'
BAT_IMG='bat_img'
GAME_FONT='game_font'
TITLE_SCREEN='title_screen'

def load_assets():
    
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'background.jpg')).convert()
    assets[BLOCK_IMG_RED] = pygame.image.load(os.path.join(IMG_DIR, 'Bloco Vermelho.png')).convert()
    assets[BLOCK_IMG_GRN] = pygame.image.load(os.path.join(IMG_DIR, 'Bloco Verde.png')).convert()
    assets[BLOCK_IMG_BLU] = pygame.image.load(os.path.join(IMG_DIR, 'Bloco Azul.png')).convert()
    assets[BLOCK_IMG_YLW] = pygame.image.load(os.path.join(IMG_DIR, 'Bloco Amarelo.png')).convert()
    assets[BALL_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'ball_red.png')).convert()
    assets[BAT_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'bat_blue.png')).convert()
    assets[GAME_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'ArcadeNormal-ZDZ.ttf'), 28)
    #INCLUIR IMAGEM NA PASTA IMG
    assets[TITLE_SCREEN] = pygame.image.load(os.path.join(IMG_DIR, 'Title_screen_placeholder.png')).convert()
    
    #pygame.mixer.music.load(os.path.join(SND_DIR, 'TBD'))
    #pygame.mixer.music.set_volume(0.4)

    return assets
    