import pygame

from constants import tile as tc


class Tile:
    def __init__(self, tile_type, x=0, y=0):
        self.tile_type = tile_type
        self.x = x
        self.y = y
        self.tile_properties = tc.TILE_PROPERTIES.get(tile_type)
        self.accessible = self.tile_properties.get(tc.ACCESSIBLE)
        self.color = self.tile_properties.get(tc.FILL_COLOR)
        self.occupied_by = None

    def draw(self, screen):
        shape = pygame.Rect(self.x, self.y, tc.TILE_SIZE, tc.TILE_SIZE)
        pygame.draw.rect(screen, self.color, shape)
        # pygame.draw.rect(screen, pygame.Color('black'),
        #                  pygame.Rect(self.x, self.y, tc.TILE_SIZE, tc.TILE_SIZE), 1)
