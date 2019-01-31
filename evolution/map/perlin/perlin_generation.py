import noise
import numpy as np
# TODO: Remove me
from scipy.misc import toimage

import constants.map as map_const


# TODO: Remove me
def add_color(world):
    blue = [65, 105, 225]
    green = [34, 139, 34]
    beach = [238, 214, 175]
    snow = [255, 250, 250]
    mountain = [139, 137, 137]
    color_world = np.zeros(map_const.SHAPE_DIMENSIONS + (3,))
    for i in range(map_const.SHAPE_DIMENSIONS[0]):
        for j in range(map_const.SHAPE_DIMENSIONS[1]):
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


def generate_world():
    world_array = np.zeros(map_const.SHAPE_DIMENSIONS)
    for x in range(map_const.SHAPE_DIMENSIONS[0]):
        for y in range(map_const.SHAPE_DIMENSIONS[1]):
            world_array[x][y] = noise.pnoise2(x / map_const.PERLIN_SCALE,
                                              y / map_const.PERLIN_SCALE,
                                              octaves=map_const.PERLIN_OCTAVES,
                                              persistence=map_const.PERLIN_PERSISTENCE,
                                              lacunarity=map_const.PERLIN_LACUNARITY,
                                              repeatx=1024,
                                              repeaty=1024,
                                              base=0)
    return world_array


if __name__ == '__main__':
    toimage(add_color(generate_world())).show()
