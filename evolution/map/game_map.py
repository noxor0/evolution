import pygame

from constants.tile import *
from constants import game as gc
from map.perlin.perlin_generation import generate_tile_array
from map.tile import Tile


def draw_tile(screen, x, y, tile_type=TileTypes.DIRT):
    tile = Tile(tile_type)
    pygame.draw.rect(screen, tile.color, pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))


class GameMap:
    def __init__(self, screen):
        self.screen = screen
        self.tile_map = generate_tile_array()

    def setup_map(self):
        for x in range(0, gc.WINDOW_SIZE, TILE_SIZE):
            for y in range(0, gc.WINDOW_SIZE, TILE_SIZE):
                x_tile = int(x / TILE_SIZE)
                y_tile = int(y / TILE_SIZE)
                tile_type = self.tile_map[x_tile][y_tile].tile_type
                draw_tile(self.screen, x, y, tile_type=tile_type)
        return self


