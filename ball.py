import pygame
from pygame.draw import *
from random import randint

pygame.init()

number_of_balls = 10
FPS = 100

width = 1200
height = 800
screen = pygame.display.set_mode((width, height))


class Balls:
    def __init__(self):
        self.x = randint(100, width - 100)
        self.y = randint(100, height - 100)
        self.r = randint(40, 80)
        self.color = [randint(0, 255), randint(0, 255), randint(0, 255)]
        self.x_speed = randint(-500, 500) / 100
        self.y_speed = randint(-500, 500) / 100
        circle(screen, self.color, (self.x, self.y), self.r)

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        self.y_speed += randint(-20, 20) / 100
        self.x_speed += randint(-20, 20) / 100
        circle(screen, self.color, (self.x, self.y), self.r)

    def reflection(self):
        if self.x >= width - self.r or self.x <= self.r:
            self.x_speed *= -1
        if self.y >= height - self.r or self.y <= self.r:
            self.y_speed *= -1

    def click(self, event):
        return (event.pos[0] - self.x) ** 2 + (event.pos[1] - self.y) ** 2 <= self.r ** 2


clock = pygame.time.Clock()
game_balls = [Balls() for i in range(number_of_balls)]
counter = 0
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            for ball in game_balls:
                if ball.click(event):
                    game_balls.remove(ball)
                    game_balls.append(Balls())
                    counter += 1

    for ball in game_balls:
        ball.update()
        ball.reflection()
    pygame.display.update()
    screen.fill((0, 0, 0))

print('У Вас ' + str(counter) + ' очков(-а)!')

pygame.quit()
