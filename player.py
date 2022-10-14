import pygame
import math
import main
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
        if keys[pygame.K_RIGHT]:
            self.angle += player_rotation_speed * self.delta_time
        if keys[pygame.K_LEFT]:
            self.angle -= player_rotation_speed * self.delta_time
        #claculates the margin the snake will move
        dx = math.cos(self.angle) * player_speed * self.delta_time
        dy = math.sin(self.angle) * player_speed * self.delta_time

        self.angle %= math.tau
        self.collision(dx, dy)
        #self.check_for_trail()
        self.move(dx, dy)

# moves the snake
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

# draws the snake
    def draw(self):
        [pygame.draw.circle(self.game.screen, 'red', (pos[0] * 100, pos[1] * 100), 15) for pos in self.trail]
        pygame.draw.line(self.game.screen, 'purple', (self.x * 100, self.y * 100),
                         (self.x * 100 + screen_width * math.cos(self.angle),
                          (self.y * 100 + screen_height * math.sin(self.angle))), 2)
        pygame.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)

# check if the player will crash into a wall
    def check_for_wall(self, x, y):
        return (x, y) in self.game.map.world_map

    # checks if the snake will crash into his tail - not done yet
    def check_for_trail(self):
        moy, mox = 0, 0
        for i in self.trail:
            mox, moy = 0, 0
            if self.trail[i][0] > self.x and self.trail[i][0] < self.x + 10:
                mox = 1
            if self.trail[i][0] < self.x and self.trail[i][0] > self.x + 10:
                mox = 1
            if self.trail[i][1] > self.y and self.trail[i][1] < self.y + 10:
                moy = 1
            if self.trail[i][1] < self.y and self.trail[i][1] > self.y + 10:
                moy = 1
        if mox == 1 and moy == 1:
            sys.exit()

# closes the game if snake crashes into a wall
    def collision(self, dx, dy):
        if self.check_for_wall((int(self.x + dx)), int(self.y)):
            sys.exit()
        if self.check_for_wall((int(self.x)), int(self.y + dy)):
            sys.exit()

# calls movement, updates delta time variable, adds elemnts to trail, lenghtens snake - bcs the food does not work
    def update(self):
        self.delta_time = (pygame.time.get_ticks() - self.prev_tics)
        self.prev_tics = pygame.time.get_ticks()
        self.movement()
        self.make_trail()
        self.lenght += 0.1

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