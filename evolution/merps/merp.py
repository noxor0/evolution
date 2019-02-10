import pygame
import random

from constants import game as gc
from constants import merp as mc
from merps import create_life_choices

random.seed(gc.RAND_SEED)


class Merp:
    merp_count = 0

    def __init__(self, tile, parent=None):
        self.color = random.choice([mc.FEMALE_COLOR, mc.MALE_COLOR])
        self.tile = tile
        self.id = Merp.merp_count
        self.parent = parent
        self.genetic_commands = create_life_choices()
        self.commands_todo = self.genetic_commands
        Merp.merp_count += 1

    def draw(self, screen):
        pygame.draw.circle(screen,
                           self.color,
                           (self.tile.coordinates.x + mc.HALF_TILE_SIZE, self.tile.coordinates.y + mc.HALF_TILE_SIZE),
                           mc.SPRITE_RADIUS)

    def get_next_choice(self):
        if self.commands_todo:
            return self.commands_todo.pop()
