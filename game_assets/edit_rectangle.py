import pygame as pg
from game_config import WINDOW_DIMENSIONS, GRID_SIZE


class EditRectangle:
    def __init__(self, game_screen, starting_point, opacity, color):
        self.game_screen = game_screen
        self.grid_starting_point = [coord // GRID_SIZE for coord in starting_point]
        self.starting_point = [coord * GRID_SIZE for coord in self.grid_starting_point]
        self.opacity = opacity
        self.color = color

        self.transparent_surface = pg.Surface(WINDOW_DIMENSIONS)
        self.transparent_surface.set_alpha(self.opacity)
        self.transparent_surface.fill("black")
        self.transparent_surface.set_colorkey("black")

        self.moving_corner_position = (0, 0)
        self.edit_rectangle = self.calculate_rectangle()

    def update_moving_corner_position(self):
        mouse_coords = pg.mouse.get_pos()
        grid_mouse_coords = [coord // GRID_SIZE for coord in mouse_coords]
        final_grid_mouse_coords = grid_mouse_coords[:]
        if grid_mouse_coords[0] >= self.grid_starting_point[0]:
            final_grid_mouse_coords[0] += 1
        if grid_mouse_coords[1] >= self.grid_starting_point[1]:
            final_grid_mouse_coords[1] += 1
        self.moving_corner_position = [coord * GRID_SIZE for coord in final_grid_mouse_coords]

    def calculate_rectangle(self):
        self.update_moving_corner_position()
        return pg.Rect(
            min(self.moving_corner_position[0], self.starting_point[0]),   # Left
            min(self.moving_corner_position[1], self.starting_point[1]),   # Top
            abs(self.moving_corner_position[0] - self.starting_point[0]),  # Width
            abs(self.moving_corner_position[1] - self.starting_point[1])   # Height
        )

    def update_transparent_surface(self):
        self.transparent_surface.fill("black")
        self.edit_rectangle = self.calculate_rectangle()
        pg.draw.rect(self.transparent_surface, self.color, self.edit_rectangle)

    def draw(self):
        self.update_transparent_surface()
        self.game_screen.blit(self.transparent_surface, (0, 0))
