class LevelCommandExecutor:
    def __init__(self, level):
        self.level = level

    def parse_command(self, command):
        if len(command.split()) == 2:
            command_name, arg = command.split()

            if command_name == "color":
                self.level.update_colorset(arg)
