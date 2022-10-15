import pygame
import math
import random
from map import Map
from settings import *
import sys


class Player:
    def __init__(self, game):

        self.game = game
        self.x, self.y = player_pos
        self.angle = player_angle
        self.prev_tics = pygame.time.get_ticks()
        self.trail = []
        self.lenght = 100

# moves the player, calls collision method
    def movement(self):
        # check which keys are pressed
        keys = pygame.key.get_pressed()
        # changes player angle
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.angle += player_rotation_speed * self.delta_time
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.angle -= player_rotation_speed * self.delta_time

        # claculates the margin the snake will move

        dx = math.cos(self.angle) * player_speed * self.delta_time
        dy = math.sin(self.angle) * player_speed * self.delta_time

        self.angle %= math.tau
        self.collision(dx, dy)
        self.check_for_trail()
        self.move(dx, dy)


# moves the snake
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

# draws the snake
    def draw(self):
        [pygame.draw.circle(self.game.screen, colors[(i % len(colors))], (pos[0] * 100, pos[1] * 100), 15) for i, pos in enumerate(self.trail)]
#       pygame.draw.line(self.game.screen, 'purple', (self.x * 100, self.y * 100),
#                        (self.x * 100 + screen_width * math.cos(self.angle),
#                          (self.y * 100 + screen_height * math.sin(self.angle))), 2)
        pygame.draw.circle(self.game.screen, 'violet', (self.x * 100, self.y * 100), 15)

# check if the player will crash into a wall
    def check_for_wall(self, x, y):
        return (x, y) in self.game.map.world_map

    def check_for_fruit(self, fruits):
        for x, i in enumerate(fruits):
            moy, mox = False, False
            if (i[0] / 100) < self.x and (i[0] / 100) > self.x + 0.2:
                mox = True
            if (i[0] / 100) < self.x and (i[0] / 100) > self.x - 0.2:
                mox = True
            if (i[1] / 100) < self.y and (i[1] / 100) > self.y + 0.2:
                moy = True
            if (i[1] / 100) < self.y and (i[1] / 100) > self.y - 0.2:
                moy = True
            if mox is True and moy is True:
                print(f"snx {self.x} sny {self.y}  tx {i[0]}  ty {i[1]}")
                self.lenght += 100
                fruits.pop(x)
        return fruits


    # checks if the snake will crash into his tail - not done yet
    def check_for_trail(self):
        for i in self.trail[:-20]:
            moy, mox = False, False
            if i[0] < self.x and i[0] > self.x + 0.1:
                mox = True
            if i[0] < self.x and i[0] > self.x - 0.1:
                mox = True
            if i[1] < self.y and i[1] > self.y + 0.1:
                moy = True
            if i[1] < self.y and i[1] > self.y - 0.1:
                moy = True
            if mox is True and moy is True:
                print(f"snx {self.x} sny {self.y}  tx {i[0]}  ty {i[1]}")
                sys.exit()

# closes the game if snake crashes into a wall
    def collision(self, dx, dy):
        if self.check_for_wall((int(self.x + dx)), int(self.y)):
            sys.exit()
        if self.check_for_wall((int(self.x)), int(self.y + dy)):
            sys.exit()

# calls movement, updates delta time variable, adds elemnts to trail, lenghtens snake - bcs the food does not work
    def update(self, fruits):
        self.delta_time = (pygame.time.get_ticks() - self.prev_tics)
        self.prev_tics = pygame.time.get_ticks()
        self.movement()
        fruits = self.check_for_fruit(fruits)
        self.make_trail()
        return fruits


# handles array with snake tail coordinartes
    def make_trail(self):
        self.trail.append((self.x, self.y))
        while len(self.trail) > self.lenght:
            del self.trail[0]


    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)