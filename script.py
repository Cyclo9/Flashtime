""" INIT """

import os, sys
import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
FPS = 500

""" SET UP """

# Window
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Flashtime!")

# Variables
orb_x = 250
orb_y = 250

""" FUNCTIONS """

def drawOrb():
    pygame.draw.circle(win, (0, 255, 255), (orb_x, orb_y), 25)

""" MAIN LOOP """

status = True
while status:
    
    """ SET UP """

    # FPS
    clock.tick(FPS)

    # Basically, when you click `exit` it actually closes 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False

    # Key logger
    keys = pygame.key.get_pressed()

    """ OBJECT CREATION """

    # Removes remanants of drawings
    win.fill((0, 0, 0))

    # Creats Blue Orb --> Main Player
    drawOrb()

    # Velocities for moving objects
    orbVel = 1

    """ MOVEMENT """

    if keys[K_w]:
        orb_y -= orbVel
    if keys[K_a]:
        orb_x -= orbVel
    if keys[K_s]:
        orb_y += orbVel
    if keys[K_d]:
        orb_x += orbVel

    """ BOUNDARIES """

    if orb_x > 450:
        orb_x = 450
    if orb_x < 0:
        orb_x = 0
    if orb_y > 450:
        orb_y = 450
    if orb_y < 0:
        orb_y = 0

    """ WRAP UP """

    # Shows the drawings, after they are made3
    pygame.display.update()

    """ STATS """

    print("(" + str(orb_x) + ", " + str(orb_y) + ")") # Shows coordinates of the orb

pygame.quit()
