import pygame
import random

from constants import game as gc
from constants import merp as mc
from merps import create_a_choice

random.seed(gc.RAND_SEED)


class Merp:
    merp_count = 0

    def __init__(self, tile, parents=(None, None)):
        self.color = random.choice([mc.FEMALE_COLOR, mc.MALE_COLOR])
        self.tile = tile
        self.id = Merp.merp_count
        self.parents = parents
        self.genetic_commands = [create_a_choice()]
        Merp.merp_count += 1

    def draw(self, screen):
        pygame.draw.circle(screen,
                           self.color,
                           (self.tile.coordinates.x + mc.HALF_TILE_SIZE, self.tile.coordinates.y + mc.HALF_TILE_SIZE),
                           mc.SPRITE_RADIUS)

    def get_next_choice(self):
        self.genetic_commands.append(create_a_choice(self.parents))
        return self.genetic_commands[-1]

    def move(self, new_tile):
        self.tile.occupied_by = None
        self.tile = new_tile
        self.tile.occupied_by = self

