from constants import command as cc


class MoveCommand:
    def __init__(self, **kwargs):
        self.merp = kwargs.get(cc.MERP)
        self.game_map = kwargs.get(cc.GAME_MAP)
        self.direction = kwargs.get(cc.PARAMS)

    def execute(self):
        print(self, "executed")

