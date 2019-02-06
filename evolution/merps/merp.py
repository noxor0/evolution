import pygame
import random

from commands.move_command import MoveCommand
from commands.command_with_params import CommandWithParams
from constants import game as gc
from constants import merp as mc
from constants import command as cc

random.seed(gc.RAND_SEED)


class Merp:
    merp_count = 0

    def __init__(self, tile):
        self.color = random.choice([mc.FEMALE_COLOR, mc.MALE_COLOR])
        self.tile = tile
        self.id = Merp.merp_count
        # TODO: If no parent, random list of commands, else take from 50/50 from parents
        self.genetic_commands = [CommandWithParams(MoveCommand, cc.DirectionMap.UP)]
        self.commands_todo = self.genetic_commands
        Merp.merp_count += 1

    def draw(self, screen):
        pygame.draw.circle(screen,
                           self.color,
                           (self.tile.x + mc.HALF_TILE_SIZE, self.tile.y + mc.HALF_TILE_SIZE),
                           mc.SPRITE_RADIUS)

    def get_next_command(self):
        if self.commands_todo:
            return self.commands_todo.pop()
