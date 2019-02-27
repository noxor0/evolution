from constants import command as cc


class Commander:
    def __init__(self, game_map):
        self.game_map = game_map
        self.command_kwargs = {
            cc.GAME_MAP: self.game_map
        }

    def execute_merp_commands(self):
        for merp in self.game_map.merp_list:
            next_command, additional_command_kwargs = merp.get_next_choice()
            if next_command:
                self.command_kwargs.update({**additional_command_kwargs, **{cc.MERP: merp}})
                next_command(**self.command_kwargs).execute()
