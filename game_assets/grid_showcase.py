import pygame as pg
from game_config import GRID_SIZE


class GridShowcase:
    def __init__(self, screen, screen_dimensions, colors, thicknesses, grid_iterations):
        self.screen = screen
        self.screen_dimensions = self.screen_dimensions_x, self.screen_dimensions_y = screen_dimensions
        self.colors = colors
        self.thicknesses = thicknesses
        self.grid_iterations = grid_iterations

    def draw_lines(self):
        for grid_iteration in range(0, len(self.grid_iterations)):
            for h_pos in range(0, self.screen_dimensions_x, GRID_SIZE * self.grid_iterations[grid_iteration]):
                pg.draw.line(self.screen, self.colors[grid_iteration], (h_pos, 0), (h_pos, self.screen_dimensions_y), self.thicknesses[grid_iteration])
            for v_pos in range(0, self.screen_dimensions_y, GRID_SIZE * self.grid_iterations[grid_iteration]):
                pg.draw.line(self.screen, self.colors[grid_iteration], (0, v_pos), (self.screen_dimensions_x, v_pos), self.thicknesses[grid_iteration])
