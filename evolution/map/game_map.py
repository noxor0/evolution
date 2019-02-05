import random

from constants import tile as tc
from constants import game as gc
from map.perlin.perlin_generation import generate_tile_array
from merps.merp import Merp

random.seed(gc.RAND_SEED)


class GameMap:
    def __init__(self, screen):
        self.screen = screen
        self.tile_map = generate_tile_array()

    def setup_map(self):
        self._populate_merp()
        for x in range(0, gc.WINDOW_SIZE, tc.TILE_SIZE):
            for y in range(0, gc.WINDOW_SIZE, tc.TILE_SIZE):
                x_tile = int(x / tc.TILE_SIZE)
                y_tile = int(y / tc.TILE_SIZE)
                tile = self.tile_map[x_tile][y_tile]
                self._render_tile(tile)
        return self

    def _render_tile(self, tile):
        tile.draw(self.screen)

        merp = tile.occupied_by
        if merp is not None:
            merp.draw(self.screen)

    def _populate_merp(self):
        map_size = len(self.tile_map) - 1
        for merp_numb in range(gc.START_MERP_COUNT):
            random_x = random.randint(0, map_size)
            random_y = random.randint(0, map_size)
            random_tile = self.tile_map[random_x][random_y]
            if not random_tile.accessible:
                valid_x, valid_y = self._get_closest_valid_spot_coordinates(random_tile)
                random_tile = self.tile_map[valid_x][valid_y]
            random_tile.occupied_by = Merp(random_tile)

    def _get_closest_valid_spot_coordinates(self, tile):
        inaccessible_tile = tile
        range_from_start = 1
        tile_x = int(tile.x / tc.TILE_SIZE)
        tile_y = int(tile.y / tc.TILE_SIZE)
        map_limit = len(self.tile_map)

        def _get_right_tile_coordinates():
            if tile_x + range_from_start >= map_limit:
                return
            if self.tile_map[tile_x + range_from_start][tile_y].accessible:
                return tile_x + range_from_start, tile_y

        def _get_top_tile_coordinates():
            if tile_y + range_from_start >= map_limit:
                return
            elif self.tile_map[tile_x][tile_y + range_from_start].accessible:
                return tile_x, tile_y + range_from_start

        def _get_left_tile_coordinates():
            if tile_x - range_from_start < 0:
                return
            if self.tile_map[tile_x - range_from_start][tile_y].accessible:
                return tile_x - range_from_start, tile_y

        def _get_bottom_tile_coordinates():
            if tile_y - range_from_start < 0:
                return
            if self.tile_map[tile_x][tile_y - range_from_start].accessible:
                return tile_x, tile_y - range_from_start

        while not inaccessible_tile.accessible:
            adjacent_tile_checks = [_get_bottom_tile_coordinates, _get_top_tile_coordinates,
                                    _get_left_tile_coordinates, _get_right_tile_coordinates]
            random.shuffle(adjacent_tile_checks)

            while len(adjacent_tile_checks) > 0:
                check_func = adjacent_tile_checks.pop(0)
                potential_coordinates = check_func()
                if check_func() is not None:
                    return potential_coordinates

            range_from_start += 1

            if range_from_start >= map_limit:
                return "Fuck"




