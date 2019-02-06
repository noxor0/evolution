class CommandWithParams:
    def __init__(self, command_cls, *args):
        self.command_class = command_cls
        self.params = args
