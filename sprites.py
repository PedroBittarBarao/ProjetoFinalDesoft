import pygame
from config import SW, SH,   BAT_W, BAT_H,   BLOCK_W, BLOCK_H,   BALL_SPEEDX_0, BALL_SPEEDY_0
from Assets import BALL_IMG, BAT_IMG, WALL_SND
"BLOCK_IMG_RED, BLOCK_IMG_GRN, BLOCK_IMG_BLU, BLOCK_IMG_YLW,   WALL_SND, BAT_SND, BLOCK_SND_1, BLOCK_SND_2"


class Ball(pygame.sprite.Sprite):
    def __init__(self, assets):
        super().__init__()

        self.image = assets[BALL_IMG]
        self.sound = assets[WALL_SND]
        self.mask = pygame.mask.from_surface(self.image)
        #Rect e posição inicial
        self.rect = self.image.get_rect(center = (SW/2, (SH - 160)))
        #Velocidade inicial
        self.speedx = BALL_SPEEDX_0
        self.speedy = BALL_SPEEDY_0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y -= self.speedy

        if self.rect.left <0 or self.rect.right> SW:
            self.sound.play()
            self.speedx *= -1

        if self.rect.top <0:
            self.sound.play()
            self.speedy *= -1

class Bat(pygame.sprite.Sprite):
    def __init__(self, assets):
        super().__init__()    

        self.image = assets[BAT_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center = (SW/2, SH - 80))
        #Velocidade inicial
        self.speedx = 0
    
    def update(self):
        self.rect.x += self.speedx

        if self.rect.x <0:
            self.rect.x = 0
        if (self.rect.x + BAT_W)> SW:
            self.rect.x = SW - BAT_W
        

class Block(pygame.sprite.Sprite):
    def __init__(self, assets, color, l, c):
        super().__init__()
        self.width = BLOCK_W
        self.height = BLOCK_H
        self.image = assets[color]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = (c-1) * self.width 
        self.rect.y = (l-1) * self.height
    
    def update(self):
        pass

    def destroy(self):
        self.kill()

