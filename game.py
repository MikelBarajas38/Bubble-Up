import pygame
import sys

from scripts.level import Tilemap, Background

class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Bubble Game')
        self.screen = pygame.display.set_mode((1600, 1200))
        self.clock = pygame.time.Clock()
        self.running = True
        self.tile_size = 64

        self.background = Background(self, (1600, 1200), self.tile_size, (232, 229, 244), True)
        print(self.background.checkered)
        self.tilemap = Tilemap(self, self.tile_size, (1600, 1200))

    def run(self):

        while self.running:

            self.screen.fill((255, 255, 255))
            self.background.render(self.screen)
            self.tilemap.render(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    Game().run()