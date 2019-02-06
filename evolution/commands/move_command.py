class MoveCommand:

    def __init__(self, merp, tile_map, direction=None):
        self.merp = merp
        self.tile_map = tile_map
        self.direction = direction

