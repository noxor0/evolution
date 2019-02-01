import noise
import numpy as np
# TODO: Remove me
from scipy.misc import toimage

import constants.map as mc
from constants.tile import TileTypes
from map.tile import Tile


# TODO: Remove me
def add_color(world):
    blue = [65, 105, 225]
    green = [34, 139, 34]
    beach = [238, 214, 175]
    snow = [255, 250, 250]
    mountain = [139, 137, 137]
    color_world = np.zeros(mc.SHAPE_DIMENSIONS + (3,))
    for i in range(mc.SHAPE_DIMENSIONS[0]):
        for j in range(mc.SHAPE_DIMENSIONS[1]):
            if world[i][j] < -0.30:
                color_world[i][j] = blue
            elif world[i][j] < -.15:
                color_world[i][j] = beach
            elif world[i][j] < .2:
                color_world[i][j] = green
            elif world[i][j] < 0.3:
                color_world[i][j] = mountain
            elif world[i][j] < 1.0:
                color_world[i][j] = snow

    return color_world


def generate_perlin_world_array():
    world_array = np.zeros(mc.SHAPE_DIMENSIONS)
    for x in range(mc.SHAPE_DIMENSIONS[0]):
        for y in range(mc.SHAPE_DIMENSIONS[1]):
            world_array[x][y] = noise.pnoise2(x / mc.PERLIN_SCALE,
                                              y / mc.PERLIN_SCALE,
                                              octaves=mc.PERLIN_OCTAVES,
                                              persistence=mc.PERLIN_PERSISTENCE,
                                              lacunarity=mc.PERLIN_LACUNARITY,
                                              repeatx=1024,
                                              repeaty=1024,
                                              base=0)
    return world_array


def generate_tile_array():
    tile_map = np.zeros(mc.SHAPE_DIMENSIONS, dtype=TileTypes)
    perlin_array = generate_perlin_world_array()
    # TODO: Add overlapping range with a random choice to smooth out transitions
    for i in range(perlin_array[0].size):
        for j in range(perlin_array[1].size):
            if perlin_array[i][j] < -.35:
                tile_map[i][j] = Tile(TileTypes.DEEP_WATER)
            elif perlin_array[i][j] < -0.20:
                tile_map[i][j] = Tile(TileTypes.WATER)
            elif perlin_array[i][j] < -.15:
                tile_map[i][j] = Tile(TileTypes.DIRT)
            elif perlin_array[i][j] < .25:
                tile_map[i][j] = Tile(TileTypes.GRASS)
            elif perlin_array[i][j] < 0.45:
                tile_map[i][j] = Tile(TileTypes.MOUNTAIN)
            elif perlin_array[i][j] < 1.0:
                tile_map[i][j] = Tile(TileTypes.SNOW)
    return tile_map


if __name__ == '__main__':
    toimage(add_color(generate_perlin_world_array())).show()
