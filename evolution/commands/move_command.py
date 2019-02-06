from constants import command as cc


class MoveCommand:
    def __init__(self, **kwargs):
        self.merp = kwargs.get(cc.MERP)
        self.game_map = kwargs.get(cc.GAME_MAP)
        self.params = kwargs.get(cc.PARAMS)
        if self.params:
            self.direction = self.params[0]
        else:
            self.direction = cc.DirectionMap.UP

    def execute(self):
        curr_tile = self.merp.tile
        new_tile_coordinates = curr_tile.tile_map_coordinates + self.direction
        self.merp.tile.occupied_by = None
        self.merp.tile = self.game_map.tile_map[new_tile_coordinates.x][new_tile_coordinates.y]
        self.game_map.tile_map[new_tile_coordinates.x][new_tile_coordinates.y].occupied_by = self.merp

        print(self, "executed move with old: {}, new:{}"
              .format(curr_tile.coordinates.to_tuple(), new_tile_coordinates.to_tuple()))
