import pygame

from constants import tile as tc
from map.coordinates import Coordinates
from merps.merp import Merp


class Tile:
    def __init__(self, tile_type, x=0, y=0):
        self.tile_type = tile_type
        self.coordinates = Coordinates(x, y)
        self._tile_map_x = int(self.coordinates.x / tc.TILE_SIZE)
        self._tile_map_y = int(self.coordinates.y / tc.TILE_SIZE)
        self.tile_map_coordinates= Coordinates(self._tile_map_x, self._tile_map_y)
        self.tile_properties = tc.TILE_PROPERTIES.get(tile_type)
        self.accessible = self.tile_properties.get(tc.ACCESSIBLE)
        self.color = self.tile_properties.get(tc.FILL_COLOR)
        self.occupied_by = None

    def draw(self, screen):
        shape = pygame.Rect(self.coordinates.x, self.coordinates.y, tc.TILE_SIZE, tc.TILE_SIZE)
        pygame.draw.rect(screen, self.color, shape)

        if self.occupied_by is not None and isinstance(self.occupied_by, Merp):
            self.occupied_by.draw(screen)
