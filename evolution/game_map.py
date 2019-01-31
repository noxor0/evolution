import pygame

from constants.tile import *
from constants import game as gc


def create_tile(screen, x, y, tile_type=Tiles.DIRT):
    tile = TILE_INFO.get(tile_type)
    pygame.draw.rect(screen, tile.get(FILL_COLOR),
                     pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
    pygame.draw.rect(screen, tile.get(OUTLINE_COLOR),
                     pygame.Rect(x, y, TILE_SIZE, TILE_SIZE), TILE_OUTLINE)


class GameMap:
    def __init__(self, screen):
        self.screen = screen

    def setup_map(self):
        for x in range(0, gc.WINDOW_SIZE, TILE_SIZE):
            for y in range(0, gc.WINDOW_SIZE, TILE_SIZE):
                create_tile(self.screen, x, y, tile_type=Tiles.DIRT)
        return self
