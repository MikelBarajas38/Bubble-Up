import pygame

class Background:
    def __init__(self, game, size=(800, 600), tile_size=16, color=(0, 0, 0), checkered=False):
        self.game = game
        self.size = size
        self.tile_size = tile_size
        self.color = color
        self.checkered = checkered

    def render(self, surf):

        if not self.checkered:
            surf.fill(self.color)
            return
        
        for y in range(0, self.size[1], self.tile_size):
            for x in range(0, self.size[0], self.tile_size):
                if (x // self.tile_size) % 2 == (y // self.tile_size) % 2:
                    pygame.draw.rect(surf, self.color, (x, y, self.tile_size, self.tile_size))


class Tile:
    def __init__(self, game, x, y, tile_size=16, color=(255, 255, 255)):
        self.game = game
        self.x = x
        self.y = y
        self.tile_size = tile_size
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def render(self, surf):
        surf.blit(self.image, self.rect.topleft)

class Tilemap:
    def __init__(self, game, tile_size=16, size=(800, 600)):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}

        for y in range(0, 1, tile_size):
            for x in range(0, 32, tile_size):
                    print(f'Creating tile at {x}, {y}')
                    self.tilemap[(x, y)] = Tile(game, x, y, tile_size, (81, 165, 168))

    def render(self, surf):
        for tile in self.tilemap:
            self.tilemap[tile].render(surf)


    