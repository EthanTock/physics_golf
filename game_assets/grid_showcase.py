import pygame as pg
from game_config import GRID_SIZE, WINDOW_X, WINDOW_Y


class GridShowcase:
    def __init__(self, game_screen, opacity, colors, thicknesses, grid_iterations):
        self.game_screen = game_screen

        self.opacity = opacity
        self.blend_screen = pg.Surface((WINDOW_X, WINDOW_Y))
        self.blend_screen.set_alpha(self.opacity)
        self.blend_screen.set_colorkey("black")

        self.colors = colors
        self.thicknesses = thicknesses
        self.grid_iterations = grid_iterations

    def draw_lines(self):
        for grid_iteration in range(0, len(self.grid_iterations)):
            for h_pos in range(0, WINDOW_X, GRID_SIZE * self.grid_iterations[grid_iteration]):
                pg.draw.line(self.blend_screen, self.colors[grid_iteration], (h_pos, 0), (h_pos, WINDOW_Y), self.thicknesses[grid_iteration])
            for v_pos in range(0, WINDOW_Y, GRID_SIZE * self.grid_iterations[grid_iteration]):
                pg.draw.line(self.blend_screen, self.colors[grid_iteration], (0, v_pos), (WINDOW_X, v_pos), self.thicknesses[grid_iteration])
        self.game_screen.blit(self.blend_screen, (0, 0))
