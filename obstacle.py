import pygame

class ob (pygame.sprite.Sprite):
    def __init__(self,co,gr):
        super().__init__()
        self.image = pygame.image.load('asset/ob1.png')
        self.rect = self.image.get_rect()
        self.rect.y = co
        self.gr=gr
        self.rect.x=1500
    def mouve(self):
        self.rect.x-=6
        if self.rect.x <= -30:
            self.kill()
            print('ob')










