from commands.command import Command
from constants import command as cc
from constants import map as mc


class MoveCommand(Command):
    def __init__(self, direction=cc.DIRECTION_MAP.get(cc.UP), **kwargs):
        self.direction = direction
        super().__init__(**kwargs)

    def _is_new_tile_inbounds(self, new_tile_coordinates):
        x = new_tile_coordinates.x
        y = new_tile_coordinates.y

        return (0 <= x < mc.SHAPE_DIMENSIONS[0] and 0 <= y < mc.SHAPE_DIMENSIONS[1]
                and self.game_map.tile_map[x][y].accessible)

    def execute(self):
        curr_tile = self.merp.tile
        new_tile_coordinates = curr_tile.tile_map_coordinates + self.direction

        if self._is_new_tile_inbounds(new_tile_coordinates):
            new_tile = self.game_map.tile_map[new_tile_coordinates.x][new_tile_coordinates.y]
            self.merp.move(new_tile)

        super().execute()
