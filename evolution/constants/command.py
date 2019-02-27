from map.coordinates import Coordinates

DOWN = 'DOWN'
UP = 'UP'
RIGHT = 'RIGHT'
LEFT = 'LEFT'
MERP = 'merp'
GAME_MAP = 'game_map'
PARAMS = 'param'
DIRECTION = 'direction'

DIRECTION_MAP = {
    DOWN: Coordinates(0, 1),
    UP: Coordinates(0, -1),
    RIGHT: Coordinates(1, 0),
    LEFT: Coordinates(-1, 0),
}

