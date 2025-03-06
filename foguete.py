import pygame
from pygame.locals import *

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jogo da Nave Espacial")

class NaveEspacial(pygame.sprite.Sprite):
    def __init__(self, name):
        super(NaveEspacial, self).__init__()
        self.name = name
        self.alive = True
        self.position = pygame.math.Vector2(screen_width // 2, screen_height //2)
        self.direction = 0
        self.speed = 5
        self.shield = 100
        self.energy = 100
        self.image = pygame.Surface((50, 30))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[K_LEFT]:
            self.position.x -= self.speed
        if keys[K_RIGHT]:
            self.position.x += self.speed    
        if keys[K_UP]:
                self.position.y -= self.speed
        if keys[K_DOWN]:
            self.position.y += self.speed

        if keys[K_n]:
            self.speed += 1
        if keys[K_m] and self.speed > 1:
            self.speed -= 1
        self.rect.center = self.position
                
def main():
    nave = NaveEspacial("Nave 1")
    all_sprites = pygame.sprite.Group()
    all_sprites.add(nave)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        all_sprites.update()

        screen.fill((0, 0 , 0))    
        all_sprites.draw(screen)        

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()                
