import pygame

pygame.init()

display = pygame.display.set_mode((1280,720))

player1 = pygame.Rect(0,0,30,150)
player1_speed = 0
player2 = pygame.Rect(1250,0,30,150)
player2_speed = 0
ball = pygame.Rect(600,350,15,15)
ball_dir_x = 5
ball_dir_y = 5

# Variáveis de pontuação
score1 = 0
score2 = 0
font = pygame.font.SysFont('sans', 40)

pygame.draw.rect(display, (0,0,0), player1)
pygame.draw.rect(display, (0,0,0), player2)
pygame.draw.circle(display,(0,0,0),ball.center, 8)
fps = pygame.time.Clock()

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                loop = False

            # Movimento do Player 1
            if event.key == pygame.K_w:
                player1_speed = -5
            elif event.key == pygame.K_s:
                player1_speed = 5

            # Movimento do Player 2
            if event.key == pygame.K_o:
                player2_speed = -5
            elif event.key == pygame.K_l:
                player2_speed = 5

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_w, pygame.K_s]:
                player1_speed = 0
            if event.key in [pygame.K_o, pygame.K_l]:
                player2_speed = 0

    # Movimentação dos jogadores
    player1.y += player1_speed
    player2.y += player2_speed

    # Limites dos jogadores
    player1.y = max(0, min(player1.y, 720 - 150))
    player2.y = max(0, min(player2.y, 720 - 150))

    # Colisão da bola com os jogadores
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_dir_x *= -1
        hit = pygame.mixer.Sound("som/colisao.wav")
        hit.play()

    # Pontuação
    if ball.x <= 0: 
        score2 += 1
        ball.x, ball.y = 600, 350
        ball_dir_x *= -1
        point_sound = pygame.mixer.Sound("som/ponto2.wav")
        point_sound.play()
    
    elif ball.x >= 1280:
        score1 += 1
        ball.x, ball.y = 600, 350
        ball_dir_x *= -1
        point_sound = pygame.mixer.Sound("som/ponto1.wav")
        point_sound.play()

    # Movimento da bola
    if ball.y <= 0 or ball.y >= 720 - 15:
        ball_dir_y *= -1

    ball.x += ball_dir_x
    ball.y += ball_dir_y

    # Renderização
    display.fill((0,255,0))
    pygame.draw.rect(display, "black", player1)
    pygame.draw.rect(display, "black", player2)
    pygame.draw.circle(display, "black", ball.center, 8)

    # Exibir placar
    text1 = font.render(f'Player 1: {score1}', True, (255, 255, 255))
    text2 = font.render(f'Player 2: {score2}', True, (255, 255, 255))
    display.blit(text1, (500, 50))
    display.blit(text2, (700, 50))

    fps.tick(60)
    pygame.display.flip()