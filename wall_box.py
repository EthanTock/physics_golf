import pygame as pg
from math import pi

DEFAULT_COLOR = "black"
THIN_WALL_THICKNESS = 5


class WallBox:
    def __init__(self, top_left_tiles, dimensions_tiles, orientation="vertical", sides=("right", "up", "left", "down"), color=DEFAULT_COLOR):
        self.top_left_tiles = self.top_left_tiles_x, self.top_left_tiles_y = top_left_tiles
        self.dimensions_tiles = self.dimensions_tiles_x, self.dimensions_tiles_y = dimensions_tiles

        self.top_left = self.top_left_x, self.top_left_y = self.top_left_tiles_x * 20, self.top_left_tiles_y * 20
        self.dimensions = self.dimensions_x, self.dimensions_y = self.dimensions_tiles_x * 20, self.dimensions_tiles_y * 20

        self.orientation = orientation
        self.sides = sides
        self.color = color

        self.walls = []
        self.create_walls()

    def create_walls(self):
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
