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
    def draw_game(self):
        self.screen.fill((0,255,170))
        self.map.draw()
        self.player.draw()
        self.draw_score()

    def draw_score(self):
        font = pygame.font.SysFont("monospace", 98)
        textsurface = font.render(str((self.player.lenght - 100) // 10), False, "black")
        self.screen.blit(textsurface, (screen_width // 2, 0))

# checks if window should be closed
    def get_events(self):
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q] or event.type == pygame.QUIT:
                pygame.quit()
                sys.exit("cgo")




# main game loop, calls all other methods
    def run(self):
        while True:
            self.get_events()
            self.draw_game()
            self.map.fruits = self.player.update(self.map.fruits)
            if len(self.map.fruits) <= max_fruits:
                self.map.spawn_fruit()
            self.update()



# runs program
if __name__ == '__main__':
    game = Game()
    game.run()

