import pygame

from constants import tile as tc
from merps.merp import Merp


class Tile:
    def __init__(self, tile_type, x=0, y=0):
        self.tile_type = tile_type
        self.x = x
        self.y = y
        self.tile_map_x = int(self.x / tc.TILE_SIZE)
        self.tile_map_y = int(self.y / tc.TILE_SIZE)
        self.tile_properties = tc.TILE_PROPERTIES.get(tile_type)
        self.accessible = self.tile_properties.get(tc.ACCESSIBLE)
        self.color = self.tile_properties.get(tc.FILL_COLOR)
        self.occupied_by = None

    def draw(self, screen):
        shape = pygame.Rect(self.x, self.y, tc.TILE_SIZE, tc.TILE_SIZE)
        pygame.draw.rect(screen, self.color, shape)

        if self.occupied_by is not None and isinstance(self.occupied_by, Merp):
            self.occupied_by.draw(screen)
