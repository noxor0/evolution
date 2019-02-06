from map.coordinates import Coordinates


class DirectionMap:
    UP = Coordinates(0, 1)
    DOWN = Coordinates(0, -1)
    RIGHT = Coordinates(1, 0)
    LEFT = Coordinates(-1, 0)


MERP = 'merp'
GAME_MAP = 'game_map'
PARAMS = 'param'
DIRECTION = 'direction'
