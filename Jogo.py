import pygame
from funcoes import setup_blocks,setup_bat,setup_window, update_ball,update_bat,update_blocks,WINDOW,BALL_SPEED_HOR,BALL_SPEED_VERT, update_speed
import config
from config import BALL_SPEED_VERT_BASE, BLOCK_HEIGHT,BLOCK_WIDTH, WIDTH
import Assets
from Assets import BAT_IMG, load_assets,GAME_FONT,BACKGROUND,BAT_HEIGHT,BAT_WIDTH,BLOCK_IMG_BLU,BLOCK_IMG_YLW,BLOCK_IMG_GRN,BLOCK_IMG_RED



pygame.display.set_caption('Nome')
BAT_POS=config.BAT_POS_0
keys_down = {}

   

def update_window(event,lista_current_speed,ball_img_rect,bat_img_rect,blocks_rect,block_img_blu_scale,block_keys): # puxa funções de atualização e atualiza a tela
    WINDOW.fill((255,255,255))
    assets=Assets.load_assets()
    WINDOW.blit(assets[BACKGROUND], (0, 0))
    update_bat(BAT_POS,event)
    update_speed(lista_current_speed,ball_img_rect,bat_img_rect,blocks_rect,block_keys)
    update_blocks([block_img_blu_scale,blocks_rect,block_keys])
    update_ball(event,lista_current_speed)
    pygame.display.update()

def main():
    pygame.init
    pygame.font.init()
    clock=pygame.time.Clock()
    game=True
    lista_current_speed=setup_window()[0]
    ball_img_rect=setup_window()[1]
    bat_img_rect=setup_window()[2]
    block_keys=setup_window()[5]
    blocks_rect=setup_window()[3]
    block_img_blu_scale=setup_window()[4]
    while game:
        clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game=False
        update_window(event,lista_current_speed,ball_img_rect,bat_img_rect,blocks_rect,block_img_blu_scale,block_keys)

    pygame.QUIT

main()