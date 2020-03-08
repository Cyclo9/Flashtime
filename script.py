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
rect1_x = 50
rect1_y = 50

rect2_x = 110
rect2_y = 50

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

    # Draws a rectangle --> rect1
    pygame.draw.rect(win, (255, 255, 255), (rect1_x, rect1_y, 50, 50))
    
    # Draws a 2nd rectangle --> rect2
    pygame.draw.rect(win, (0, 225, 255), (rect2_x, rect2_y, 50, 50))

    # Velocities for moving objects
    rect1Vel = 1
    rect2Vel = 1

    """ MOVEMENT """

    # Keys for moving rectangle 1

    if keys[K_LEFT]:
        rect1_x -= rect1Vel
    if keys[K_RIGHT]:
        rect1_x += rect1Vel
    if keys[K_DOWN]:
        rect1_y += rect1Vel
    if keys[K_UP]:
        rect1_y -= rect1Vel

    # Keys for moving rectangle 2

    if keys[K_w]:
        rect2_y -= 1
    if keys[K_a]:
        rect2_x -= 1
    if keys[K_s]:
        rect2_y += 1
    if keys[K_d]:
        rect2_x += 1

    """ BOUNDARIES """

    # Boundaries for rectangle 1

    if rect1_x > 450:
        rect1_x = 450
    if rect1_y > 450:
        rect1_y = 450
    if rect1_x < 0:
        rect1_x = 0
    if rect1_y < 0:
        rect1_y = 0

    # Boundaries for rectangle 2

    if rect2_x > 450:
        rect2_x = 450
    if rect2_y > 450:
        rect2_y = 450
    if rect2_x < 0:
        rect2_x = 0
    if rect2_y < 0:
        rect2_y = 0

    # Shows the drawings, after they are made3
    pygame.display.update()

    """ STATS """

    print("(" + str(rect1_x) + ", " + str(rect1_y) + ")" + " " + "(" + str(rect2_x) + ", " + str(rect2_y) + ")") # Shows coordinates of rect1

pygame.quit()
