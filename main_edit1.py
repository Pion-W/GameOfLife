import numpy as np
#import matplotlib as mpl
import pygame
from sys import exit
import copy

pygame.init()
GRIDCOLOR = (0,85,255)
BLACK = (0,0,0)
LIFECOLOR = (77, 255, 0)
LIGHT_BLUE = (0, 168, 255)
WIDTH, HEIGHT = 800, 800
BUFFER = WIDTH//3
WIN = pygame.display.set_mode((WIDTH + BUFFER,HEIGHT))
pygame.display.set_caption("Game of Life")
FPS = 60
LIFENUM = WIDTH//20
D = int(WIDTH/LIFENUM)
#play = False

#################################################
# Classes and draw function
#################################################

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
        else:
            pygame.draw.rect(WIN, GRIDCOLOR, self.rect, width = 0)
            pygame.draw.rect(WIN, BLACK, self.rect, width = 1)

#################################################
# Game
#################################################

def update(tempallLife, num_gen):
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
    num_gen += 1
    return allLife, num_gen

def draw_text(pos, text, text_size, color, isBold):
    font = pygame.font.SysFont('arial', text_size, isBold)
    text = font.render(text, 1, color)
    WIN.blit(text, pos)

def draw_instructions_text():
    draw_text((WIDTH + BUFFER/30, 10), "INSTRUCTIONS:", 32, BLACK, True)
    draw_text((WIDTH + BUFFER/30, 5*HEIGHT/50), "Click a box to make it", 20, BLACK, False)
    draw_text((WIDTH + 3*BUFFER/30, 6*HEIGHT/50 + 10), "come alive", 20, BLACK, False)
    draw_text((WIDTH + BUFFER/30, 10*HEIGHT/50), "Press the Spacebar to run", 20, BLACK, False)
    draw_text((WIDTH + 3*BUFFER/30, 11*HEIGHT/50 + 10), "the Game of Life", 20, BLACK, False)
    draw_text((WIDTH + BUFFER/30, 16*HEIGHT/50), "Press the P key to", 20, BLACK, False)
    draw_text((WIDTH + 3*BUFFER/30, 17*HEIGHT/50 + 10), "Pause the game", 20, BLACK, False)
    draw_text((WIDTH + BUFFER/30, 22*HEIGHT/50), "Press the R key to", 20, BLACK, False)
    draw_text((WIDTH + 3*BUFFER/30, 23*HEIGHT/50 + 10), "Reset the game", 20, BLACK, False)
    draw_text((WIDTH + BUFFER/30, 28*HEIGHT/50), "Press the left Arrow key to", 20, BLACK, False)
    draw_text((WIDTH + 3*BUFFER/30, 29*HEIGHT/50 + 10), "Increment through a", 20, BLACK, False)
    draw_text((WIDTH + 3*BUFFER/30, 30*HEIGHT/50 + 20), "Generation", 20, BLACK, False)
    draw_text((WIDTH + BUFFER/30, 35*HEIGHT/50 + 20), "Number of Generations:", 20, BLACK, False)

def drawAll(allLife, num_gen):
    # draw background
    WIN.fill(LIGHT_BLUE)
    for i in range(LIFENUM):
        for j in range(LIFENUM):
            allLife[i][j].drawself()
    pygame.draw.rect(WIN, BLACK, (0,0,WIDTH,HEIGHT), width = 3)
    draw_instructions_text()
    draw_text((WIDTH + 3*BUFFER/30, 37*HEIGHT/50 + 10), str(num_gen), 20, BLACK, False)
    pygame.display.update()

def initialize():
    allLife = np.empty((LIFENUM,LIFENUM),dtype=Life)
    for i in range(LIFENUM):
        for j in range(LIFENUM):
            allLife[i][j] = Life(i,j,0)
    play = False
    num_gen = 0
    return allLife, play, num_gen

def main():
    clock = pygame.time.Clock()
    allLife, play, num_gen = initialize()

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()

            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_SPACE]:
                play = True
            if keys_pressed[pygame.K_p]:
                play = False
            if keys_pressed[pygame.K_RIGHT]:
                allLife, num_gen = update(allLife, num_gen)
            if keys_pressed[pygame.K_r]:
                allLife, play, num_gen = initialize()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for i in range(LIFENUM):
                    for j in range(LIFENUM):
                        s = allLife[i][j]
                        if pygame.Rect.collidepoint(s.rect, pos):
                            if s.status == 0:
                                s.status = 1
                            else:
                                s.status = 0
                
        drawAll(allLife, num_gen)
        if play:
            allLife, num_gen = update(allLife, num_gen)

if __name__ == "__main__":
    main()