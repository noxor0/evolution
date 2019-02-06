import random

from constants import tile as tc
from constants import game as gc
from map.perlin.perlin_generation import generate_tile_array as perlin_generate_map
from merps.merp import Merp

random.seed(gc.RAND_SEED)


def _translate_to_tile_map_coordinates(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return int(x / tc.TILE_SIZE), int(y / tc.TILE_SIZE)


class GameMap:
    def __init__(self, screen):
        self.screen = screen
        self.tile_map = None
        self.merp_list = None

    def setup(self):
        self.tile_map = perlin_generate_map()
        self.merp_list = self._populate_merp()

    def draw(self):
        for x in range(0, gc.WINDOW_SIZE, tc.TILE_SIZE):
            for y in range(0, gc.WINDOW_SIZE, tc.TILE_SIZE):
                x_tile, y_tile = _translate_to_tile_map_coordinates(x, y)
                self.tile_map[x_tile][y_tile].draw(self.screen)
        return self

    def update(self):
        # TODO: Uses a queue that contains all the changes that happen to the map
        pass

    def _populate_merp(self):
        merp_list = []
        map_size = len(self.tile_map) - 1
        for merp_numb in range(gc.START_MERP_COUNT):
            random_x = random.randint(0, map_size)
            random_y = random.randint(0, map_size)
            random_tile = self.tile_map[random_x][random_y]
            if not random_tile.accessible:
                valid_x, valid_y = self._get_closest_valid_spot_coordinates(random_tile)
                random_tile = self.tile_map[valid_x][valid_y]
            new_merp = Merp(random_tile)
            merp_list.append(new_merp)
            random_tile.occupied_by = new_merp
        return merp_list

    def _get_closest_valid_spot_coordinates(self, tile):
        inaccessible_tile = tile
        range_from_start = 1
        map_limit = len(self.tile_map)

        def _get_right_tile_coordinates():
            if tile.tile_map_x + range_from_start >= map_limit:
                return
            if self.tile_map[tile.tile_map_x + range_from_start][tile.tile_map_y].accessible:
                return tile.tile_map_x + range_from_start, tile.tile_map_y

        def _get_top_tile_coordinates():
            if tile.tile_map_y + range_from_start >= map_limit:
                return
            elif self.tile_map[tile.tile_map_x][tile.tile_map_y + range_from_start].accessible:
                return tile.tile_map_x, tile.tile_map_y + range_from_start

        def _get_left_tile_coordinates():
            if tile.tile_map_x - range_from_start < 0:
                return
            if self.tile_map[tile.tile_map_x - range_from_start][tile.tile_map_y].accessible:
                return tile.tile_map_x - range_from_start, tile.tile_map_y

        def _get_bottom_tile_coordinates():
            if tile.tile_map_y - range_from_start < 0:
                return
            if self.tile_map[tile.tile_map_x][tile.tile_map_y - range_from_start].accessible:
                return tile.tile_map_x, tile.tile_map_y - range_from_start

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
                # NANI?
                return 0, 0
