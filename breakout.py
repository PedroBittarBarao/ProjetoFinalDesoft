import pygame

from config import SW, SH, FPS, BLACK, WHITE, INIT, GAME, QUIT
from assets import  load_assets, BACKGROUND, BLOCK_IMG_RED, BLOCK_IMG_GRN, BLOCK_IMG_BLU, BLOCK_IMG_YLW, WALL_SND, BLOCK_SND_1, BLOCK_SND_2, GAME_FNT
from sprites import Ball, Bat, Block


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
    for c in range(1, 13):
        for l in range (1, 3):
            block = Block(assets, BLOCK_IMG_RED, l, c)
            all_sprites.add(block)
            all_blocks.add(block)
        for l in range (3, 5):
            block = Block(assets, BLOCK_IMG_BLU, l, c)
            all_sprites.add(block)
            all_blocks.add(block)
        for l in range (5, 7):
            block = Block(assets, BLOCK_IMG_GRN, l, c)
            all_sprites.add(block)
            all_blocks.add(block)
        for l in range(7, 9):
            block = Block(assets, BLOCK_IMG_YLW, l, c)
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
        all_sprites.update()

        if state == GAME:
            
            #Colisão bola-paddle/bat:
            #if pygame.sprite.spritecollide(player, all_sprites, True, pygame.sprite.collide_mask):
                #ball.speedy *= -1
            
            #Colisão bola-bloco:
            block_hits = pygame.sprite.spritecollide(ball, all_blocks, True, pygame.sprite.collide_mask)
            for block in block_hits:
                assets[BLOCK_SND_1].play()
                ball.speedy *= -1

                score+= 10

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        window.blit(assets[BACKGROUND], (0, 0))
        # Desenhando todos os sprites
        all_sprites.draw(window)

        # Desenhando o score
        text_surface = assets[GAME_FNT].render('SCORE :{} '.format(score), True, WHITE)
        text_rect = text_surface.get_rect(x = 200, y = 570)
        window.blit(text_surface, text_rect)

        # Desenhando as vidas
        text_surface = assets[GAME_FNT].render('LIVES :{} '.format(lives), True, WHITE)
        text_rect = text_surface.get_rect(x = 10, y = 570)
        window.blit(text_surface, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador

game_screen(window)

#Finalização
pygame.quit()
