import pygame
import Classes
import config
import Assets
from Assets import load_assets,GAME_FONT,BACKGROUND


WINDOW=pygame.display.set_mode((config.WIDTH,config.HEIGHT))
pygame.display.set_caption('Nome')

def draw_window():
    WINDOW.fill((255,255,255))
    assets=Assets.load_assets()
    WINDOW.blit(assets[BACKGROUND], (0, 0))
    pygame.display.update()

def main():
    pygame.init
    pygame.font.init()
    clock=pygame.time.Clock()
    game=True
    while game:
        clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game=False

        draw_window()

    pygame.QUIT

main()