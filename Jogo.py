import pygame
from funcoes import setup_blocks,setup_bat,setup_window, update_ball,update_bat,update_blocks,WINDOW,BALL_SPEED_HOR,BALL_SPEED_VERT, update_speed
import config
from config import BALL_SPEED_VERT_BASE, BLOCK_HEIGHT,BLOCK_WIDTH, WIDTH
import Assets
from Assets import BAT_IMG, load_assets,GAME_FONT,BACKGROUND,BAT_HEIGHT,BAT_WIDTH,BLOCK_IMG_BLU,BLOCK_IMG_YLW,BLOCK_IMG_GRN,BLOCK_IMG_RED



pygame.display.set_caption('Nome')
BAT_POS=config.BAT_POS_0
keys_down = {}
SCORE=0
   

def update_window(event,lista_current_speed,ball_img_rect,bat_img_rect,blocks_rect,block_img_blu_scale,block_keys,SCORE): # puxa funções de atualização e atualiza a tela
    WINDOW.fill((255,255,255))
    assets=Assets.load_assets()
    WINDOW.blit(assets[BACKGROUND], (0, 0))
    update_bat(BAT_POS,event)
    update_speed(lista_current_speed,ball_img_rect,bat_img_rect,blocks_rect,block_keys)
    update_blocks([block_img_blu_scale,blocks_rect,block_keys])
    update_ball(event,lista_current_speed)
    SCORE+=len(block_keys)-len(blocks_rect.keys())
    text1 = assets[GAME_FONT].render('SCORE :{} '.format(SCORE), True, (0, 0, 0))
    WINDOW.blit(text1, (10, 570))
    pygame.display.update()

def main():
    pygame.init
    pygame.font.init()
    pygame.mixer.init()
    clock=pygame.time.Clock()
    game=True
    lista_setup=setup_window()
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
        update_window(event,lista_current_speed,ball_img_rect,bat_img_rect,blocks_rect,block_img_blu_scale,block_keys,SCORE)

    pygame.QUIT

main()