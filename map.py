import random
from settings import *
import pygame
# defines map, o is a clear space, 1 is a wall
o = False
room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, o, o, o, o, o, o, o, o, 1, o, o, o, 1],
    [1, o, o, o, o, o, o, o, o, o, o, o, o, 1],
    [1, o, o, 1, o, o, o, o, o, o, o, o, o, 1],
    [1, o, o, o, o, o, 1, o, o, o, o, o, 1, 1],
    [1, o, o, o, o, o, o, o, o, o, o, o, o, 1],
    [1, o, o, 1, o, o, o, o, o, o, o, o, o, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class Map:

    def __init__(self, game):
        self.game = game
        self.room_map = room_map
        self.world_map = {}
        self.fruit_space = []
        self.get_map()
        self.get_fruit_space()
        self.fruits = [(0, 0)]

# transforms map into a list of walls and coordinates
    def get_map(self):
        for j, row in enumerate(self.room_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def get_fruit_space(self):
        for j, row in enumerate(self.room_map):
            for i, value in enumerate(row):
                if not value:
                    self.fruit_space.append((i, j))

# spawns fruit
    def spawn_fruit(self):
        x = random.choice(self.fruit_space)
        self.fruits.append((x[0] + (random.randint(150, 850) / 1000), (x[1] + (random.randint(150, 850) / 1000))))

# draws map and fruits on the screen
    def draw(self):
        [pygame.draw.rect(self.game.screen, "gray", (pos[0] * 100, pos[1] * 100, 100, 100), 0)
            for pos in self.world_map]
        [pygame.draw.circle(self.game.screen, "black", (pos[0] * 100, pos[1] * 100), 16) for pos in self.fruits]
        [pygame.draw.circle(self.game.screen, "red", (pos[0] * 100, pos[1] * 100), 15) for pos in self.fruits]



