from level import Level
import datetime as dt
import json


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
            elif command_name == "grid":
                if arg == "off":
                    self.commands.append("nogrid")
                elif arg == "on":
                    self.commands.append("grid")
            elif command_name == "save":
                self.level.name = arg
                self.level.save_to_levels_json()
        elif command == "new":
            self.change_level_to("l" + str(dt.datetime.isoformat(dt.datetime.now())))
        elif command == "edit":
            self.commands.append("edit")
        elif command == "play":
            self.commands.append("play")
        elif command == "save":
            self.level.save_to_levels_json()

    def change_level_to(self, level_name):
        try:
            with open(f"levels_json/{level_name}.json", "r") as json_file:
                self.level = Level(**json.load(json_file))
        except FileNotFoundError:
            self.level = Level(level_name)
        self.commands.append("change")
