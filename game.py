import player
import pygame
import sys
from player import *
from map import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()
        self.get_map()
        self.get_player()


    def get_player(self):
        self.player = Player(self)

    def get_map(self):
        self.map = Map(self)

    def update(self):
        pygame.display.flip()
        self.clock.tick(fps)
        pygame.display.set_caption(f"{self.clock.get_fps() :.1f}")

    def draw(self):
        self.screen.fill('grey')
        self.map.draw()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.get_events()
            self.draw()
            self.player.update()
            self.player.movement()
            self.player.draw()
            self.update()




