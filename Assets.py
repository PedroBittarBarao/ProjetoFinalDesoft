# Arquivo para carregar assets
import pygame
import os
from config import BLOCK_WIDTH,BLOCK_HEIGHT,IMG_DIR,FNT_DIR,SND_DIR

BACKGROUND='background'
BLOCK_IMG_RED='block_img_red'
BLOCK_IMG_GRN='block_img_grn'
BLOCK_IMG_BLU='block_img_blu'
BLOCK_IMG_YLW='block_img_ylw'
SCORE_FONT='score_font'

def load_assets():
    assets={}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'Backgroud_Estrelas.png')).convert()
    assets[BLOCK_IMG_RED] = pygame.image.load(os.path.join(IMG_DIR, 'Bloco Vermelho.png')).convert()
    assets[BLOCK_IMG_GRN] = pygame.image.load(os.path.join(IMG_DIR, 'Bloco Verde.png')).convert()
    assets[BLOCK_IMG_BLU] = pygame.image.load(os.path.join(IMG_DIR, 'Bloco Azul.png')).convert()
    assets[BLOCK_IMG_YLW] = pygame.image.load(os.path.join(IMG_DIR, 'Bloco Amarelo.png')).convert()

    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'TBD'), 28)

    pygame.mixer.music.load(os.path.join(SND_DIR, 'TBD'))
    pygame.mixer.music.set_volume(0.4)

    return assets
    