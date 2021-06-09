"""
Arquivo com a tela principal do jogo.
"""

import pygame
from config import SW, SH,   FPS,   BLACK, WHITE,   GAME, QUIT,END
from Assets import  load_assets, BACKGROUND,   BLOCK_IMG_RED, BLOCK_IMG_GRN, BLOCK_IMG_BLU, BLOCK_IMG_YLW,   BAT_SND, BLOCK_SND_1, BLOCK_SND_2,   GAME_FNT
from sprites import Ball, Bat, Block


def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Armazenando assets
    assets = load_assets()

    # Criação de grupos de sprites 
    all_balls = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_blocks = pygame.sprite.Group()
    groups = {}
    groups['all_balls'] = all_balls
    groups['all_sprites'] = all_sprites
    groups['all_blocks'] = all_blocks

    # Criando elementos do jogo:
    
    # Bola (é inserida num grupo de bolas para a execução da colisão com o 'bat')
    ball = Ball(assets)
    all_sprites.add(ball)
    all_balls.add(ball)
    # Bat
    player = Bat(assets)
    all_sprites.add(player)

    # Blocos (c--> coluna, l--> linha)
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

    # Dicionário de eventos do teclado
    keys_down = {}

    # Pontuação e vidas
    score = 0
    lives = 3

    # ===== Loop principal =====
    # pygame.mixer.music.play(loops=-1)
    while state != QUIT:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = QUIT
            # Só verifica o teclado se está no estado de jogo
            if state == GAME:
                # Verifica se apertou alguma tecla
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 15
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 15
                # Verifica se soltou alguma tecla
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            player.speedx += 15
                        if event.key == pygame.K_RIGHT:
                            player.speedx -= 15

        # ----- Atualiza estado do jogo
        all_sprites.update()

        if state == GAME: 
            
            # Colisões:

            # Colisão bola-bat
            if pygame.sprite.spritecollide(player, all_balls, False, pygame.sprite.collide_mask ):
                assets[BAT_SND].play()
                ball.speedy *= -1
  
            # Colisão bola-bloco
            block_hits = pygame.sprite.spritecollide(ball, all_blocks, True, pygame.sprite.collide_mask)
            for block in block_hits:
                assets[BLOCK_SND_1].play()
                ball.speedy *= -1
                
            """Diferentes pontuações para cada cor"""
           
            # Se o topo da bola passar do limite da tela (se ela cair):
            if ball.rect.top > SH:
                ball.kill() 
                lives -= 1
                # Aguardo de 3 segundos
                pygame.time.delay(3000)

                # Se não houver mais vidas disponíveis, o jogo acaba  
                if lives == 0:
                    state = END
                else:
                    # Caso contrário, a bola será redesenhada na tela 
                    state = GAME
                    ball = Ball(assets)
                    all_sprites.add(ball)
                    all_balls.add(ball)

            """
            if ball.rect.y > HEIGHT:
            ball.rect.x = WIDTH // 2 - 5
            ball.rect.y = HEIGHT // 2 - 5
            ball.velocity[1] = ball.velocity[1]
            balls += 1
            if balls == 4:
                font = pygame.font.Font('text_style/DSEG14Classic-Bold.ttf', 70)
                text = font.render("GAME OVER", 1, WHITE)
                text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
                screen.blit(text, text_rect)
                pygame.display.update()
                pygame.time.wait(2000)
                run = False
            """
        
        # ----- Gera saídas
        window.fill(BLACK)
        window.blit(assets[BACKGROUND], (0, 0))
        # Desenhando todos os sprites
        all_sprites.draw(window)

        # Desenhando o score
        text_surface = assets[GAME_FNT].render('SCORE :{} '.format(score), True, WHITE)
        text_rect = text_surface.get_rect(x = 230, y = 570)
        window.blit(text_surface, text_rect)

        # Desenhando as vidas
        text_surface = assets[GAME_FNT].render('LIVES :{} '.format(lives), True, WHITE)
        text_rect = text_surface.get_rect(x = 10, y = 570)
        window.blit(text_surface, text_rect)

        # Mostra o novo frame para o jogador
        pygame.display.update()

    return state

