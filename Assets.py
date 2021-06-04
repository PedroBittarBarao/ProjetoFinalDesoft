#Arquivo para carregar assets
import pygame
import os
from config import BALL_W, BALL_H,   BAT_W, BAT_H,   BLOCK_W, BLOCK_H,   IMG_DIR, SND_DIR, FNT_DIR

TITLE_SCREEN='title_screen'
GAME_OVER='game_over'
BACKGROUND='background'

BALL_IMG='ball_img'
BAT_IMG='bat_img'
BLOCK_IMG_RED='block_img_red'
BLOCK_IMG_GRN='block_img_grn'
BLOCK_IMG_BLU='block_img_blu'
BLOCK_IMG_YLW='block_img_ylw'

WALL_SND='wall_SND'
BAT_SND='bat_snd'
BLOCK_SND_1='block_snd_1'
BLOCK_SND_2='block_snd_2'

GAME_FNT='game_fnt'

def load_assets():
    
    assets = {}
    
    #Imagens
    assets[TITLE_SCREEN] = pygame.image.load(os.path.join(IMG_DIR, 'Title_screen_placeholder.png')).convert()
    assets[GAME_OVER]= pygame.image.load(os.path.join(IMG_DIR, 'game_over_placeholder.png')).convert()
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'background.jpg')).convert()
    
    assets[BALL_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'ball_red.png')).convert_alpha()
    assets[BALL_IMG] = pygame.transform.scale(assets[BALL_IMG], (BALL_W, BALL_H))
    assets[BAT_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'bat_blue.png')).convert()
    assets[BAT_IMG] = pygame.transform.scale(assets[BAT_IMG], (BAT_W, BAT_H))

    assets[BLOCK_IMG_RED] = pygame.image.load(os.path.join(IMG_DIR, 'Bloco Vermelho.png')).convert()
    assets[BLOCK_IMG_RED] = pygame.transform.scale(assets[BLOCK_IMG_RED], (BLOCK_W, BLOCK_H))
    assets[BLOCK_IMG_GRN] = pygame.image.load(os.path.join(IMG_DIR, 'Bloco Verde.png')).convert()
    assets[BLOCK_IMG_GRN] = pygame.transform.scale(assets[BLOCK_IMG_GRN], (BLOCK_W, BLOCK_H))
    assets[BLOCK_IMG_BLU] = pygame.image.load(os.path.join(IMG_DIR, 'Bloco Azul.png')).convert()
    assets[BLOCK_IMG_BLU] = pygame.transform.scale(assets[BLOCK_IMG_BLU], (BLOCK_W, BLOCK_H))
    assets[BLOCK_IMG_YLW] = pygame.image.load(os.path.join(IMG_DIR, 'Bloco Amarelo.png')).convert()
    assets[BLOCK_IMG_YLW] = pygame.transform.scale(assets[BLOCK_IMG_YLW], (BLOCK_W, BLOCK_H))    

    #Efeitos sonoros
    assets[WALL_SND]=pygame.mixer.Sound(os.path.join(SND_DIR, 'parede.wav'))
    assets[BAT_SND]=pygame.mixer.Sound(os.path.join(SND_DIR, 'bat.wav'))
    assets[BLOCK_SND_1]=pygame.mixer.Sound(os.path.join(SND_DIR, 'block1.wav'))
    assets[BLOCK_SND_2]=pygame.mixer.Sound(os.path.join(SND_DIR, 'block2.wav'))
    pygame.mixer.music.set_volume(0.4)

    #Fontes
    assets[GAME_FNT] = pygame.font.Font(os.path.join(FNT_DIR, 'ArcadeNormal-ZDZ.ttf'), 20)

    return assets
    