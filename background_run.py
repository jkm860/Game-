import pygame
import sys
import os
from pygame.locals import *
# Background running
pygame.init()
screen=pygame.display.set_mode((900,900))
pygame.display.set_caption("RUN!")
bg=pygame.image.load(os.path.join("car.png"))
car= pygame.image.load(os.path.join("racing-car.png"))

clock=pygame.time.Clock()
frame=60

x,y=0,0
loop=True
while loop:
    
    for event in pygame.event.get():
        pressed=pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            loop=False
        
        
        if pressed[K_RIGHT]:
            x+=1
        if pressed[K_LEFT]:
            x-=1
        if pressed[K_DOWN]:
            y+=1
        if pressed[K_UP]:
            y-=1




    screen.fill((0,0,0))
    clock.tick(frame)
    screen.blit(car, (x,y))
    pygame.display.flip()
    



















pygame.quit()








pygame.mouse.set_visible(0)



