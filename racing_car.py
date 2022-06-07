import pygame
import sys
import os
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((500,480))
# Background

pygame.display.set_caption("Racing Car")
bg=pygame.image.load(os.path.join("road.jpg"))
###########""

car= pygame.image.load(os.path.join("racing-car.png"))

clock=pygame.time.Clock()
frame=50000

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
        



    screen.fill((0,0,0))
    screen.blit(bg, (0,0))
    #clock.tick(frame)
    
    pygame.display.flip()
    



















pygame.quit()








pygame.mouse.set_visible(0)



