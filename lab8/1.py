import pygame as pg
import numpy as np
from random import randint

SCREEN_SIZE = (800, 600)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pg.init()


class Ball():
    """
    Создаёт мячи, управляет их движениями и цветом
    """
    def __init__(self, coord, vel, rad=15, color=None):
        if color == None:
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.color = color
        self.coord = coord
        self.vel = vel
        self.rad = rad
        self.is_alive = True

    def draw(self, screen):
        """
        Рисует мяч на экране.
        """
        pg.draw.circle(screen, self.color, self.coord, self.rad)

    def move(self, t_step=1., g=2.):
        """
        Перемещает мяч. Скорость мяча также изменяется под действием силы тяжести.
        """
        self.vel[1] += int(g * t_step)
        for i in range(2):
            self.coord[i] += int(self.vel[i] * t_step)
        self.check_walls()
        if self.vel[0]**2 + self.vel[1]**2 < 2**2 and self.coord[1] > SCREEN_SIZE[1] - 2*self.rad:
               self.is_alive = False

    def check_walls(self):
        """
        Проверяет, столкнулся ли мяч со стенами, и вызывает метод flip_vel для изменения его скорости, если это произошло.
        """
        n = [[1, 0], [0, 1]]
        for i in range(2):
            if self.coord[i] < self.rad:
                self.coord[i] = self.rad
                self.flip_vel(n[i], 0.8, 0.9)
            elif self.coord[i] > SCREEN_SIZE[i] - self.rad:
                self.coord[i] = SCREEN_SIZE[i] - self.rad
                self.flip_vel(n[i], 0.8, 0.9)

    def flip_vel(self, axis, coef_perp=1., coef_par=1.):
        """
        Изменяет скорость шара, как если бы он неупруго столкнулся со стенкой с нормальным вектором «axis».
        """
        vel = np.array(self.vel)
        n = np.array(axis)
        n = n / np.linalg.norm(n)
        vel_perp = vel.dot(n) * n
        vel_par = vel - vel_perp
        ans = -vel_perp * coef_perp + vel_par * coef_par
        self.vel = ans.astype(np.int).tolist()


class Table():
    """
    Управляет подсчетом очков и показом их игроку.
    """
    def __init__(self, targets_hit=0, balls_used=0):
        self.targets_hit = targets_hit
        self.balls_used = balls_used
        self.score = max(0, self.targets_hit - self.balls_used)

    def draw(self, screen):
        self.score = max(0, self.targets_hit - self.balls_used)

        font = pg.font.SysFont('Arial', 30)

        text_targets_hit = font.render("Поражено мишений: " + str(self.targets_hit),
                                       False, (200, 200, 200))
        text_balls_used = font.render("Использовано мячей: " + str(self.balls_used),
                                      False, (200, 200, 200))
        text_score = font.render("Счёт: " + str(self.score),
                                 False, (200, 200, 200))
        screen.blit(text_targets_hit, (0, 0))
        screen.blit(text_balls_used, (0, 50))
        screen.blit(text_score, (0, 100))


class Gun():
    """
    Создает пушку, управляет её движениями, стрельбой, прицеливанием и рендерингом.
    """
    def __init__(self, coord=[30, SCREEN_SIZE[1]//2], 
                 min_pow=20, max_pow=50):
        """
        Создает пушку с заданными начальными условиями.
        """
        self.coord = coord
        self.angle = 0
        self.min_pow = min_pow
        self.max_pow = max_pow
        self.power = min_pow
        self.active = False

    def draw(self, screen):
        """
        Рисует пушку на экране.
        """
        end_pos = [self.coord[0] + self.power*np.cos(self.angle), 
                   self.coord[1] + self.power*np.sin(self.angle)]
        pg.draw.line(screen, RED, self.coord, end_pos, 5)

    def strike(self):
        """
        Создает мяч. Скорость полета мяча зависит от того, куда направлено ружье и сколько у него мощности.
        """
        vel = [int(self.power * np.cos(self.angle)), int(self.power * np.sin(self.angle))]
        self.active = False
        self.power = self.min_pow
        return Ball(list(self.coord), vel)
        
    def move(self):
        """
        Изменяет мощность оружия.
        """
        if self.active and self.power < self.max_pow:
            self.power += 1

    def set_angle(self, mouse_pos):
        """
        Изменяет угол наклона пушки.
        """
        self.angle = np.arctan2(mouse_pos[1] - self.coord[1], 
                                mouse_pos[0] - self.coord[0])


class Target():
    """
    Создает мишени, управляет их столкновениями с шарами, рендерингом.
    """
    def __init__(self, coord, rad=30, color=None):
        """
        Создает мишень с заданными начальными условиями.
        """
        if color is None:
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.color = color
        self.coord = coord
        self.rad = rad
        self.is_alive = True

    def draw(self, screen):
        """
        Рисует мишень на экране.
        """
        pg.draw.circle(screen, self.color, self.coord, self.rad)

    def check_collision(self, ball):
        """
        Проверяет, столкнулся ли мяч с мишенью.
        """
        distance = (sum((ball.coord[i] - self.coord[i])**2 for i in range(2)))**0.5
        return distance <= self.rad + ball.rad


class Manager():
    """
    Управляет процессом игры.
    """
    def __init__(self):
        """
        Создает игру: пушки, шары, мишени и таблицу очков. Создает переменные для отслеживания состояния игры.
        """
        self.gun = Gun()
        self.table = Table()
        self.balls = []
        self.targets = []

        self.done = False
        self.up_key_pressed = False
        self.down_key_pressed = False
    
    def process(self, events, screen):
        """
        Управляет игрой. Если все цели были поражены, создает новые.
        """
        self.handle_events(events)

        if len(self.targets) == 0 and len(self.balls) == 0:
            radius = max(int(30 - self.table.score), 3)
            self.targets = [Target([randint(100, SCREEN_SIZE[0] - 30),
                                    randint(30, SCREEN_SIZE[1] - 30)],
                                   rad=radius) for i in range(3)]

        self.check_collisions()
        self.check_alive()
        self.move()
        self.draw(screen)
        return done

    def draw(self, screen):
        """
        Рисует все объекты, которые нужно нарисовать на экране.
        """
        screen.fill(BLACK)
        self.gun.draw(screen)
        for ball in self.balls:
            ball.draw(screen)
        for target in self.targets:
            target.draw(screen)
        self.table.draw(screen)

    def move(self):
        """
        Перемещает все объекты, которые нужно переместить.
        """
        for ball in self.balls:
            ball.move()
        self.gun.move()

    def check_alive(self):
        """
        Проверяет, движутся ли мячи и не поражены ли ещё мишени.
        """
        dead_balls = []
        for i, ball in enumerate(self.balls):
            if not ball.is_alive:
                dead_balls.append(i)

        for i in reversed(dead_balls):
            self.balls.pop(i)
            
    def check_collisions(self):
        """
        Проверяет, попали ли мячи в какие-то мишени.
        """
        for target in self.targets:
            for ball in self.balls:
                if target.check_collision(ball):
                    target.is_alive = False
                    self.table.targets_hit += 1
    
    def handle_events(self, events):
        """
        Обрабатывает события.
        """
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.gun.coord[1] -= 5
                elif event.key == pg.K_DOWN:
                    self.gun.coord[1] += 5
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.gun.active = True
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self.balls.append(self.gun.strike())
                    self.table.balls_used += 1
                    
        if pg.mouse.get_focused():
            mouse_pos = pg.mouse.get_pos()
            self.gun.set_angle(mouse_pos)

        return done


screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("Пушка Хирьянова")
clock = pg.time.Clock()

mgr = Manager()

done = False

while not done:
    clock.tick(15)

    done = mgr.process(pg.event.get(), screen)

    pg.display.flip()