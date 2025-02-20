import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE =(800,600)
screen = pygame.display.set_mode(SCREEN_SIZE)

tank = pygame.image.load('tanque.jpg').convert()

x, y = 0, 0
target_x, target_y = x, y

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            target_x, target_y = event.pos

    if x < target_x: # Calcula o deslocamento para mover o tanque suavemente
        x += 1
    elif x > target_x:
        x -= 1
    if y < target_y:
        y += 1
    elif y > target_y:
        y -= 1

    screen.fill((255,255,255))
    screen.blit(tank,(x,y))

    pygame.display.update()
