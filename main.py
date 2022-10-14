import player
import pygame
import sys
from player import *
from map import *


# class game, handles the main game loop, calls all other methods
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()
        self.get_map()
        self.get_player()

# get class player from player.py
    def get_player(self):
        self.player = Player(self)

# get class map from map.py
    def get_map(self):
        self.map = Map(self)

# updates display, writes current fps
    def update(self):
        pygame.display.flip()
        self.clock.tick(fps)
        pygame.display.set_caption(f"{self.clock.get_fps() :.1f}")

# draws map and player
    def draw(self):
        self.screen.fill('grey')
        self.map.draw()
        self.player.draw()

# checks if window should be closed
    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# main game loop, calls all other methods
    def run(self):
        while True:
            self.get_events()
            self.draw()
            self.player.update()
            self.update()


# runs program
if __name__ == '__main__':
    game = Game()
    game.run()

