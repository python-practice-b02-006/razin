import pygame
from pygame.draw import *
import numpy as np


clock = pygame.time.Clock()
pygame.init()
FPS = 30


# цвета
purple = (140, 78, 148)
yellow = (255, 255, 0)
red = (155, 30, 30)
orange = (250, 150, 0)
light_yellow = (240, 187, 74)
pink = (255, 199, 199)

# размеры
SCALE = 0.5
SCREEN_WIDTH = round(2500 * SCALE)
SCREEN_HEIGHT = round(1667 * SCALE)
SUN_RADIUS = round(140 * SCALE)

# цвета частей
SUN_COLOR = yellow
BACKGROUND_1_COLOR = light_yellow
BACKGROUND_2_COLOR = pink
BACKGROUND_3_COLOR = light_yellow
BACKGROUND_4_COLOR = purple
MOUNTAINS_1_COLOR = orange
MOUNTAINS_2_COLOR = red

# расположение частей
SUN_POSITION = round(1175 * SCALE), round(360 * SCALE)
BACKGROUND_2_POSITION = round(360 * SCALE)
BACKGROUND_3_POSITION = round(715 * SCALE)
BACKGROUND_4_POSITION = round(1100 * SCALE)
MOUNTAINS_1_COORDINATES = [[0, 776], [0, 678], [514, 330], [608, 357], [652, 419],
                           [960, 629], [1127, 603], [1211, 648], [1335, 529], [1440, 554],
                           [1501, 500], [1819, 264], [1869, 305], [1982, 411],
                           [2072, 392], [2242, 476], [2325, 430], [2500, 517], [0, 776]]
MOUNTAINS_2_COORDINATES = [[0, 832], [64, 864], [221, 669], [433, 1066], [545, 879],
                           [721, 974], [800, 752], [1021, 800], [1200, 932], [1433, 884],
                           [1712, 680], [2041, 883], [2152, 750], [2254, 821],
                           [2304, 740], [2402, 750], [2500, 590], [2500, 1074], [0, 1129]]

# масштабирование координат гор
for point in MOUNTAINS_1_COORDINATES:
    point[0] = round(point[0] * SCALE)
    point[1] = round(point[1] * SCALE)
for point in MOUNTAINS_2_COORDINATES:
    point[0] = round(point[0] * SCALE)
    point[1] = round(point[1] * SCALE)

# экран
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# задний фон
rect(screen, BACKGROUND_1_COLOR, (0, 0, SCREEN_WIDTH, BACKGROUND_2_POSITION - 0))
rect(screen, BACKGROUND_2_COLOR, (0, BACKGROUND_2_POSITION,
                                  SCREEN_WIDTH, BACKGROUND_3_POSITION - BACKGROUND_2_POSITION))
rect(screen, BACKGROUND_3_COLOR, (0, BACKGROUND_3_POSITION,
                                  SCREEN_WIDTH, BACKGROUND_4_POSITION - BACKGROUND_3_POSITION))
rect(screen, BACKGROUND_4_COLOR, (0, BACKGROUND_4_POSITION,
                                  SCREEN_WIDTH, SCREEN_HEIGHT - BACKGROUND_2_POSITION))

# горы
polygon(screen, MOUNTAINS_1_COLOR, MOUNTAINS_1_COORDINATES)
polygon(screen, MOUNTAINS_2_COLOR, MOUNTAINS_2_COORDINATES)

# Солнце
circle(screen, SUN_COLOR, SUN_POSITION, SUN_RADIUS)


pygame.display.update()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()