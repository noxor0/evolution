import random

from constants.tile import *
from constants import game as gc
from map.perlin.perlin_generation import generate_tile_array
from merps.merp import Merp

random.seed(gc.RAND_SEED)


class GameMap:
    def __init__(self, screen):
        self.screen = screen
        self.tile_map = generate_tile_array()

    def setup_map(self):
        self.populate_merp()
        for x in range(0, gc.WINDOW_SIZE, TILE_SIZE):
            for y in range(0, gc.WINDOW_SIZE, TILE_SIZE):
                x_tile = int(x / TILE_SIZE)
                y_tile = int(y / TILE_SIZE)
                tile = self.tile_map[x_tile][y_tile]
                self.render_tile(x, y, tile)
        return self

    def render_tile(self, x, y, tile):
        tile.draw(self.screen)
        # tile = Tile(tile_type, x, y)
        # tile.draw(self.screen)
        # if x == 200 and y == 200:
        #     tile.occupied_by = Merp()

        merp = tile.occupied_by
        if merp is not None:
            merp.draw(self.screen)

    def populate_merp(self):
        map_size = len(self.tile_map) - 1
        for merp_numb in range(gc.START_MERP_COUNT):
            random_x = random.randint(0, map_size)
            random_y = random.randint(0, map_size)
            random_tile = self.tile_map[random_x][random_y]
            random_tile.occupied_by = Merp(random_tile)


