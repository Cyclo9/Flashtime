""" INIT """

import os, sys
import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
FPS = 400

""" SET UP """

# Window
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Flashtime!")

# Text for countdown
font = pygame.font.SysFont("arial", 15, bold = True)
text = font.render("Hello, World", True, (0, 0, 0))

""" VARIABLES """

# Orb Position
orb_x = 250
orb_y = 250

# Background Image
bgImg = pygame.image.load("lib/img/background.png")

""" FUNCTIONS """

# Drawings

# The Orb - It represents a little Time Orb
def drawOrb():
    pygame.draw.circle(win, (0, 255, 255), (orb_x, orb_y), 25)

# Doors
def drawDoors():
    pygame.draw.rect(win, (139, 69, 19), (0, 200, 16, 100))
    pygame.draw.rect(win, (139, 69, 19), (200, 0, 100, 16))
    pygame.draw.rect(win, (139, 69, 19), (484, 200, 16, 100))
    pygame.draw.rect(win, (139, 69, 19), (200, 484, 100, 16))

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
    win.blit(bgImg, (0, 0))
    
    # Countdown Timer
    
    win.blit(text, (460, 460) )
    
    # win.fill((0, 0, 0)) # <-- Backup
 
    # Creats Blue Orb --> Main Player
    drawOrb()

    # Draws doors
    drawDoors()

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

    # Wall Boundaries
    if orb_x > 459:
        orb_x = 459
    if orb_x < 41:
        orb_x = 41
    if orb_y > 459:
        orb_y = 459
    if orb_y < 41:
        orb_y = 41

    """ WRAP UP """

    # Shows the drawings, after they are made3
    pygame.display.update()

    """ STATS """

    print("(" + str(orb_x) + ", " + str(orb_y) + ")") # Shows coordinates of the orb
    
pygame.quit()
