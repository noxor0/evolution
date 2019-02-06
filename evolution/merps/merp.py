import pygame
import random

from constants import game as gc
from constants import merp as mc
from constants import tile as tc

random.seed(gc.RAND_SEED)


class Merp:
    merp_count = 0

    def __init__(self, tile):
        self.color = random.choice([mc.FEMALE_COLOR, mc.MALE_COLOR])
        self.tile = tile
        self.id = Merp.merp_count
        Merp.merp_count += 1

    def draw(self, screen):
        half_tile_size = int(tc.TILE_SIZE / 2)
        pygame.draw.circle(screen,
                           self.color,
                           (self.tile.x + half_tile_size, self.tile.y + half_tile_size),
                           mc.SPRITE_RADIUS)
