from colorsets import COLORSETS
from game_assets.wall_box import WallBox
from game_assets.button import Button
from game_assets.hole import Hole
import pygame as pg
import json
import math

OUTER_WALLS = [
    (pg.Rect(0, 0, 1080, 20), math.pi * 3/2),
    (pg.Rect(0, 0, 20, 720), 0),
    (pg.Rect(0, 720-20, 1080, 20), math.pi / 2),
    (pg.Rect(1080-20, 0, 20, 720), math.pi),
]

DEFAULT_HOLE_ARGS = {
    "left_top": (20, 20),
    "dimensions": (20, 20)
}


class Level:
    def __init__(self, name, colorset="grayscale", unnamed_wall_boxes=(), named_wall_boxes={}, buttons={}, start_point=(0, 0), hole=DEFAULT_HOLE_ARGS):
        self.name = name
        self.colorset = colorset
        self.bg_color = COLORSETS[self.colorset]["bg"]
        self.wall_color = COLORSETS[self.colorset]["wall"]
        self.ball_color = COLORSETS[self.colorset]["ball"]
        self.obj_color = COLORSETS[self.colorset]["obj"]
        self.unnamed_wall_boxes = [WallBox(**args) for args in unnamed_wall_boxes]
        self.named_wall_boxes = {name: WallBox(**kwargs) for name, kwargs in named_wall_boxes.items()}
        self.buttons = {name: Button(**kwargs) for name, kwargs in buttons.items()}
        self.start_point = start_point
        self.hole = Hole(**hole)

    def to_dict(self):
        return {
            "name": self.name,
            "colorset": self.colorset,
            "unnamed_wall_boxes": [wall_box.to_kwargs() for wall_box in self.unnamed_wall_boxes],
            "named_wall_boxes": {wall_box.name: wall_box.to_kwargs() for wall_box in self.named_wall_boxes},
            "buttons": {button.name: button.to_kwargs() for button in self.buttons},
            "start_point": self.start_point,
            "hole": self.hole.to_kwargs()
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    def save_to_levels_json(self):
        try:
            with open(f"./levels_json/{self.name}.json", "x") as json_file:
                json_file.write(self.to_json())
        except FileExistsError:
            with open(f"./levels_json/{self.name}.json", "w") as json_file:
                json_file.write(self.to_json())

    def add_wall_box(self, new_wall_box):
        if new_wall_box.name:
            self.named_wall_boxes.update({new_wall_box.name: new_wall_box})
        else:
            self.unnamed_wall_boxes.append(new_wall_box)

    def pop_wall_box(self):
        if self.unnamed_wall_boxes:
            self.unnamed_wall_boxes.pop()

    def get_all_walls(self):
        all_walls = OUTER_WALLS.copy()
        for w in self.unnamed_wall_boxes:
            all_walls.extend(w.walls)
        for w in self.named_wall_boxes.values():
            all_walls.extend(w.walls)
        return all_walls

    def update_colorset(self, new_colorset):
        if new_colorset in COLORSETS.keys():
            self.colorset = new_colorset
            self.bg_color = COLORSETS[self.colorset]["bg"]
            self.wall_color = COLORSETS[self.colorset]["wall"]
            self.ball_color = COLORSETS[self.colorset]["ball"]
            self.obj_color = COLORSETS[self.colorset]["obj"]
