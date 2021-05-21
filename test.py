import numpy as np
import matplotlib as mpl
import pygame
from sys import exit
import copy
GRIDCOLOR = (0,85,255)
BLACK = (0,0,0)
LIFECOLOR = (77, 255, 0)
WIDTH, HEIGHT = 900,900
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game of Life")
FPS = 5
LIFENUM = 45
D = int(WIDTH/LIFENUM)

def drawBackgroundGrid():
    for x in range(0, WIDTH, D):
        for y in range(0, HEIGHT, D):
            rect = pygame.Rect(x,y,D,D)
            pygame.draw.rect(WIN, BLACK, rect, width = 1)


class Life:
    def __init__(self, nx, ny, status):
       self.nx = nx
       self.ny = ny
       self.status = status
       self.rect = pygame.Rect(nx*D,ny*D,D,D)
    
    def drawself(self):
        if self.status == 1:
            pygame.draw.rect(WIN, LIFECOLOR, self.rect, width = 0)
            pygame.draw.rect(WIN, BLACK, self.rect, width = 1)

lifelist = [Life(1,2,0),Life(1,3,0),Life(2,5,1)]
print(lifelist[1].status)
lifelist[1].status = 1
print(lifelist[1].status)