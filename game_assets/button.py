import pygame as pg
from game_config import GRID_SIZE


def noop(*args, **kwargs):
    pass


class Button:
    def __init__(self, top_left_tiles, dimensions_tiles, perma_down, holdable, action=noop, action_args=(), action_kwargs={}):
        self.action = action
        self.action_args = action_args
        self.action_kwargs = action_kwargs

        self.top_left_tiles = self.top_left_tiles_x, self.top_left_tiles_y = top_left_tiles
        self.dimensions_tiles = self.dimensions_tiles_x, self.dimensions_tiles_y = dimensions_tiles
        self.top_left = self.top_left_x, self.top_left_y = self.top_left_tiles_x * GRID_SIZE, self.top_left_tiles_y * GRID_SIZE
        self.dimensions = self.dimensions_x, self.dimensions_y = self.dimensions_tiles_x * GRID_SIZE, self.dimensions_tiles_y * GRID_SIZE

        self.interact_box = pg.Rect(self.top_left, self.dimensions)
        self.active = True
        self.holdable = holdable
        self.perma_down = perma_down

    def do_action(self):
        self.action(*self.action_args, **self.action_kwargs)

    def down(self):
        if self.active:
            self.do_action()
        if not self.holdable:
            self.active = False

    def up(self):
        if not self.perma_down:
            self.active = True
