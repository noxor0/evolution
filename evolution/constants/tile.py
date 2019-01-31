from enum import Enum

from pygame import Color


class Tiles(Enum):
    DIRT = 1
    # WATER = '2'


TILE_SIZE = 5
TILE_OUTLINE = 1
FILL_COLOR = 'fill_color'
OUTLINE_COLOR = 'outline_color'

TILE_INFO = {
    Tiles.DIRT: {
        FILL_COLOR: Color('sandybrown'),
        OUTLINE_COLOR: Color('black')
    }
}
