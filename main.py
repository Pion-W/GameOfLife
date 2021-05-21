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
FPS = 120
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
            
def update(tempallLife):
    allLife = copy.deepcopy(tempallLife)
    for i in range(LIFENUM):
        for j in range(LIFENUM):
            n = ( tempallLife[(i-1)%LIFENUM][(j-1)%LIFENUM].status + tempallLife[(i-1)%LIFENUM][j].status + tempallLife[(i-1)%LIFENUM][(j+1)%LIFENUM].status
                + tempallLife[i            ][(j-1)%LIFENUM].status                                        + tempallLife[i            ][(j+1)%LIFENUM].status
                + tempallLife[(i+1)%LIFENUM][(j-1)%LIFENUM].status + tempallLife[(i+1)%LIFENUM][j].status + tempallLife[(i+1)%LIFENUM][(j+1)%LIFENUM].status )
            if tempallLife[i][j].status == 1 and (n == 2 or n == 3):
                allLife[i][j].status = 1
            elif tempallLife[i][j].status == 0 and n == 3:
                allLife[i][j].status = 1
            else:
                allLife[i][j].status = 0
    return allLife


def drawAll(allLife):
    # draw background
    WIN.fill(GRIDCOLOR)
    drawBackgroundGrid()
    for i in range(LIFENUM):
        for j in range(LIFENUM):
            allLife[i][j].drawself()

    pygame.display.update()

def initialize():
    allLife = np.empty((LIFENUM,LIFENUM),dtype=Life)
    for i in range(LIFENUM):
        for j in range(LIFENUM):
            allLife[i][j] = Life(i,j,0)
    allLife[12][10].status = 1
    allLife[10][11].status = 1
    allLife[12][11].status = 1
    allLife[12][12].status = 1
    allLife[11][12].status = 1

    allLife[21][13].status = 1
    allLife[19][14].status = 1
    allLife[20][14].status = 1
    allLife[20][15].status = 1
    allLife[21][15].status = 1
    return allLife

def main():
    clock = pygame.time.Clock()

    allLife = initialize()

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()
        drawAll(allLife)
        allLife = update(allLife)

if __name__ == "__main__":
    main()