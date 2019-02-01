from constants.game import WINDOW_SIZE
from constants.tile import TILE_SIZE

SHAPE_DIMENSIONS = tuple(int(WINDOW_SIZE/TILE_SIZE) for x in range(2))

PERLIN_SCALE = 50.0
PERLIN_OCTAVES = 6
PERLIN_PERSISTENCE = 0.3
PERLIN_LACUNARITY = 2.8
