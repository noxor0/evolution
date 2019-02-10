import random

from constants import game as gc
from constants import merp as mc
from commands.command import Command
from commands.move_command import MoveCommand

COMMAND_LIST = Command.__subclasses__()

random.seed(gc.RAND_SEED)


# GODS PLAN
def create_life_choices(parents=None):
    command_generation_function = {
        MoveCommand: _create_move_command,
    }
    merp_choices = []
    for _ in range(mc.LIFE_SPAN):
        next_choice = random.choice(COMMAND_LIST)
        merp_choices.append(command_generation_function.get(next_choice)(parents))


def _create_move_command(parents):
    if parents:
        # TODO: Parent 50/50 here
        pass
    else:
        return MoveCommand()
