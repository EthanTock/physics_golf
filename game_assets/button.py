import pygame as pg
from game_config import GRID_SIZE, BUTTON_DARKNESS


def noop(*args, **kwargs):
    pass


class Button:
    def __init__(self, top_left_tiles, dimensions_tiles, name="", perma_down=False, holdable=False, action=noop, action_args=(), action_kwargs={}):
        if type(action) == str:
            self.action = eval(action)
        else:
            self.action = action
        self.action_args = action_args
        self.action_kwargs = action_kwargs

        self.top_left_tiles = self.top_left_tiles_x, self.top_left_tiles_y = top_left_tiles
        self.dimensions_tiles = self.dimensions_tiles_x, self.dimensions_tiles_y = dimensions_tiles
        self.top_left = self.top_left_x, self.top_left_y = self.top_left_tiles_x * GRID_SIZE, self.top_left_tiles_y * GRID_SIZE
        self.dimensions = self.dimensions_x, self.dimensions_y = self.dimensions_tiles_x * GRID_SIZE, self.dimensions_tiles_y * GRID_SIZE

        self.interact_box = pg.Rect(self.top_left, self.dimensions)
        self.active = True
        self.is_down = False
        self.holdable = holdable
        self.perma_down = perma_down
        self.name = name

    def to_kwargs(self):
        return {
            "top_left_tiles": self.top_left_tiles,
            "dimensions_tiles": self.dimensions_tiles,
            "name": self.name,
            "perma_down": self.perma_down,
            "holdable": self.holdable,
            "action": self.action,
            "action_args": self.action_args,
            "action_kwargs": self.action_kwargs
        }

    def to_json_safe_kwargs(self):
        return self.to_kwargs().update({"action": str(self.action)})

    def has_name(self):
        return bool(self.name)

    def do_action(self):
        self.action(*self.action_args, **self.action_kwargs)

    def down(self):
        self.is_down = True
        if self.active:
            self.do_action()
        if not self.holdable:
            self.active = False

    def up(self):
        self.is_down = False
        if not self.perma_down:
            self.active = True

    def draw(self, game_screen, color):
        if self.is_down:
            color = tuple([b * BUTTON_DARKNESS for b in color])
        pg.draw.rect(game_screen, color, self.interact_box)
