import pygame
import random

class Asteroide(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('img/sprite2.png')
        self.rect = pygame.Rect(0, 0, 40, 40)
        # meteoro descer na posicao vertical inicial
        self.rect.y = -150 + random.randint(-75, 1)
        # meteoro descer em uma posiçao aleatoria
        self.rect.x = random.randint(-80, 660)
        self.speed = 2 + random.random() * 6

    def update(self, *args):
        self.rect.y += self.speed
        # Fazer o esteroide sumir apos sair da tela
        if self.rect.top > 390:
            self.kill()