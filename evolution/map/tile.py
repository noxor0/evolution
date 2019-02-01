from constants import tile as tc


class Tile:
    def __init__(self, tile_type):
        self.tile_type = tile_type
        self.tile_properties = tc.TILE_PROPERTIES.get(tile_type)
        self.accessible = self.tile_properties.get(tc.ACCESSIBLE)
        self.color = self.tile_properties.get(tc.FILL_COLOR)
        self.occupied = False
