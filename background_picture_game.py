
import pygame

import sys

import os

from pygame.locals import *


pygame.init()  # initialize pygame

clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 480))


# Load the background image here. Make sure the file exists!

bg = pygame.image.load(os.path.join("./", "road.jpg"))

pygame.mouse.set_visible(0)

pygame.display.set_caption('Space Age Game')


# fix indentation
while True:

    clock.tick(60)

    screen.blit(bg, (0, 0))

    x, y = pygame.mouse.get_pos()


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()


    pygame.display.update()

    class ScrollingBackground:

        def __init__(self, screenheight, imagefile):

            self.img = pygame.image.load(imagefile)

            self.coord = [0, 0]

            self.coord2 = [0, -screenheight]

            self.y_original = self.coord[1]

            self.y2_original = self.coord2[1]


        def Show(self, surface):

            surface.blit(self.img, self.coord)

            surface.blit(self.img, self.coord2)
        

        def UpdateCoords(self, speed_y, time):

            distance_y = speed_y * time

            self.coord[1] += distance_y

            self.coord2[1] += distance_y

            if self.coord2[1] >= 0:

                self.coord[1] = self.y_original

                self.coord2[1] = self.y2_original

