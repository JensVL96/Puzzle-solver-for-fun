import pygame as pg
from pygame import event

class Input_handler():
    def __init__(self):
        pass

    def event_keys(self, val):
        if event.key == pygame.K_1:
            val = 1
        if event.key == pygame.K_2:
            val = 2
        if event.key == pygame.K_3:
            val = 3
        if event.key == pygame.K_4:
            val = 4
        if event.key == pygame.K_5:
            val = 5
        if event.key == pygame.K_6:
            val = 6
        if event.key == pygame.K_7:
            val = 7
        if event.key == pygame.K_8:
            val = 8
        if event.key == pygame.K_9:
            val = 9

        return val