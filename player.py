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
        [pygame.draw.circle(self.game.screen, "black", (pos[0] * 100, pos[1] * 100), 16) for i, pos in enumerate(self.trail)]
        [pygame.draw.circle(self.game.screen, colors[(i % len(colors))], (pos[0] * 100, pos[1] * 100), 15) for i, pos in enumerate(self.trail)]
        pygame.draw.circle(self.game.screen, 'yellow', (self.x * 100, self.y * 100), 15)

# check if the player will crash into a wall
    def check_for_wall(self, x, y):
        return (x, y) in self.game.map.world_map

    def check_for_fruit(self, fruits):

        for x, i in enumerate(fruits):
            moy, mox = False, False
            if abs(abs(i[0]) - abs(self.x)) <= 0.2:
                mox = True
            if abs(abs(i[1]) - abs(self.y)) <= 0.2:
                moy = True
            if mox is True and moy is True:
                self.lenght += 10
                fruits.pop(x)
        return fruits

    # checks if the snake will crash into his tail - not done yet
    def check_for_trail(self):
        for i in self.trail[:-20]:
            moy, mox = False, False
            if abs(abs(i[0]) - abs(self.x)) <= 0.2:
                mox = True
            if abs(abs(i[1]) - abs(self.y)) <= 0.2:
                moy = True
            if mox is True and moy is True:
                self.game.endscreen()


# closes the game if snake crashes into a wall
    def collision(self, dx, dy):
        if self.check_for_wall((int(self.x + dx)), int(self.y)):
            self.game.endscreen()
        if self.check_for_wall((int(self.x)), int(self.y + dy)):
            self.game.endscreen()

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