import pygame
from pygame.draw import *
from random import randint

print('What is your name?')
name = input()
pygame.init()

image = pygame.image.load('muha.png')
razmer_muhi = 50
image = pygame.transform.scale(image, (razmer_muhi, razmer_muhi))
number_for_muha = 10
time_muhi = 5
FPS = 30
height = 450
lenght = 600
rmax = 50
rmin = 20
v_0 = 10
n_sh = 5
time_of_exist = 10
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, WHITE]

screen = pygame.display.set_mode((lenght, height + 50))


def rand_param():
    '''
    Функция выдает случайные характеристики шарика:
    координаты по осям x и y,
    радиус,
    цвет,
    проекции скорости на оси x и y
    '''    
    x1 = randint(rmax,lenght - rmax)
    y1 = randint(rmax, height - rmax)
    r1 = randint(rmin, rmax)
    v_x1 = randint(-v_0, v_0)
    v_y1 = randint(-v_0, v_0)
    color = COLORS[randint(0, 6)]
    return x1, y1, r1, color, v_x1, v_y1


def draw_ball(color2, x2, y2, r2):
    '''
    функция рисует шарик
    x2 - координата шарика по оси x
    y2 - координата шарика по оси y
    r2 - радиус шарика
    color2 - цвет шарика, заданный в формате, подходящем для pygame.Color
    '''
    circle(screen, color2, (x2, y2), r2)


def rand_v():
    '''
    функция возврашает:
    v_x2 - случайная величина ,лежащая в промежутке (-v_0, v_0)
    v_y2 - случайная величина ,лежащая в промежутке (-v_0, v_0)
    '''
    v_x2 = randint(-v_0, v_0)
    v_y2 = randint(-v_0, v_0)
    return v_x2, v_y2


def score(number_1):
    '''
    функция выводит счет number_1 на экран
    '''
    text = font.render("Score: " + str(number_1), 1, (0, 255, 0))
    place = text.get_rect(center = (lenght/2, height + 30))
    sc.blit(text, place)


pygame.mixer.music.load('polish_rap.mp3')
pygame.mixer.music.play()
pygame.display.update()
clock = pygame.time.Clock()
finished = False
number = 0
sh = []
timer = -1
odin_raz = True

sc = pygame.display.set_mode((lenght, height + 55))
sc.fill((255, 255, 255))
font = pygame.font.Font(None, 72)
    
for j in range(n_sh):
    x, y, r, color, v_x, v_y = rand_param()
    i=0
    sh.append([x, y, r, color, v_x, v_y, i])

while not finished:
    rect(screen, WHITE, (0, height, lenght, 55))
    o = number % number_for_muha
    if (o <= 1) and (number != o) and odin_raz:
        timer = 0
        odin_raz = False
        x_muhi = randint(0, lenght - razmer_muhi)
        y_muhi = randint(0, height - razmer_muhi)
    if -1 < timer < time_muhi * FPS:
        timer += 1
        v_muhi_x, v_muhi_y = rand_v()
        if x_muhi <= v_0:
            v_muhi_x = abs(v_muhi_x)
        if x_muhi >= lenght - v_0 - razmer_muhi:
            v_muhi_x = -abs(v_muhi_x)            
        if y_muhi <= v_0:
            v_muhi_y = abs(v_muhi_y)
        if y_muhi >= height - v_0 - razmer_muhi:
            v_muhi_y = -abs(v_muhi_y)
        x_muhi += v_muhi_x
        y_muhi += v_muhi_y
        rect(screen, (0, 255, 0), (0, height, lenght*(1 - timer/(time_muhi*FPS)), 5))
        image_rect = image.get_rect(topleft=(x_muhi, y_muhi))
        screen.blit(image, image_rect)

    for j in range(n_sh):
        if sh[j][6] == time_of_exist * FPS:
            sh[j][0], sh[j][1], sh[j][2], sh[j][3], sh[j][4], sh[j][5] = rand_param()
            sh[j][6] = 0
        draw_ball(sh[j][3], sh[j][0], sh[j][1], sh[j][2])

    score(number)
    pygame.display.update()
    screen.fill(BLACK)
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            with open("Scores.txt", "a") as file:
                file.write(name + ': ' + str(number) + '\n')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_m, y_m = event.pos
            if 0 < timer < time_muhi * FPS:
                if (0 < (x_m - x_muhi) < razmer_muhi) and (0 < (y_m - y_muhi) < razmer_muhi):
                    number += 5
                    timer = -1
                    odin_raz = True
            for j in range(n_sh):
                if (sh[j][0] - x_m)**2 + (sh[j][1] - y_m)**2 <= sh[j][2]**2:
                    number += 1
                    if (number % number_for_muha == 0) and (number != 0) and odin_raz:
                        timer = 0
                    score(number)
                    sh[j][0], sh[j][1], sh[j][2], sh[j][3], sh[j][4], sh[j][5] = rand_param()
                    sh[j][6] = 0
    for j in range(n_sh):
        sh[j][6] += 1
        if (sh[j][0] <= sh[j][2]) or (sh[j][0] >= lenght - sh[j][2]):
            sh[j][4] = -sh[j][4]
        if (sh[j][1] <= sh[j][2]) or (sh[j][1] >= height - sh[j][2]):
            sh[j][5] = -sh[j][5]
        sh[j][0] += sh[j][4]
        sh[j][1] += sh[j][5]

pygame.quit()