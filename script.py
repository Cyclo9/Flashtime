# Init
import os, sys
import pygame
from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()
FPS = 500

# Window
win = pygame.display.set_mode((500, 500))

# Variables
rect1x = 50
rect1y = 50

rect2x = 110
rect2y = 50

# Main Loop
status = True
while status:
    
    # FPS
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False

    keys = pygame.key.get_pressed()

    rect1Vel = 1

    if keys[K_LEFT]:
        rect1x -= rect1Vel
    if keys[K_RIGHT]:
        rect1x += rect1Vel
    if keys[K_DOWN]:
        rect1y += rect1Vel
    if keys[K_UP]:
        rect1y -= rect1Vel

    # Boundaries

    if rect1x > 450:
        rect1x = 450
    if rect1y > 450:
        rect1y = 450
    if rect1x < 0:
        rect1x = 0
    if rect1y < 0:
        rect1y = 0

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 255), (rect1x, rect1y, 50, 50))
    pygame.display.update()

    print("(" + str(rect1x) + ", " + str(rect1y) + ")") # Shows coordinates of rect1

pygame.quit()
