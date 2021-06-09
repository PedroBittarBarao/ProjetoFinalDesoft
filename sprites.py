"""
Arquivo com as classes do jogo.
"""

import pygame
from config import SW, SH,   BLOCK_W, BLOCK_H,   BALL_SPEEDX_0, BALL_SPEEDY_0
from Assets import BALL_IMG, BAT_IMG, WALL_SND


class Ball(pygame.sprite.Sprite):
    def __init__(self, assets):
        super().__init__()

        self.image = assets[BALL_IMG]
        # Guarda o som da parede para ser usado na função 'update'
        self.sound = assets[WALL_SND]
        
        self.mask = pygame.mask.from_surface(self.image)
        # Rect e posição inicial
        self.rect = self.image.get_rect(center = (SW/2, (SH - 180)))
        # Velocidades iniciais nos eixos x e y
        self.speedx = BALL_SPEEDX_0
        self.speedy = BALL_SPEEDY_0

    def update(self):
        # Altera da posição da bola de acordo com sua velocidade
        self.rect.x += self.speedx
        self.rect.y -= self.speedy

        # Limita a posição da bola à largura da tela (cria paredes) e atribui um efeito sonoro à colisão
        if self.rect.left <0 or self.rect.right> SW:
            self.sound.play()
            self.speedx *= -1
        
        # Limita a posição da bola ao início da tela (teto) e atribui um efeito sonoro à colisão
        if self.rect.top <0:
            self.sound.play()
            self.speedy *= -1

class Bat(pygame.sprite.Sprite):
    def __init__(self, assets):
        super().__init__()    

        self.image = assets[BAT_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        # Posiciona o Rect no centro horizontal da tela
        self.rect = self.image.get_rect(center = (SW/2, SH - 80))
        # Velocidade inicial
        self.speedx = 0
    
    def update(self):
        #Altera a posição do 'bat' de acordo com sua velocidade
        self.rect.x += self.speedx

        # Limita a posição do 'bat' à largura da tela
        if self.rect.left <0:
            self.rect.left = 0
        if self.rect.right> SW:
            self.rect.right = SW
        

class Block(pygame.sprite.Sprite):
    def __init__(self, assets, color, l, c):
        super().__init__()
        
        #Dimensões do bloco
        self.width = BLOCK_W
        self.height = BLOCK_H
        # A imagem do bloco varia de acordo com sua cor
        self.image = assets[color]

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        # Atribui diferentes posições ao Rect (a classe será implementada num loop para criar uma parede) 
        self.rect.x = (c-1) * self.width 
        self.rect.y = (l-1) * self.height
    
    def update(self):
        pass

