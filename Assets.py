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
BLOCK_SOUND_1='block_sound_1'
BLOCK_SOUND_2='block_sound_2'
PAREDE_SOUND='parede_SOUND'
BAT_SOUND='bat_sound'

def load_assets():
    
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'background.jpg')).convert()
    #PASSAR A CONVERSÃO DA ESCALA DOS BLOCOS PARA ESTE ARQUIVO
    assets[BLOCK_IMG_RED] = pygame.image.load(os.path.join(IMG_DIR, 'Bloco Vermelho.png')).convert()
    assets[BLOCK_IMG_GRN] = pygame.image.load(os.path.join(IMG_DIR, 'Bloco Verde.png')).convert()
    assets[BLOCK_IMG_BLU] = pygame.image.load(os.path.join(IMG_DIR, 'Bloco Azul.png')).convert()
    assets[BLOCK_IMG_YLW] = pygame.image.load(os.path.join(IMG_DIR, 'Bloco Amarelo.png')).convert()
    assets[BALL_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'ball_red.png')).convert_alpha()
    assets[BALL_IMG] = pygame.transform.scale(assets[BALL_IMG], (BALL_WIDTH,BALL_HEIGHT))
    assets[BAT_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'bat_blue.png')).convert()
    assets[BAT_IMG] = pygame.transform.scale(assets[BAT_IMG], (BAT_WIDTH,BAT_HEIGHT))
    assets[GAME_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'ArcadeNormal-ZDZ.ttf'), 28)
    #INCLUIR IMAGEM NA PASTA IMG
    assets[TITLE_SCREEN] = pygame.image.load(os.path.join(IMG_DIR, 'Title_screen_placeholder.png')).convert()
    assets[BLOCK_SOUND_1]=pygame.mixer.Sound(os.path.join(SND_DIR, 'block1.wav'))
    assets[BLOCK_SOUND_2]=pygame.mixer.Sound(os.path.join(SND_DIR, 'block2.wav'))
    assets[PAREDE_SOUND]=pygame.mixer.Sound(os.path.join(SND_DIR, 'parede.wav'))
    assets[BAT_SOUND]=pygame.mixer.Sound(os.path.join(SND_DIR, 'bat.wav'))
    pygame.mixer.music.set_volume(0.4)

    return assets
    