import pygame as pg
from game_config import WINDOW_X, WINDOW_Y, DEBUG_FONT

LINE_SIZE = 20
TEXT_SIZE = 15
MAX_TERMINAL_HEIGHT = WINDOW_Y / 2 - 50


class Terminal:
    def __init__(self, game_screen, level_command_executor):
        self.game_screen = game_screen
        self.level_command_executor = level_command_executor

        self.is_on = False
        self.just_turned_on = False

        self.term_bg = pg.Surface((WINDOW_X, MAX_TERMINAL_HEIGHT + 1))
        self.term_bg.set_alpha(128)
        self.term_bg.fill("black")

        self.current_command = ""
        self.past_commands = []
        self.lines_printed = 0

    def execute_command(self):
        self.current_command = self.current_command.strip()
        self.past_commands.insert(0, self.current_command)
        if self.current_command == "exit":
            self.turn_off()
        elif self.current_command == "clear":
            self.clear()
        else:
            self.level_command_executor.parse_command(self.current_command)
        self.current_command = ""

    def command_text(self, text):
        return pg.font.Font(DEBUG_FONT, TEXT_SIZE).render("> " + text, False, "white")

    def turn_on(self):
        self.is_on = True
        self.just_turned_on = True

    def turn_off(self):
        self.is_on = False

    def clear(self):
        self.current_command = ""
        self.past_commands = []

    def display(self):
        self.game_screen.blit(self.term_bg, (0, WINDOW_Y - MAX_TERMINAL_HEIGHT))
        for past_command_index in range(0, len(self.past_commands)):
            if past_command_index < MAX_TERMINAL_HEIGHT // LINE_SIZE - 1:
                self.game_screen.blit(self.command_text(self.past_commands[past_command_index]), (0, WINDOW_Y - LINE_SIZE * (past_command_index + 2)))
        self.game_screen.blit(self.command_text(self.current_command), (0, WINDOW_Y - LINE_SIZE))

    def run(self, events):
        for event in events:
            if event.type == pg.KEYDOWN and not self.just_turned_on:
                if event.key == pg.K_RETURN:
                    self.execute_command()
                elif event.key == pg.K_BACKSPACE and len(self.current_command) > 0:
                    self.current_command = self.current_command[:-1]
                else:
                    self.current_command += event.unicode
            elif self.just_turned_on:
                self.just_turned_on = False
        self.display()
