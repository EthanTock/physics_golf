import pygame as pg
from game_config import WINDOW_X, WINDOW_Y, DEBUG_FONT
from game_assets.level_command_executor import LevelCommandExecutor

LINE_SIZE = 20
TEXT_SIZE = 15


class Terminal:
    def __init__(self, game_screen, level_command_executor):
        self.game_screen = game_screen
        self.level_command_executor = level_command_executor

        self.is_on = False

        self.term_bg = pg.Surface((WINDOW_X, WINDOW_Y))
        self.term_bg.set_alpha(50)
        self.term_bg.fill("black")

        self.current_command = ""
        self.past_commands = []
        self.lines_printed = 0

    def new_entry(self):
        self.past_commands.insert(0, self.current_command)
        self.current_command = ""

    def command_text(self):
        return pg.font.Font(DEBUG_FONT, TEXT_SIZE).render("> " + self.current_command, False, "white")

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def clear(self):
        self.current_command = ""
        self.past_commands = []
        self.lines_printed = 0

    def display(self):
        self.game_screen.blit(self.term_bg, (0, 0))
        self.game_screen.blit(self.command_text(), (0, WINDOW_Y - LINE_SIZE))

    def run(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.level_command_executor.parse_command(self.current_command)
                    self.new_entry()
                elif event.key == pg.K_BACKSPACE and len(self.current_command) > 0:
                    self.current_command = self.current_command[:-1]
                else:
                    self.current_command += event.unicode
        self.display()
