import random

from constants import game as gc
from commands.command import Command
from commands.move_command import MoveCommand
from constants import command as cc

COMMAND_LIST = Command.__subclasses__()

random.seed(gc.RAND_SEED)


# GODS PLAN
def create_a_choice(parents=None):
    command_generation_function = {
        MoveCommand: _create_move_command,
    }
    next_choice = random.choice(COMMAND_LIST)
    command, command_kwargs = command_generation_function.get(next_choice)(parents)
    return command, command_kwargs


def _create_move_command(parents):
    if parents:
        # TODO: Parent 50/50 here
        pass
    else:
        return MoveCommand, {cc.DIRECTION: random.choice(list(cc.DIRECTION_MAP.values()))}
