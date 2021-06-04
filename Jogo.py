#ANÁLISE PT.2
import pygame
"""
from config import BALL_POS_0, BALL_SPEED_HOR_BASE, BALL_SPEED_VERT_BASE, BAT_POS_0, BLOCK_H,BLOCK_W, GAME, SW
from Assets import BAT_IMG, load_assets,GAME_FNT,BACKGROUND,BAT_H,BAT_W,BLOCK_IMG_BLU,BLOCK_IMG_YLW,BLOCK_IMG_GRN,BLOCK_IMG_RED
from funcoes import BALL_POS, setup_blocks,setup_bat,setup_window, update_ball,update_bat,update_blocks,WINDOW,BALL_SPEED_HOR,BALL_SPEED_VERT, update_speed
"""

from config import SW, SH, FPS, INIT, GAME, QUIT
from Assets import  load_assets, BACKGROUND, WALL_SND, BLOCK_SND_1, BLOCK_SND_2, GAME_FNT
from funcoes import Ball, Bat, Block

"""
pygame.display.set_caption('Breakout')
BAT_POS=BAT_POS_0 # cria uma variável com a posição do bat para se alterada depois
keys_down = {}
SCORE=0
"""

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((SW, SH))
pygame.display.set_caption('Breakout')

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    # Criando um grupo de meteoros
    all_sprites = pygame.sprite.Group()
    all_blocks = pygame.sprite.Group()

    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_blocks'] = all_blocks

    # Criando elementos do jogo
    ball = Ball(assets)
    all_sprites.add(ball)
    player = Bat(assets)
    all_sprites.add(player)

    #Criando os blocos
    for c in range(1, 16):
        for l in range(1, 10):
            block = Block(assets, l, c)
            all_sprites.add(block)
            all_blocks.add(block)


    INIT = 0
    GAME = 1
    QUIT = 2

    state = GAME

    keys_down = {}
    score = 0
    lives = 3

    # ===== Loop principal =====
    #pygame.mixer.music.play(loops=-1)
    while state != QUIT:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = QUIT
            # Só verifica o teclado se está no estado de jogo
            if state == GAME:
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 15
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 15
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            player.speedx += 15
                        if event.key == pygame.K_RIGHT:
                            player.speedx -= 15

        # ----- Atualiza estado do jogo
        # Atualizando a posição dos meteoros
        all_sprites.update()

        if state == GAME:
            #Colisões:
            hits = pygame.sprite.spritecollide(player, all_blocks, True)
            for block in hits:
                assets[BLOCK_SND_1]

                score+= 10

            """
        elif state == EXPLODING:
            now = pygame.time.get_ticks()
            if now - explosion_tick > explosion_duration:
                if lives == 0:
                    state = DONE
                else:
                    state = PLAYING
                    player = Ship(groups, assets)
                    all_sprites.add(player)
            """

        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets[BACKGROUND], (0, 0))
        # Desenhando todos os sprites
        all_sprites.draw(window)

        # Desenhando o score
        text_surface = assets[GAME_FNT].render('SCORE :{} '.format(score), True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        window.blit(text_surface, text_rect)

        # Desenhando as vidas
        text_surface = assets[GAME_FNT].render('LIVES :{} '.format(lives), True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        window.blit(text_surface, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador

game_screen(window)
#Finalização
pygame.quit()

"""
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
"""