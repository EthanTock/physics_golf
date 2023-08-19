import pygame as pg
from game_config import WINDOW_DIMENSIONS, GRID_SIZE


class SelectionBox:
    def __init__(self, game_screen, starting_point, opacity, color):
        self.game_screen = game_screen
        self.grid_starting_point = [coord // GRID_SIZE for coord in starting_point]
        self.starting_point = [coord * GRID_SIZE for coord in self.grid_starting_point]
        self.opacity = opacity
        self.color = color
        self.is_active = True
        self.is_hidden = False

        self.transparent_surface = pg.Surface(WINDOW_DIMENSIONS)
        self.transparent_surface.set_alpha(self.opacity)
        self.transparent_surface.set_colorkey("black")

        self.moving_corner_position = (0, 0)
        self.center_corner_position = (0, 0)
        self.selection_box = self.calculate_rectangle()

    def hide(self):
        self.is_hidden = True

    def show(self):
        self.is_hidden = False

    def keep_still(self):
        self.is_active = False

    def update_corner_positions(self):
        final_grid_mouse_coords = [coord // GRID_SIZE for coord in pg.mouse.get_pos()]
        final_grid_center_corner_coords = self.grid_starting_point[:]
        if final_grid_mouse_coords[0] < self.grid_starting_point[0]:
            final_grid_center_corner_coords[0] += 1
        else:
            final_grid_mouse_coords[0] += 1
        if final_grid_mouse_coords[1] < self.grid_starting_point[1]:
            final_grid_center_corner_coords[1] += 1
        else:
            final_grid_mouse_coords[1] += 1
        self.moving_corner_position = [coord * GRID_SIZE for coord in final_grid_mouse_coords]
        self.center_corner_position = [coord * GRID_SIZE for coord in final_grid_center_corner_coords]

    def calculate_rectangle(self):
        self.update_corner_positions()
        return pg.Rect(
            min(self.moving_corner_position[0], self.center_corner_position[0]),   # Left
            min(self.moving_corner_position[1], self.center_corner_position[1]),   # Top
            abs(self.moving_corner_position[0] - self.center_corner_position[0]),  # Width
            abs(self.moving_corner_position[1] - self.center_corner_position[1])   # Height
        )

    def update_transparent_surface(self):
        self.transparent_surface.fill("black")
        self.selection_box = self.calculate_rectangle()
        pg.draw.rect(self.transparent_surface, self.color, self.selection_box)

    def get_wall_box_args(self):
        grid_top_left = [coord // GRID_SIZE for coord in self.selection_box.topleft]
        grid_dimensions = [dimension // GRID_SIZE for dimension in self.selection_box.size]
        return grid_top_left, grid_dimensions

    def draw(self):
        if not self.is_hidden:
            if self.is_active:
                self.update_transparent_surface()
            self.game_screen.blit(self.transparent_surface, (0, 0))
