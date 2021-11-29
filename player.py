import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('img/sprite.png')
        self.rect = pygame.Rect(300, 240, 40, 40)


    def update(self, *args):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x += -5
        elif keys[pygame.K_RIGHT]:
            self.rect.x += +5

        #limitando o sprite dentro da janela
        if self.rect.left < -80:
            self.rect.left = -80
        elif self.rect.right > 645:
            self.rect.right = 645