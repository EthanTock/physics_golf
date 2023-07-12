import pygame as pg

DEFAULT_COLOR = "white"


class GridShowcase:
    def __init__(self, screen, screen_dimensions, tile_size, color=DEFAULT_COLOR):
        self.screen = screen
        self.screen_dimensions = self.screen_dimensions_x, self.screen_dimensions_y = screen_dimensions
        self.tile_size = tile_size
        self.color = color

    def draw_lines(self):
        for h_pos in range(0, self.screen_dimensions_x, self.tile_size):
            pg.draw.line(self.screen, self.color, (h_pos, 0), (h_pos, self.screen_dimensions_y))
        for v_pos in range(0, self.screen_dimensions_y, self.tile_size):
            pg.draw.line(self.screen, self.color, (0, v_pos), (self.screen_dimensions_x, v_pos))
