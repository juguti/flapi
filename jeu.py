#import des différent module et classe
import pygame
from pygame import mixer
from fusé import fuse
from obstacle import ob
from random import *
from time import *
#Paramettrage de la page de jeu
pygame.init()
pygame.mixer.init()
song=mixer.music.load ("asset/pop.mp3")
fond = pygame.image.load('asset/fond2.png')
fond =pygame.transform.scale(fond,(1500,800))
taille_ecran = (1500, 800)
scr = pygame.display.set_mode(taille_ecran)
fichier = open("data.txt", "r")
ms=fichier.read()
fichier.close()
sco=0
Fuse=fuse()
sp=0
gr=pygame.sprite.Group()
myfont = pygame.font.SysFont("monospace", 16)
Ob=ob
sk=time()
sk2=sk+0.5
T=time()
t=T+1
font1 = pygame.font.SysFont('pressed space for start', 72)
message = font1.render(("pressed space for start"), 100, (255, 255, 0))
def spawn():
    global sco
    y = randint(-650, -200  )
    gr.add(ob(y,gr))
    sco=sco+1
run = True
lect=False
clock = pygame.time.Clock()
skin=0
while run:
    if lect==True:
            score_display = myfont.render(("scorre:  "+str(sco)), 10, (255, 255, 0))
            mscore_display = myfont.render(("m scorre:  " + str(ms)), 10, (255, 255, 0))
            if int(sco) >= int(ms):
                ms=sco
            sk = time()
            if sk >= sk2:
                Fuse.chage_skin()
                sk2 = sk + 0.2
            if pygame.sprite.spritecollide(Fuse,gr,False,pygame.sprite.collide_mask):
                if int(ms) >= int(sco):
                    fichier = open("data.txt", "a")
                    fichier.truncate(0)
                    fichier.write(str(ms))
                    fichier.close()
                lect = False
                gr=pygame.sprite.Group()
                sco=0
            T=time()
            sp=randint(1,200)
            if T>=t:
                spawn()
                t = T +(randint(140,230)/100)
            for Ob in gr:
                Ob.mouve()
            if Fuse.rect.y <= 0:
                Fuse.rect.y =6
            if Fuse.rect.y < 660:
                Fuse.tombe()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE :
                        Fuse.monte()
                        mixer.music.play()
                else:
                    Fuse.tombe()
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            scr.blit(fond, (0, 0))
            scr.blit(Fuse.image, (Fuse.rect.x, Fuse.rect.y))
            scr.blit(score_display, (1365, 10))
            scr.blit(mscore_display, (1365, 23))
            gr.draw(scr)
            clock.tick(60)
            pygame.display.flip()
    else:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE :
                    lect=True
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        scr.blit(fond, (0, 0))
        scr.blit(message, (600, 400))
        clock.tick(60)
        pygame.display.flip()
