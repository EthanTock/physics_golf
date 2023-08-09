from level import Level
from levels import LEVELS
import datetime as dt


class LevelCommandExecutor:
    def __init__(self, level):
        self.level = level
        self.commands = []

    def parse_command(self, command):
        if len(command.split()) == 2:
            command_name, arg = command.split()

            if command_name == "color":
                self.level.update_colorset(arg)
            elif command_name == "load":
                self.change_level_to(arg)
            elif command_name == "edit":
                if arg == "off":
                    self.commands.append("play")
                elif arg == "on":
                    self.commands.append("edit")
            elif command_name == "zoomies":
                if arg == "off":
                    self.commands.append("nozoomies")
                elif arg == "on":
                    self.commands.append("zoomies")
        elif command == "new":
            self.change_level_to(str(dt.datetime.isoformat(dt.datetime.now())))
        elif command == "edit":
            self.commands.append("edit")
        elif command == "play":
            self.commands.append("play")

    def change_level_to(self, level_name):
        if level_name in LEVELS.keys():
            self.level = LEVELS[level_name]
        else:
            self.level = Level(
                level_name
            )
        self.commands.append("change")
