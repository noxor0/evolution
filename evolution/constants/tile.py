from enum import Enum

from pygame import Color


class TileTypes(Enum):
    DIRT = 1
    GRASS = 2
    WATER = 3
    MOUNTAIN = 4
    SNOW = 5
    DEEP_WATER = 6


TILE_SIZE = 8
TILE_OUTLINE = 1
FILL_COLOR = 'fill_color'
OUTLINE_COLOR = 'outline_color'
ACCESSIBLE = 'accessible'

TILE_PROPERTIES = {
    TileTypes.DIRT: {
        FILL_COLOR: Color('#db9356'),
        ACCESSIBLE: True,
    },
    TileTypes.GRASS: {
        FILL_COLOR: Color('#30a630'),
        ACCESSIBLE: True,
    },
    TileTypes.WATER: {
        FILL_COLOR: Color('#1da2d8'),
        ACCESSIBLE: True,
    },
    TileTypes.DEEP_WATER: {
        FILL_COLOR: Color('#1e5481'),
        ACCESSIBLE: False,
    },
    TileTypes.MOUNTAIN: {
        FILL_COLOR: Color('#9a9a9a'),
        ACCESSIBLE: False,
    },
    TileTypes.SNOW: {
        FILL_COLOR: Color('#fffafa'),
        ACCESSIBLE: False,
    },
}
