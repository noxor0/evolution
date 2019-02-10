from commands.command import Command
from constants import command as cc


class MoveCommand(Command):
    def __init__(self, direction=cc.DirectionMap.UP, **kwargs):
        self.direction = direction
        super().__init__(**kwargs)

    def execute(self):
        # TODO check for valid move
        curr_tile = self.merp.tile
        new_tile_coordinates = curr_tile.tile_map_coordinates + self.direction
        self.merp.tile.occupied_by = None
        self.merp.tile = self.game_map.tile_map[new_tile_coordinates.x][new_tile_coordinates.y]
        self.game_map.tile_map[new_tile_coordinates.x][new_tile_coordinates.y].occupied_by = self.merp

        # print(self, "executed move with old: {}, new: {}"
        #       .format(curr_tile.coordinates.to_tuple(), new_tile_coordinates.to_tuple()))
        super().execute()
