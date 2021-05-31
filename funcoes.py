import pygame
import config
from config import WIDTH,HEIGHT, BLOCK_WIDTH,BLOCK_HEIGHT, BALL_WIDTH,BALL_HEIGHT, BAT_WIDTH,BAT_HEIGHT, BALL_POS_0, BAT_POS_0, BALL_SPEED_HOR_BASE,BALL_SPEED_VERT_BASE
from Assets import BACKGROUND, BAT_SOUND, BLOCK_IMG_RED,BLOCK_IMG_GRN,BLOCK_IMG_BLU,BLOCK_IMG_YLW, BALL_IMG, BAT_IMG, BLOCK_SOUND_1, GAME_FONT, PAREDE_SOUND, load_assets

BALL_POS = BALL_POS_0
BAT_POS = BAT_POS_0
BALL_SPEED_HOR = BALL_SPEED_HOR_BASE
BALL_SPEED_VERT = BALL_SPEED_VERT_BASE

block_positions={'1-1': (0, 0), '2-1': (30, 0), '3-1': (60, 0), '4-1': (90, 0), '5-1': (120, 0), '6-1': (150, 0), '7-1': (180, 0), '8-1': (210, 0), '9-1': (240, 0), '10-1': (270, 0),
'11-1': (300, 0), '12-1': (330, 0), '13-1': (360, 0), '14-1': (390, 0), '1-2': (0, 15), '2-2': (30, 15), '3-2': (60, 15), '4-2': (90, 15), '5-2': (120, 15), '6-2': (150, 15),
'7-2': (180, 15), '8-2': (210, 15), '9-2': (240, 15), '10-2': (270, 15), '11-2': (300, 15), '12-2': (330, 15), '13-2': (360, 15), '14-2': (390, 15), '1-3': (0, 30), '2-3': (30, 30),
'3-3': (60, 30), '4-3': (90, 30), '5-3': (120, 30), '6-3': (150, 30), '7-3': (180, 30), '8-3': (210, 30), '9-3': (240, 30), '10-3': (270, 30), '11-3': (300, 30), '12-3': (330, 30),
'13-3': (360, 30), '14-3': (390, 30), '1-4': (0, 45), '2-4': (30, 45), '3-4': (60, 45), '4-4': (90, 45), '5-4': (120, 45), '6-4': (150, 45), '7-4': (180, 45), '8-4': (210, 45),
'9-4': (240, 45), '10-4': (270, 45), '11-4': (300, 45), '12-4': (330, 45), '13-4': (360, 45), '14-4': (390, 45), '1-5': (0, 60), '2-5': (30, 60), '3-5': (60, 60), '4-5': (90, 60),
'5-5': (120, 60), '6-5': (150, 60), '7-5': (180, 60), '8-5': (210, 60), '9-5': (240, 60), '10-5': (270, 60), '11-5': (300, 60), '12-5': (330, 60), '13-5': (360, 60), '14-5': (390, 60)}
# posições espaciais dos blocos

keys_down = {}

def setup_bat(BAT_WIDTH,BAT_HEIGHT): #cria o 'bat'
    assets=load_assets()
    bat_img_rect=assets[BAT_IMG].get_rect(topleft=(BAT_POS_0))
    WINDOW.blit(assets[BAT_IMG],bat_img_rect)
    return bat_img_rect



def setup_blocks(): #cria os blocos
    assets=load_assets()
    blocks_rect={}
    block_keys=[]
    for block in block_positions.keys():
        block_img_blu_scale=pygame.transform.scale(assets[BLOCK_IMG_BLU], (BLOCK_WIDTH,BLOCK_HEIGHT))
    for block in block_positions.keys():
        block_keys.append(block)
        block_img_rect=block_img_blu_scale.get_rect(topleft=(block_positions[block][0],block_positions[block][1]))
        blocks_rect[block]=block_img_rect
        WINDOW.blit(block_img_blu_scale,block_img_rect)
    return [block_img_blu_scale,blocks_rect,block_keys]

def setup_ball(): # cria a bola
    assets=load_assets()
    ball_img_rect=assets[BALL_IMG].get_rect(topleft=(BALL_POS_0))
    WINDOW.blit(assets[BALL_IMG], ball_img_rect)
    current_speed_HOR=BALL_SPEED_HOR
    current_speed_VERT=BALL_SPEED_VERT
    return [[current_speed_HOR,current_speed_VERT],ball_img_rect]


def setup_window(): #puxa outras funções setup e cria a janela
    WINDOW.fill((255,255,255))
    assets=load_assets()
    WINDOW.blit(assets[BACKGROUND], (0, 0))
    bat_img_rect=setup_bat(BAT_WIDTH,BAT_HEIGHT)
    lista_current_speed=setup_ball()[0]
    ball_img_rect=setup_ball()[1]
    block_keys=setup_blocks()[2]
    block_rect=setup_blocks()[1]
    block_img_blu_scale=setup_blocks()[0]

    pygame.display.update()
    return [lista_current_speed,ball_img_rect,bat_img_rect,block_rect,block_img_blu_scale,block_keys]
    
def update_blocks(lista): # atualiza os blocos
    assets=load_assets()
    block_img_blu_scale=lista[0]
    blocks_rect=lista[1]
    block_keys=lista[2]
    for block in block_keys:
        if block in blocks_rect.keys() and BALL_POS[0]-block_positions[block][0]<=BLOCK_WIDTH and BALL_POS[0]-block_positions[block][0]>=0  and BALL_POS[1]-block_positions[block][1]<=BLOCK_HEIGHT and BALL_POS[1]-block_positions[block][1]>=0: #verifica condição de colisão entre bola e bloco
            blocks_rect.pop(block)
            pygame.mixer.Sound.play(assets[BLOCK_SOUND_1])
        elif block in blocks_rect.keys():
            block_img_rect=block_img_blu_scale.get_rect(topleft=(block_positions[block]))
            blocks_rect[block]=block_img_rect
            WINDOW.blit(block_img_blu_scale,block_img_rect)
    

def update_speed(lista_current_speed,ball_img_rect,bat_img_rect,blocks_rect,block_keys): #atualiza os valores de velocidade vertical e horizontal
    assets=load_assets()
    if BALL_POS[0]>WIDTH or BALL_POS[0]<0 :
        lista_current_speed[0]*=-1
        pygame.mixer.Sound.play(assets[PAREDE_SOUND])
    if BALL_POS[1]>HEIGHT-BALL_HEIGHT or BALL_POS[1]<(0+BALL_HEIGHT): # verifica condição de colidão entre bola e as bordas da janela
        lista_current_speed[1]*=-1
        pygame.mixer.Sound.play(assets[PAREDE_SOUND])
    if BALL_POS[0]-BAT_POS[0]<=BAT_WIDTH and BALL_POS[0]-BAT_POS[0]>=0 and BALL_POS[1]-BAT_POS[1]<=BAT_HEIGHT and BALL_POS[1]-BAT_POS[1]>=0: # verifica condição de colisão enre bola e 'bat'
        lista_current_speed[1]*=-1
        pygame.mixer.Sound.play(assets[BAT_SOUND])
        if BALL_POS[0]-BAT_POS[0]<=BAT_WIDTH/2 and BALL_POS[0]-BAT_POS[0]>=0:
            lista_current_speed[0]*=-1
    for block in block_keys:
        if block in blocks_rect.keys() and BALL_POS[0]-block_positions[block][0]<=BLOCK_WIDTH and BALL_POS[0]-block_positions[block][0]>=0  and BALL_POS[1]-block_positions[block][1]<=BLOCK_HEIGHT and BALL_POS[1]-block_positions[block][1]>=0: #verifica condição de colisão entre bola e bloco
            lista_current_speed[1]*=-1
    return lista_current_speed,block_keys, blocks_rect

def update_ball(event,speed_lista): # atualiza a posição da bola
    assets=load_assets()
    BALL_POS[0]+=speed_lista[0]
    BALL_POS[1]+=speed_lista[1]
    ball_img_rect=assets[BALL_IMG].get_rect(topleft=(BALL_POS))
    WINDOW.blit(assets[BALL_IMG],ball_img_rect)

def update_bat(BAT_POS,event): #atualiza a posição do 'bat'
    assets=load_assets()
    if event.type == pygame.KEYDOWN:
        keys_down[event.key] = True
        if event.key == pygame.K_LEFT and BAT_POS[0]>0:
           BAT_POS_0[0]-=20
        if event.key == pygame.K_RIGHT and BAT_POS[0]<(WIDTH-BAT_WIDTH):
            BAT_POS_0[0]+=20
    
    bat_img_rect=assets[BAT_IMG].get_rect(topleft=(BAT_POS))
    WINDOW.blit(assets[BAT_IMG], bat_img_rect)
    
    

WINDOW=pygame.display.set_mode((WIDTH,HEIGHT)) #configura a janela
