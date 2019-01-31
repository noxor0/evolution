import pygame

from constants.tile import *
from constants import game as gc
from map.perlin.perlin_generation import generate_tile_array


def create_tile(screen, x, y, tile_type=Tiles.DIRT):
    tile = TILE_INFO.get(tile_type)
    pygame.draw.rect(screen, tile.get(FILL_COLOR),
                     pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
    if OUTLINE_COLOR in tile:
        pygame.draw.rect(screen, tile.get(OUTLINE_COLOR),
                         pygame.Rect(x, y, TILE_SIZE, TILE_SIZE), TILE_OUTLINE)


class GameMap:
    def __init__(self, screen):
        self.screen = screen

    def setup_map(self):
        tile_array = generate_tile_array()
        for x in range(0, gc.WINDOW_SIZE, TILE_SIZE):
            for y in range(0, gc.WINDOW_SIZE, TILE_SIZE):
                x_tile = int(x / TILE_SIZE)
                y_tile = int(y / TILE_SIZE)
                tile_type = tile_array[x_tile][y_tile]
                # TODO: Create an actionable map that sprites can interact with
                # Build map visual map off of that instead
                create_tile(self.screen, x, y, tile_type=tile_type)
        return self


