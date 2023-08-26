import pygame as pg
from game_config import GRID_SIZE


class Decal:
    def __init__(self, game_screen, left_top_tiles, dimensions_tiles, image_filename, image_opacity, tint_color, tint_opacity, image_colorkey=None):
        self.left_top_tiles = self.left_top_tiles_x, self.left_top_tiles_y = left_top_tiles
        self.left_top = self.left_top_x, self.left_top_y = [coord * GRID_SIZE for coord in self.left_top_tiles]
        self.dimensions_tiles = self.dimensions_tiles_x, self.dimensions_tiles_y = dimensions_tiles
        self.dimensions = self.dimensions_x, self.dimensions_y = [dimension * GRID_SIZE for dimension in self.dimensions_tiles]

        self.image_filename = image_filename
        self.image_opacity = image_opacity
        self.image_colorkey = image_colorkey
        self.tint_color = tint_color
        self.tint_opacity = tint_opacity

        self.game_screen = game_screen
        try:
            self.transparent_image = pg.image.load(self.image_filename).convert()
            self.transparent_image = pg.transform.scale(self.transparent_image, self.dimensions)
            self.transparent_image.set_alpha(self.image_opacity)
            if self.image_colorkey:
                self.transparent_image.set_colorkey(self.image_colorkey)
        except FileNotFoundError:
            self.transparent_image = pg.Surface(self.dimensions)
            self.transparent_image.set_alpha(0)
        self.transparent_tint_layer = pg.Surface(self.dimensions)
        self.transparent_tint_layer.set_alpha(self.tint_opacity)
        self.transparent_tint_layer.fill(self.tint_color)

    def draw(self):
        self.game_screen.blits(((self.transparent_image, self.left_top), (self.transparent_tint_layer, self.left_top)))

    def colorpick_at(self, x_y):
        return self.transparent_image.get_at(x_y)
