import pygame

class Shot(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('img/shot.png')
        self.rect = pygame.Rect(300, 240, 40, 40)
        self.rect.y = 200
        self.speed = 3



    def update(self, *args):
        self.rect.y -= self.speed

        if self.rect.bottom < 0:
            self.kill()

