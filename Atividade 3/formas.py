import pygame
from pygame.locals import *
from sys import exit
from random import *

pygame.init()
screen = pygame.display.set_mode((640,480))
def gera_cor():
    red = randrange(0,255)
    green = randrange(0,255)
    blue = randrange(0,255)
    colorRect = (red, green, blue)
    return colorRect

def retangulo():
    altura = randrange(0,70)
    largura = randrange(0,70)
    pos_x = randrange(0,600)
    pos_y = randrange(0,600)
    return pygame.draw.rect(screen, gera_cor(), (pos_x, pos_y, altura,
largura))

def circulo():
    raio = randrange(0,100)
    pos_x = randrange(0,600)
    pos_y = randrange(0,600)
    return pygame.draw.circle(screen, gera_cor(), (pos_x, pos_y), raio)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    retangulo()
    circulo()

    pygame.display.update()