import pygame as pg
from game_config import GRID_SIZE


class GridShowcase:
    def __init__(self, screen, screen_dimensions, colors):
        self.screen = screen
        self.screen_dimensions = self.screen_dimensions_x, self.screen_dimensions_y = screen_dimensions
        self.colors = self.color_1, self.color_2, self.color_3 = colors

    def __give_color(self, line_num):
        if line_num % (10 * GRID_SIZE) == 0:
            return self.color_1
        elif line_num % (2 * GRID_SIZE) == 0:
            return self.color_2
        else:
            return self.color_3

    def __give_thickness(self, line_num):
        if line_num % (10 * GRID_SIZE) == 0:
            return 3
        elif line_num % (2 * GRID_SIZE) == 0:
            return 1
        else:
            return 1

    def draw_lines(self):
        for h_pos in range(0, self.screen_dimensions_x, GRID_SIZE):
            pg.draw.line(self.screen, self.__give_color(h_pos), (h_pos, 0), (h_pos, self.screen_dimensions_y), self.__give_thickness(h_pos))
        for v_pos in range(0, self.screen_dimensions_y, GRID_SIZE):
            pg.draw.line(self.screen, self.__give_color(v_pos), (0, v_pos), (self.screen_dimensions_x, v_pos), self.__give_thickness(v_pos))
