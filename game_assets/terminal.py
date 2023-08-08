import pygame as pg
from game_config import GRID_X, GRID_Y, GRID_SIZE, DEBUG_FONT

LINE_SIZE = 20
TEXT_SIZE = 15


class Terminal:
    def __init__(self, game_screen):
        self.game_screen = game_screen

        self.is_on = False

        self.term_bg = pg.Surface((GRID_X * GRID_SIZE, GRID_Y * GRID_SIZE))
        self.term_bg.set_alpha(50)
        self.term_bg.fill("black")

        self.current_command = ""

    def new_entry(self):
        pass

    def command_text(self):
        return pg.font.Font(DEBUG_FONT, TEXT_SIZE).render("> " + self.current_command, False, "white")

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def display(self):
        self.game_screen.blit(self.term_bg, (0, 0))
        self.game_screen.blit(self.command_text(), (0, 0))
