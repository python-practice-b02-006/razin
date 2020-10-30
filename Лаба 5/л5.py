import pygame
import math
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def ball1():
    global x1, y1, r1, a1
    x1 += math.floor(5 * math.cos(a1))
    y1 -= math.floor(5 * math.sin(a1))
    circle(screen, color1, (x1, y1), r1)
    if 800-x1 <= r1:
        a1 = math.pi - a1
    if y1 <= -r1:
        a1 = 2*math.pi - a1
    if x1 <= r1:
        a1 = 3*math.pi - a1
    if 800 - y1 <= r1:
        a1 = 4*math.pi - a1
        
def ball2():
    global x2, y2, r2, a2
    x2 += math.floor(5 * math.cos(a2))
    y2 -= math.floor(5 * math.sin(a2))
    circle(screen, color2, (x2, y2), r2)
    if 800-x2 <= r2:
        a2 = math.pi - a2
    if y2 <= -r2:
        a2 = 2*math.pi - a2
    if x2 <= r2:
        a2 = 3*math.pi - a2
    if 800 - y2 <= r2:
        a2 = 4*math.pi - a2
    
pygame.display.update()
clock = pygame.time.Clock()
finished = False

screen = pygame.display.set_mode((800, 800))



x1 = (randint(100,700))
y1 = randint(100,500)
r1 = randint(50,70)
a1 = 2*math.pi*randint(0, 500)/500
color1 = COLORS[randint(0, 5)]

x2 = randint(100,700)
y2 = randint(100,500)
r2 = randint(50,70)
a2 = 2*math.pi*randint(0, 500)/500
color2 = COLORS[randint(0, 5)]

score = 0
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            xm, ym = event.pos
            pygame.font.init()
            if (((xm - x1)**2 + (ym-y1)**2) <= r1**2) or (((xm - x2)**2 + (ym-y2)**2) <= r2**2):
                score += 10
                print(score)
    
    ball1()
    ball2()    
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()