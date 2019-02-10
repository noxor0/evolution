from map.coordinates import Coordinates


class DirectionMap:
    DOWN = Coordinates(0, 1)
    UP = Coordinates(0, -1)
    RIGHT = Coordinates(1, 0)
    LEFT = Coordinates(-1, 0)


MERP = 'merp'
GAME_MAP = 'game_map'
PARAMS = 'param'
DIRECTION = 'direction'
