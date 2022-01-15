import pygame

import random
import os
import time
import visualize
import pickle

print("Set to go")

pygame.init()
win = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("The Game Dawg")

x, y = 50, 50
width, height = 40, 60
velocity = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > velocity:
        x -= velocity
    if keys[pygame.K_RIGHT] and x < 1000-width-velocity:
        x += velocity
    if keys[pygame.K_UP] and y>0:
        y -= velocity
    if keys[pygame.K_DOWN] and y<500-width-velocity:
        y += velocity

    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
pygame.quit()


