import pygame
from pygame.locals import *
from sys import exit
import math

pygame.init()
SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE)

tank = pygame.image.load('tanque.jpg').convert_alpha()
tank_original = tank

x, y = 0, 0
target_x, target_y = x, y
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            target_x, target_y = event.pos

    dx = target_x - x # Calcula a direção do movimento
    dy = target_y - y
    distance = math.hypot(dx, dy)

    if distance > 0:
        angle = math.degrees(math.atan2(-dy, dx))
        x += dx / distance
        y += dy / distance

    tank_rotated = pygame.transform.rotate(tank_original, angle) # Rotaciona a imagem do tanque
    tank_rect = tank_rotated.get_rect(center=(x, y))

    screen.fill((255, 255, 255)) # Atualiza a tela
    screen.blit(tank_rotated, tank_rect.topleft)
    pygame.display.update()
