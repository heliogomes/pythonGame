import pygame
from player import Player
from asteroide import Asteroide
from shot import Shot
import random


#inicializando
pygame.init()
#Criando janela#
display = pygame.display.set_mode([800, 600])
#Alterando nome da  janela#
pygame.display.set_caption("Infinite Shot")

#Object
objectGroup = pygame.sprite.Group()
asteroideGroup = pygame.sprite.Group()
shotGroup = pygame.sprite.Group()



#background
bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load('img/background.jpg')
bg.image = pygame.transform.scale(bg.image, [800, 600])
bg.rect = bg.image.get_rect()

player = Player(objectGroup)
shot = Shot(objectGroup)

#Music
pygame.mixer.music.load('song/song.wav')
pygame.mixer.music.play(-1)

#sound
shotsound = pygame.mixer.Sound('song/shot.flac')


#Criando loop
gameLoop = True

#limitarfps
clock = pygame.time.Clock()

timer = 20


if __name__ == '__main__':
    while gameLoop:
        clock.tick(60) #limitando fps
        for event in pygame.event.get(): #Fechar jogo
            if event.type == pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shotsound.play()
                    newShot = Shot(objectGroup, shotGroup)
                    newShot.rect.x = player.rect.x


        display.fill([0, 25, 105])  # Cor do fundo

        #Update (logica)
        objectGroup.update()

        #Fazer surgir novos asteroides
        timer += 1
        if timer > 30:
            timer = 0
            if random.random() < 0.7:
                newAsteroide = Asteroide(objectGroup, asteroideGroup)

        collisions = pygame.sprite.spritecollide(player, asteroideGroup, False)

        if collisions:
            print('Game Over')
            gameLoop = False


        hits = pygame.sprite.groupcollide(shotGroup, asteroideGroup, True, True)

        # Draw
        objectGroup.draw(display)
        pygame.display.update()
