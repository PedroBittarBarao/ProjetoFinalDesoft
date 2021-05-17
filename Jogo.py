import pygame

WIDTH, HEIGHT = 800, 720
WINDOW=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Nome')

FPS = 60 

def draw_window():
    WINDOW.fill((255,255,255))
    pygame.display.update()

def main():
    clock=pygame.time.Clock()
    game=True
    while game:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game=False

        draw_window()

    pygame.QUIT

main()