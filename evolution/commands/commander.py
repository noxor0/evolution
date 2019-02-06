from constants import command as cc


class Commander:
    def __init__(self, game_map):
        self.game_map = game_map

    def execute_merp_commands(self):
        for merp in self.game_map.merp_list:
            print(merp.id)
            next_command_with_params = merp.get_next_command()
            if next_command_with_params:
                command_class = next_command_with_params.command_class
                params = next_command_with_params.params
                kwargs = {cc.MERP: merp, cc.GAME_MAP: self.game_map, cc.PARAMS: params}
                command = command_class(**kwargs)
                command.execute()
