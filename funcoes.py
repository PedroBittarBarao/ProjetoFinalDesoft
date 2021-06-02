import pygame
import config
from config import WIDTH,HEIGHT, BLOCK_WIDTH,BLOCK_HEIGHT, BALL_WIDTH,BALL_HEIGHT, BAT_WIDTH,BAT_HEIGHT, BALL_POS_0, BAT_POS_0, BALL_SPEED_HOR_BASE,BALL_SPEED_VERT_BASE
from Assets import BACKGROUND, BAT_SOUND, BLOCK_IMG_RED,BLOCK_IMG_GRN,BLOCK_IMG_BLU,BLOCK_IMG_YLW, BALL_IMG, BAT_IMG, BLOCK_SOUND_1, GAME_FONT, GAME_OVER, PAREDE_SOUND, TITLE_SCREEN, load_assets

BALL_POS = BALL_POS_0 # armazena as posições (horizontal e vertical) da bola
BAT_POS = BAT_POS_0 # armazena as posições (horizontal e vertical) do 'bat'
BALL_SPEED_HOR = BALL_SPEED_HOR_BASE # armazena a velocidade horizontal da bola
BALL_SPEED_VERT = BALL_SPEED_VERT_BASE # armazena a velocidade vertical da bola

block_positions={'1-1': (0, 0), '2-1': (30, 0), '3-1': (60, 0), '4-1': (90, 0), '5-1': (120, 0), '6-1': (150, 0), '7-1': (180, 0), '8-1': (210, 0), '9-1': (240, 0), '10-1': (270, 0),
 '11-1': (300, 0), '12-1': (330, 0), '13-1': (360, 0), '14-1': (390, 0), '1-2': (0, 15), '2-2': (30, 15), '3-2': (60, 15), '4-2': (90, 15), '5-2': (120, 15), '6-2': (150, 15),
 '7-2': (180, 15), '8-2': (210, 15), '9-2': (240, 15), '10-2': (270, 15), '11-2': (300, 15), '12-2': (330, 15), '13-2': (360, 15), '14-2': (390, 15), '1-3': (0, 30), '2-3': (30, 30),
 '3-3': (60, 30), '4-3': (90, 30), '5-3': (120, 30), '6-3': (150, 30), '7-3': (180, 30), '8-3': (210, 30), '9-3': (240, 30), '10-3': (270, 30), '11-3': (300, 30), '12-3': (330, 30),
 '13-3': (360, 30), '14-3': (390, 30), '1-4': (0, 45), '2-4': (30, 45), '3-4': (60, 45), '4-4': (90, 45), '5-4': (120, 45), '6-4': (150, 45), '7-4': (180, 45), '8-4': (210, 45),
 '9-4': (240, 45), '10-4': (270, 45), '11-4': (300, 45), '12-4': (330, 45), '13-4': (360, 45), '14-4': (390, 45), '1-5': (0, 60), '2-5': (30, 60), '3-5': (60, 60), '4-5': (90, 60),
 '5-5': (120, 60), '6-5': (150, 60), '7-5': (180, 60), '8-5': (210, 60), '9-5': (240, 60), '10-5': (270, 60), '11-5': (300, 60), '12-5': (330, 60), '13-5': (360, 60), '14-5': (390, 60), '1-6': (0, 75), '2-6': (30, 75), '3-6': (60, 75), '4-6': (90, 75), '5-6': (120, 75), '6-6': (150, 75), '7-6': (180, 75), 
'8-6': (210, 75), '9-6': (240, 75), '10-6': (270, 75), '11-6': (300, 75), '12-6': (330, 75), '13-6': (360, 75), '14-6': (390, 75), '1-7': (0, 90), '2-7': (30, 90), '3-7': (60, 90),
'4-7': (90, 90), '5-7': (120, 90), '6-7': (150, 90), '7-7': (180, 90), '8-7': (210, 90), '9-7': (240, 90), '10-7': (270, 90), '11-7': (300, 90), '12-7': (330, 90), '13-7': (360, 90),
'14-7': (390, 90), '1-8': (0, 105), '2-8': (30, 105), '3-8': (60, 105), '4-8': (90, 105), '5-8': (120, 105), '6-8': (150, 105), '7-8': (180, 105), '8-8': (210, 105), '9-8': (240, 105),
'10-8': (270, 105), '11-8': (300, 105), '12-8': (330, 105), '13-8': (360, 105), '14-8': (390, 105), '1-9': (0, 120), '2-9': (30, 120), '3-9': (60, 120), '4-9': (90, 120),
'5-9': (120, 120), '6-9': (150, 120), '7-9': (180, 120), '8-9': (210, 120), '9-9': (240, 120), '10-9': (270, 120), '11-9': (300, 120), '12-9': (330, 120), '13-9': (360, 120),
'14-9': (390, 120), '1-10': (0, 135), '2-10': (30, 135), '3-10': (60, 135), '4-10': (90, 135), '5-10': (120, 135), '6-10': (150, 135), '7-10': (180, 135), '8-10': (210, 135),
'9-10': (240, 135), '10-10': (270, 135), '11-10': (300, 135), '12-10': (330, 135), '13-10': (360, 135), '14-10': (390, 135)}
# posições espaciais dos blocos

keys_down = {}


def setup_bat(BAT_WIDTH,BAT_HEIGHT): #cria o 'bat'
    assets=load_assets()
    bat_img_rect=assets[BAT_IMG].get_rect(topleft=(BAT_POS_0)) # cria um retângulo a partir da imagem e posição do 'bat'
    WINDOW.blit(assets[BAT_IMG],bat_img_rect) #desenha o bat

    return bat_img_rect 



def setup_blocks(): #cria os blocos
    assets=load_assets()
    blocks_rect={} # dicionário com valores sendo os retângulos criados
    block_keys=[]#lista com as chaves de TODOS os block

    for block in block_positions.keys():
        block_img_blu_scale=pygame.transform.scale(assets[BLOCK_IMG_BLU], (BLOCK_WIDTH,BLOCK_HEIGHT)) # cria uma imagem em escada dos blocos

    for block in block_positions.keys():
        block_keys.append(block) # adiciona a chave do bloco à lista de chaves
        block_img_rect = block_img_blu_scale.get_rect(topleft=(block_positions[block][0],block_positions[block][1])) # cria um retângulo a partir da imagem block_img_blu_scale
        blocks_rect[block]=block_img_rect #adiciona o retângulo ao dicionário de retângulos

        WINDOW.blit(block_img_blu_scale,block_img_rect)# desenha o bloco

    return [block_img_blu_scale,blocks_rect,block_keys]

def setup_ball(): # cria a bola
    assets=load_assets()

    ball_img_rect=assets[BALL_IMG].get_rect(topleft=(BALL_POS_0)) # cria um retângulo a partir da imagem da bola

    WINDOW.blit(assets[BALL_IMG], ball_img_rect) # desenha a bola

    return ball_img_rect


def setup_window(): #puxa outras funções setup e cria a janela
    WINDOW.fill((255,255,255))

    assets=load_assets()
    WINDOW.blit(assets[BACKGROUND], (0, 0))

    bat_img_rect=setup_bat(BAT_WIDTH,BAT_HEIGHT)
    ball_img_rect=setup_ball()
    lista_current_speed=[BALL_SPEED_HOR,BALL_SPEED_VERT] # lista para armazenar as velocidades vertical e horizontal da bola
    block_keys=setup_blocks()[2]
    block_rect=setup_blocks()[1]
    block_img_blu_scale=setup_blocks()[0]

    pygame.display.update()
    return [lista_current_speed,ball_img_rect,bat_img_rect,block_rect,block_img_blu_scale,block_keys] # retorna valores a serem alterados durante o andamento do jogo
    
def update_blocks(lista): # atualiza os blocos (#recebe uma lista com block_img_blu_scale, blocks_rect e block_keys)
    assets=load_assets()

    block_img_blu_scale=lista[0]
    blocks_rect=lista[1]
    block_keys=lista[2]

    for block in block_keys: # o processo a seguir é repetido para todos os blocos
        if block in blocks_rect.keys() and BALL_POS[0]-block_positions[block][0]<=BLOCK_WIDTH and BALL_POS[0]-block_positions[block][0]>=0  and BALL_POS[1]-block_positions[block][1]<=BLOCK_HEIGHT and BALL_POS[1]-block_positions[block][1]>=0: #verifica condição de colisão entre bola e bloco
            blocks_rect.pop(block) # retira o bloco do dicionário
            pygame.mixer.Sound.play(assets[BLOCK_SOUND_1]) # toca som de colisão com o bloco

        elif block in blocks_rect.keys(): # verifica se o bloco ainda existe no dicionário de blocos

            block_img_rect=block_img_blu_scale.get_rect(topleft=(block_positions[block]))# cria um retângulo com o bloco
            WINDOW.blit(block_img_blu_scale,block_img_rect) # desenha o retângulo
    

def update_speed(lista_current_speed,ball_img_rect,bat_img_rect,blocks_rect,block_keys): #atualiza os valores de velocidade vertical e horizontal
    assets=load_assets()

    if BALL_POS[0]>=WIDTH or BALL_POS[0]<0 :# verifica condição de colidão entre bola e as bordas da janela
        lista_current_speed[0]*=-1 # inverte a velocidade horizontal da bola
        pygame.mixer.Sound.play(assets[PAREDE_SOUND]) # toca o som de colisão com as paredes

    if BALL_POS[1]>HEIGHT-BALL_HEIGHT or BALL_POS[1]<(0+BALL_HEIGHT): # verifica condição de colidão entre bola e as bordas da janela
        lista_current_speed[1]*=-1 # inverte a velocidade vertical da bola
        pygame.mixer.Sound.play(assets[PAREDE_SOUND])# toca o som de colisão com as paredes

    if BALL_POS[0]-BAT_POS[0]<=BAT_WIDTH and BALL_POS[0]-BAT_POS[0]>=0 and BALL_POS[1]-BAT_POS[1]<=BAT_HEIGHT and BALL_POS[1]-BAT_POS[1]>=0: # verifica condição de colisão enre bola e 'bat'
        lista_current_speed[1]*=-1 # inverte a velocidade vertical da bola
        pygame.mixer.Sound.play(assets[BAT_SOUND]) # toca o som de colisão com o 'bat'

        if lista_current_speed[0] == -BALL_SPEED_HOR_BASE and BAT_POS[0]+BAT_WIDTH-BALL_POS[0]>=0: # verifica a bola bateu na primeira metade do bat e se a velocidade é positiva
            lista_current_speed[0]*= - 1 # inverte a velocidade horizontal da bola
        if  lista_current_speed[0]== BALL_SPEED_HOR_BASE and BALL_POS[0]-(BAT_POS[0]+BAT_WIDTH/2)>0: # verifica a bola bateu na segunda metade do bat e se a velocidade é negativa
            lista_current_speed[0]*= - 1 # inverte a velocidade horizontal da bola


    for block in block_keys:
        if block in blocks_rect.keys() and BALL_POS[0]-block_positions[block][0]<=BLOCK_WIDTH and BALL_POS[0]-block_positions[block][0]>=0  and BALL_POS[1]-block_positions[block][1]<=BLOCK_HEIGHT and BALL_POS[1]-block_positions[block][1]>=0: #verifica condição de colisão entre bola e bloco
            lista_current_speed[1]*=-1 # inverte a velocidade vertical da bola


def update_ball(event,speed_lista): # atualiza a posição da bola

    assets=load_assets()

    BALL_POS[0]+=speed_lista[0] # atualiza a posição horizontal da bola com base na velocidade calculada em update_speed
    BALL_POS[1]+=speed_lista[1] # atualiza a posição vertical da bola com base na velocidade calculada em update_speed

    ball_img_rect=assets[BALL_IMG].get_rect(topleft=(BALL_POS)) # cria o retângulo da bola na nova posição

    WINDOW.blit(assets[BALL_IMG],ball_img_rect) # desenha a bola na nova posição

def update_bat(BAT_POS,event): #atualiza a posição do 'bat'
    assets=load_assets()

    if event.type == pygame.KEYDOWN:
        keys_down[event.key] = True
        if event.key == pygame.K_LEFT and BAT_POS[0]>0: # verifica se a seta esquerda está apertada e se o bat não está saíndo da janela
           BAT_POS_0[0]-=20 # move o bat para a esquerda

        if event.key == pygame.K_RIGHT and BAT_POS[0]<(WIDTH-BAT_WIDTH): # verifica se a seta direita está apertada e se o bat não está saíndo da janela
            BAT_POS_0[0]+=20 # move o bat para a direita
     
    bat_img_rect=assets[BAT_IMG].get_rect(topleft=(BAT_POS)) # cria um retângulo com o bat na nova posição

    WINDOW.blit(assets[BAT_IMG], bat_img_rect) #desenha o bat na nova posição
    
WINDOW=pygame.display.set_mode((WIDTH,HEIGHT)) #configura a janela
