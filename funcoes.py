import pygame
import config
from config import BLOCK_HEIGHT,BLOCK_WIDTH, WIDTH
import Assets
from Assets import BAT_IMG, load_assets,GAME_FONT,BACKGROUND,BAT_HEIGHT,BAT_WIDTH,BLOCK_IMG_BLU,BLOCK_IMG_YLW,BLOCK_IMG_GRN,BLOCK_IMG_RED

BAT_POS=config.BAT_POS_0
keys_down = {}
def setup_bat(BAT_WIDTH,BAT_HEIGHT):
    assets=load_assets()
    bat_img_scale=pygame.transform.scale(assets[BAT_IMG], (BAT_WIDTH,BAT_HEIGHT))
    WINDOW.blit(bat_img_scale, BAT_POS)

def update_bat(BAT_POS_0,event):
    assets=load_assets()
    if event.type == pygame.KEYDOWN:
        keys_down[event.key] = True
        if event.key == pygame.K_LEFT and BAT_POS_0[0]>0:
           BAT_POS_0[0]-=15
        if event.key == pygame.K_RIGHT and BAT_POS_0[0]<(WIDTH-BAT_WIDTH):
            BAT_POS_0[0]+=15
    if event.type == pygame.KEYUP:
        if event.key in keys_down and keys_down[event.key]:
            if event.key == pygame.K_LEFT and BAT_POS_0[0]>0 :
                BAT_POS_0[0]-=15
            if event.key == pygame.K_RIGHT and BAT_POS_0[0]<(WIDTH-BAT_WIDTH): 
                BAT_POS_0[0]+=15
    bat_img_scale=pygame.transform.scale(assets[BAT_IMG], (BAT_WIDTH,BAT_HEIGHT))
    WINDOW.blit(bat_img_scale, config.BAT_POS_0)

block_positions={'1-1':(0,0),'1-2':(30,0),'1-3':(60,0),'1-4':(90,0),'1-5':(120,0),'1-6':(150,0),'1-7':(180,0),'1-8':(210,0),'1-9':(240,0),'1-10':(270,0),'1-11':(300,0),'1-12':(330,0),'1-13':(360,0),'1-14':(390,0)}


def setup_blocks():
    assets=load_assets()
    block_real={}
    for block in block_positions.keys():
        block_real[block]=True
    block_img_blu_scale=pygame.transform.scale(assets[BLOCK_IMG_BLU], (BLOCK_WIDTH,BLOCK_HEIGHT))
    for block in block_positions.values():
        WINDOW.blit(block_img_blu_scale, block)
    
    
    return [block_img_blu_scale,block_real]

def update_blocks(lista):
    block_img_blu_scale=lista[0]
    block_real=lista[1]
    for block in block_positions.keys():
        if block_real[block]==True:
            WINDOW.blit(block_img_blu_scale,block_positions[block])
    


def setup_window():
    WINDOW.fill((255,255,255))
    assets=load_assets()
    WINDOW.blit(assets[BACKGROUND], (0, 0))
    setup_bat(BAT_WIDTH,BAT_HEIGHT)
    pygame.display.update()
    

WINDOW=pygame.display.set_mode((config.WIDTH,config.HEIGHT))
