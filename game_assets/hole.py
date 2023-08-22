import pygame as pg
from game_config import GRID_SIZE


class Hole:
    def __init__(self, left_top, dimensions, color="black"):
        self.left_top = left_top
        self.dimensions = dimensions
        self.rect = pg.Rect([coord * GRID_SIZE for coord in self.left_top], [dimension * GRID_SIZE for dimension in self.dimensions])
        self.color = color

    def to_kwargs(self):
        return {
            "left_top": self.left_top,
            "dimensions": self.dimensions,
            "color": self.color
        }
