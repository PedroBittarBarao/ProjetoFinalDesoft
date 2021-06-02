import pygame
from funcoes import BALL_POS, setup_blocks,setup_bat,setup_window, update_ball,update_bat,update_blocks,WINDOW,BALL_SPEED_HOR,BALL_SPEED_VERT, update_speed
import config
from config import BALL_POS_0, BALL_SPEED_HOR_BASE, BALL_SPEED_VERT_BASE, BAT_POS_0, BLOCK_HEIGHT,BLOCK_WIDTH, GAME, WIDTH
import Assets
from Assets import BAT_IMG, load_assets,GAME_FONT,BACKGROUND,BAT_HEIGHT,BAT_WIDTH,BLOCK_IMG_BLU,BLOCK_IMG_YLW,BLOCK_IMG_GRN,BLOCK_IMG_RED



pygame.display.set_caption('Breakout')
BAT_POS=BAT_POS_0 # cria uma variável com a posição do bat para se alterada depois
keys_down = {}
SCORE=0
   

def update_window(event,lista_current_speed,ball_img_rect,bat_img_rect,blocks_rect,block_img_blu_scale,block_keys,SCORE,VIDAS): # puxa funções de atualização e atualiza a tela
    WINDOW.fill((255,255,255))

    assets=Assets.load_assets()
    WINDOW.blit(assets[BACKGROUND], (0, 0))

    update_bat(BAT_POS,event)
    update_speed(lista_current_speed,ball_img_rect,bat_img_rect,blocks_rect,block_keys)
    update_blocks([block_img_blu_scale,blocks_rect,block_keys])
    update_ball(event,lista_current_speed)
    
    SCORE+=len(block_keys)-len(blocks_rect.keys()) # calcula o score com base no número de blocos quebrados

    text1 = assets[GAME_FONT].render('SCORE :{} '.format(SCORE), True, (0, 0, 0))
    text2 = assets[GAME_FONT].render('LIVES :{} '.format(VIDAS), True, (0, 0, 0))
    WINDOW.blit(text1, (10, 570)) # desenha o score
    WINDOW.blit(text2, (240, 570)) # desenha as vidas
    pygame.display.update() # atualiza a imagem

def main():
    VIDAS=3

    pygame.init
    pygame.font.init()
    pygame.mixer.init()
    clock=pygame.time.Clock()
    game=True
    lista_setup=setup_window() # executa a função e coleta os valores interessantes
    lista_current_speed=lista_setup[0]
    ball_img_rect=lista_setup[1]
    bat_img_rect=lista_setup[2]
    block_keys=lista_setup[5]
    blocks_rect=lista_setup[3]
    block_img_blu_scale=lista_setup[4]
    while game:
        clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game=False

        update_window(event,lista_current_speed,ball_img_rect,bat_img_rect,blocks_rect,block_img_blu_scale,block_keys,SCORE,VIDAS)
        if BALL_POS[1]>565: # se a bola estiver inferior ao bat:
            BALL_POS[0]=WIDTH/2 # retorna a bola para a posição horizontal inicial
            BALL_POS[1]=450 # retorna a bola para uma posição vertical

            VIDAS-=1 # retira uma vida
            lista_current_speed=[BALL_SPEED_HOR_BASE,BALL_SPEED_HOR_BASE] # retorna as velocidades da bola para os valores iniciais

        if VIDAS<=0: # verifica se o jogador ainda tem vidas
            game=False # termina o jogo


    pygame.QUIT

main()