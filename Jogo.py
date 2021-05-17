import pygame
import Classes
import config
import Assets

WINDOW=pygame.display.set_mode((config.WIDTH,config.HEIGHT))
pygame.display.set_caption('Nome')

def draw_window():
    WINDOW.fill((255,255,255))
    pygame.display.update()

def main():
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