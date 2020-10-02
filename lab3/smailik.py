import pygame
from pygame.draw import *
import numpy as np


clock = pygame.time.Clock()
pygame.init()
FPS = 30


# цвета
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)
grey = (200, 200, 200)


# размеры
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SMILE_RADIUS = 100
LEFT_EYE_RADIUS = 20
RIGHT_EYE_RADIUS = 15
PUPIL_RADIUS = 7
EYEBROW_LENGTH = 100
EYEBROW_WIDTH = 10
MOUTH_LENGTH = 100
MOUTH_WIDTH = 20


# цвета частей
SCREEN_COLOR = grey
SMILE_COLOR = yellow
EYEBROW_COLOR = black
MOUTH_COLOR = black
PUPIL_COLOR = black
EYE_COLOR = red


# расположение частей
SMILE_POSITION = 200, 200
MOUTH_POSITION = 150, 250
LEFT_EYE_POSITION = 150, 180
RIGHT_EYE_POSITION = 250, 180
LEFT_PUPIL_POSITION = 150, 180
RIGHT_PUPIL_POSITION = 250, 180
LEFT_EYEBROW_POSITION = 102, 126
RIGHT_EYEBROW_POSITION = 218, 175
LEFT_EYEBROW_ANGLE = 32*np.pi/180
RIGHT_EYEBROW_ANGLE = -16*np.pi/180


# функция, рисующая наклонный прямоугольник
def inc_rect(screen, color, x, y, length, width, theta):
    polygon(screen, color, [(x, y), (x + round(length*np.cos(theta)), y + round(length*np.sin(theta))),
                            (x + round(length*np.cos(theta) + width*np.sin(theta)),
                             y + round(length*np.sin(theta) - width*np.cos(theta))),
                            (x + round(width*np.sin(theta)),
                             y - round(width*np.cos(theta))),
                            (x, y)])


# экран
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(SCREEN_COLOR)

# голова
circle(screen, SMILE_COLOR, SMILE_POSITION, SMILE_RADIUS)

# рот
rect(screen, MOUTH_COLOR,
     (MOUTH_POSITION[0], MOUTH_POSITION[1], MOUTH_LENGTH, MOUTH_WIDTH))

# глаза
circle(screen, EYE_COLOR, LEFT_EYE_POSITION, LEFT_EYE_RADIUS)
circle(screen, EYE_COLOR, RIGHT_EYE_POSITION, RIGHT_EYE_RADIUS)
circle(screen, PUPIL_COLOR, LEFT_PUPIL_POSITION, PUPIL_RADIUS)
circle(screen, PUPIL_COLOR, RIGHT_PUPIL_POSITION, PUPIL_RADIUS)

# брови
inc_rect(screen, EYEBROW_COLOR, LEFT_EYEBROW_POSITION[0], LEFT_EYEBROW_POSITION[1],
         EYEBROW_LENGTH, EYEBROW_WIDTH, LEFT_EYEBROW_ANGLE)
inc_rect(screen, EYEBROW_COLOR, RIGHT_EYEBROW_POSITION[0], RIGHT_EYEBROW_POSITION[1],
         EYEBROW_LENGTH, EYEBROW_WIDTH, RIGHT_EYEBROW_ANGLE)


pygame.display.update()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()