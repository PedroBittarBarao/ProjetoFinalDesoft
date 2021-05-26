import pygame
import config
from config import BALL_POS_0,BLOCK_HEIGHT,BLOCK_WIDTH, HEIGHT, WIDTH
import Assets
from Assets import BAT_IMG, load_assets,GAME_FONT,BACKGROUND,BAT_HEIGHT,BAT_WIDTH,BLOCK_IMG_BLU,BLOCK_IMG_YLW,BLOCK_IMG_GRN,BLOCK_IMG_RED,BALL_HEIGHT,BALL_WIDTH,BALL_IMG

BAT_POS=config.BAT_POS_0
BALL_POS=BALL_POS_0
BALL_SPEED_VERT=config.BALL_SPEED_VERT_BASE
BALL_SPEED_HOR=config.BALL_SPEED_HOR_BASE

block_positions={'1-1':(0,0),'1-2':(30,0),'1-3':(60,0),'1-4':(90,0),'1-5':(120,0),'1-6':(150,0),'1-7':(180,0),'1-8':(210,0),'1-9':(240,0),
'1-10':(270,0),'1-11':(300,0),'1-12':(330,0),'1-13':(360,0),'1-14':(390,0)} # posições espaciais dos blocos

keys_down = {}

def setup_bat(BAT_WIDTH,BAT_HEIGHT): #cria o 'bat'
    assets=load_assets()
    bat_img_scale=pygame.transform.scale(assets[BAT_IMG], (BAT_WIDTH,BAT_HEIGHT))
    WINDOW.blit(bat_img_scale, BAT_POS)



def setup_blocks(): #cria os blocos
    assets=load_assets()
    block_real={}
    for block in block_positions.keys():
        block_real[block]=True
    block_img_blu_scale=pygame.transform.scale(assets[BLOCK_IMG_BLU], (BLOCK_WIDTH,BLOCK_HEIGHT))
    for block in block_positions.values():
        WINDOW.blit(block_img_blu_scale, block)
    return [block_img_blu_scale,block_real]

def setup_ball(): # cria a bola
    assets=load_assets()
    ball_img_scale=pygame.transform.scale(assets[BALL_IMG], (BALL_WIDTH,BALL_HEIGHT))
    WINDOW.blit(ball_img_scale, BALL_POS)
    current_speed_HOR=BALL_SPEED_HOR
    current_speed_VERT=BALL_SPEED_VERT
    return [current_speed_HOR,current_speed_VERT]


def setup_window(): #puxa outras funções setup e cria a janela
    WINDOW.fill((255,255,255))
    assets=load_assets()
    WINDOW.blit(assets[BACKGROUND], (0, 0))
    setup_bat(BAT_WIDTH,BAT_HEIGHT)
    lista_current_speed=setup_ball()
    pygame.display.update()
    return lista_current_speed
    
def update_blocks(lista): # atualiza os blocos
    block_img_blu_scale=lista[0]
    block_real=lista[1]
    for block in block_positions.keys():
        if block_real[block]==True:
            WINDOW.blit(block_img_blu_scale,block_positions[block])
    

def update_speed(lista_current_speed): #atualiza os valores de velocidade vertical e horizontal
    if BALL_POS[0]>WIDTH or BALL_POS[0]<0 :
        lista_current_speed[0]*=-1
    if BALL_POS[1]>HEIGHT-BALL_HEIGHT or BALL_POS[1]<(0+BALL_HEIGHT):
        lista_current_speed[1]*=-1
    return lista_current_speed

def update_ball(event,speed_lista): # atualiza a posição da bola
    assets=load_assets()
    ball_img_scale=pygame.transform.scale(assets[BALL_IMG], (BALL_WIDTH,BALL_HEIGHT))
    BALL_POS[0]+=speed_lista[0]
    BALL_POS[1]+=speed_lista[1]
    WINDOW.blit(ball_img_scale, (BALL_POS[0],BALL_POS[1]))

def update_bat(BAT_POS_0,event): #atualiza a posição do 'bat'
    assets=load_assets()
    if event.type == pygame.KEYDOWN:
        keys_down[event.key] = True
        if event.key == pygame.K_LEFT and BAT_POS_0[0]>0:
           BAT_POS_0[0]-=15
        if event.key == pygame.K_RIGHT and BAT_POS_0[0]<(WIDTH-BAT_WIDTH):
            BAT_POS_0[0]+=15
    
    bat_img_scale=pygame.transform.scale(assets[BAT_IMG], (BAT_WIDTH,BAT_HEIGHT))
    WINDOW.blit(bat_img_scale, config.BAT_POS_0)
    
    

WINDOW=pygame.display.set_mode((config.WIDTH,config.HEIGHT)) #configura a janela
