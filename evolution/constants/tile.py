from enum import Enum

from pygame import Color


class Tiles(Enum):
    DIRT = 1
    GRASS = 2
    WATER = 3
    MOUNTAIN = 4
    SNOW = 5


TILE_SIZE = 5
TILE_OUTLINE = 1
FILL_COLOR = 'fill_color'
OUTLINE_COLOR = 'outline_color'

# TODO: Add interactable / moveable tags
TILE_INFO = {
    Tiles.DIRT: {
        FILL_COLOR: Color('sandybrown'),
        # OUTLINE_COLOR: Color('black'),
    },
    Tiles.GRASS: {
        FILL_COLOR: Color('green'),
    },
    Tiles.WATER: {
        FILL_COLOR: Color('blue'),
    },
    Tiles.MOUNTAIN: {
        FILL_COLOR: Color('grey'),
    },
    Tiles.SNOW: {
        FILL_COLOR: Color('white'),
    },
}
