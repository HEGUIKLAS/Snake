import random
from settings import *
import pygame
# defines map, o is a clear space, 1 is a wall
o = False
room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, o, o, o, o, o, o, o, o, o, o, o, o, 1],
    [1, o, o, o, o, o, o, o, o, o, o, o, o, 1],
    [1, o, o, o, o, o, o, o, o, o, o, o, o, 1],
    [1, o, o, o, o, o, 1, o, o, o, o, o, 1, 1],
    [1, o, o, o, o, o, o, o, o, o, o, o, o, 1],
    [1, o, o, o, o, o, o, o, o, o, o, o, o, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class Map:

    def __init__(self, game):
        self.game = game
        self.room_map = room_map
        self.world_map = {}
        self.get_map()
        self.fruits = [(0, 0)]

# transforms map into a list of walls and coordinates
    def get_map(self):
        for j, row in enumerate(self.room_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

# spawns fruit
    def spawn_fruit(self):
        self.fruits.append((random.randint(0, screen_height), random.randint(0, screen_width)))

# draws map and fruits on the screen
    def draw(self):
        [pygame.draw.rect(self.game.screen, 'black', (pos[0] * 100, pos[1] * 100, 100, 100), 0)
            for pos in self.world_map]
        [pygame.draw.circle(self.game.screen, "green", (pos[0], pos[1]), 15) for pos in self.fruits]




