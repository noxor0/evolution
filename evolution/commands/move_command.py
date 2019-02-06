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
        # curr_tile
        print(self, "executed move with", self.direction)

