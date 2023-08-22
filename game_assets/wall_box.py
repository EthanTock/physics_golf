import pygame as pg
from math import pi
from game_config import GRID_SIZE

DEFAULT_COLOR = "black"
THIN_WALL_THICKNESS = 8


class WallBox:
    def __init__(self, top_left_tiles, dimensions_tiles, name="", orientation="vertical", sides=["right", "up", "left", "down"], color=DEFAULT_COLOR):
        self.top_left_tiles = self.top_left_tiles_x, self.top_left_tiles_y = top_left_tiles
        self.dimensions_tiles = self.dimensions_tiles_x, self.dimensions_tiles_y = dimensions_tiles
        self.top_left = self.top_left_x, self.top_left_y = self.top_left_tiles_x * GRID_SIZE, self.top_left_tiles_y * GRID_SIZE
        self.dimensions = self.dimensions_x, self.dimensions_y = self.dimensions_tiles_x * GRID_SIZE, self.dimensions_tiles_y * GRID_SIZE

        self.name = name

        self.orientation = orientation
        self.sides = sides
        self.color = color

        self.walls = []

        self.create_walls()

    def to_kwargs(self):
        return {
            "top_left_tiles": self.top_left_tiles,
            "dimensions_tiles": self.dimensions_tiles,
            "name": self.name,
            "orientation": self.orientation,
            "sides": self.sides,
            "color": self.color
        }

    def has_name(self):
        return bool(self.name)

    def toggle_side(self, side):
        if side in ("right", "up", "left", "down"):
            if side in self.sides:
                self.sides.remove(side)
            else:
                self.sides.append(side)
        self.create_walls()

    def rotate(self):
        if self.orientation == "vertical":
            self.orientation = "horizontal"
        else:
            self.orientation = "vertical"
        self.create_walls()

    def create_walls(self):
        self.walls = []
        if "right" in self.sides:
            if self.orientation == "horizontal":
                self.walls.append(
                    (
                        pg.Rect(
                            self.top_left_x + self.dimensions_x - THIN_WALL_THICKNESS,
                            self.top_left_y,
                            THIN_WALL_THICKNESS,
                            self.dimensions_y
                        ),
                        0
                    )
                )
            else:
                self.walls.append(
                    (
                        pg.Rect(
                            self.top_left_x + self.dimensions_x/2,
                            self.top_left_y + 2*THIN_WALL_THICKNESS,
                            self.dimensions_x/2,
                            self.dimensions_y - 4*THIN_WALL_THICKNESS
                        ),
                        0
                    )
                )
        if "up" in self.sides:
            if self.orientation == "vertical":
                self.walls.append(
                    (
                        pg.Rect(
                            self.top_left_x,
                            self.top_left_y,
                            self.dimensions_x,
                            THIN_WALL_THICKNESS
                        ),
                        pi/2
                    )
                )
            else:
                self.walls.append(
                    (
                        pg.Rect(
                            self.top_left_x + 2*THIN_WALL_THICKNESS,
                            self.top_left_y,
                            self.dimensions_x - 4*THIN_WALL_THICKNESS,
                            self.dimensions_y/2
                        ),
                        pi/2
                    )
                )
        if "left" in self.sides:
            if self.orientation == "horizontal":
                self.walls.append(
                    (
                        pg.Rect(
                            self.top_left_x,
                            self.top_left_y,
                            THIN_WALL_THICKNESS,
                            self.dimensions_y
                        ),
                        pi
                    )
                )
            else:
                self.walls.append(
                    (
                        pg.Rect(
                            self.top_left_x,
                            self.top_left_y + 2 * THIN_WALL_THICKNESS,
                            self.dimensions_x/2,
                            self.dimensions_y - 4 * THIN_WALL_THICKNESS
                        ),
                        pi
                    )
                )
        if "down" in self.sides:
            if self.orientation == "vertical":
                self.walls.append(
                    (
                        pg.Rect(
                            self.top_left_x,
                            self.top_left_y + self.dimensions_y - THIN_WALL_THICKNESS,
                            self.dimensions_x,
                            THIN_WALL_THICKNESS
                        ),
                        pi * 3/2
                    )
                )
            else:
                self.walls.append(
                    (
                        pg.Rect(
                            self.top_left_x + 2*THIN_WALL_THICKNESS,
                            self.top_left_y + self.dimensions_y/2,
                            self.dimensions_x - 4*THIN_WALL_THICKNESS,
                            self.dimensions_y/2
                        ),
                        pi * 3/2
                    )
                )
