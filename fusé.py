import pygame
class fuse (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('asset/fusee.png')
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.vitesse=1
        self.rect.x= 200
        self.rect.y=350
        self.skin=True
    def tombe(self):
        self.rect.y += self.vitesse
        self.vitesse+=0.09
    def monte(self):
        self.vitesse=1
        self.rect.y -= 60
    def change1(self):
        self.image = pygame.image.load('asset/fusee.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
    def change2(self):
        self.image = pygame.image.load('asset/fusee2.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
    def chage_skin(self):
        if self.skin == True:
            self.change1()
            self.skin = False
        else :
            self.change2()
            self.skin = True