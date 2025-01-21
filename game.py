import pygame
import sys

class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Bubble Game')
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        i = 0
        while self.running:

            self.screen.fill((255, 255, 255))

            self.screen.blit(pygame.image.load('resources/img/bubble/bubble_lower.png'), (275, 270))

            frame = (i // 8) % 4 + 1 
            ham = pygame.image.load(f'resources/img/ham/{frame}.png')
            self.screen.blit(ham, (300, 300))
            i += 1

            self.screen.blit(pygame.image.load('resources/img/bubble/bubble_upper.png'), (275, 270))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    Game().run()