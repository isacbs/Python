import pygame
import random
from pygame.locals import *

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Jogo da Nave Espacial')

nave_image = pygame.image.load('nave.png')
nave_image = pygame.transform.scale(nave_image, (50, 50))

class Tiro(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(midbottom=position)
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

class NaveEspacial(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.position = pygame.math.Vector2(screen_width // 2, screen_height - 60)
        self.speed = 5
        self.image = nave_image
        self.rect = self.image.get_rect(center=self.position)
        self.all_tiros = pygame.sprite.Group()

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[K_LEFT] and self.rect.left > 0:
            self.position.x -= self.speed
        if keys[K_RIGHT] and self.rect.right < screen_width:
            self.position.x += self.speed
        if keys[K_UP] and self.rect.top > 0:
            self.position.y -= self.speed
        if keys[K_DOWN] and self.rect.bottom < screen_height:
            self.position.y += self.speed

        self.rect.center = self.position

        if keys[K_SPACE]:
            self.shoot()

        self.all_tiros.update()

    def shoot(self):
        tiro = Tiro(self.rect.midtop)
        self.all_tiros.add(tiro)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.all_tiros.draw(screen)

class Asteroide(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = random.randint(20, 70)
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.size)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(2, 6)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > screen_height:
            self.kill()

def main():
    nave = NaveEspacial("Nave 1")
    all_sprites = pygame.sprite.Group(nave)
    asteroides = pygame.sprite.Group()

    clock = pygame.time.Clock()
    running = True
    spawn_timer = 0

    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        all_sprites.update()
        asteroides.update()

        spawn_timer += 1
        if spawn_timer > 30:
            asteroide = Asteroide()
            asteroides.add(asteroide)
            all_sprites.add(asteroide)
            spawn_timer = 0

        all_sprites.draw(screen)
        nave.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()