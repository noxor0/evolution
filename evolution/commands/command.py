from constants import command as cc


class Command:
    def __init__(self, **kwargs):
        self.merp = kwargs.get(cc.MERP)
        self.game_map = kwargs.get(cc.GAME_MAP)

    def execute(self):
        assert not hasattr(object, 'execute')
