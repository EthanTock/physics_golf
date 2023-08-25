import pygame as pg
from math import pi
from game_config import GRID_SIZE

DEFAULT_COLOR = "black"
THIN_WALL_THICKNESS = 10
CLIP_DEPTH = 2 * THIN_WALL_THICKNESS


class WallBox:
    def __init__(self, top_left_tiles, dimensions_tiles, name="", orientation="vertical", sides=("right", "up", "left", "down"), color=DEFAULT_COLOR):
        self.top_left_tiles = self.top_left_tiles_x, self.top_left_tiles_y = top_left_tiles
        self.dimensions_tiles = self.dimensions_tiles_x, self.dimensions_tiles_y = dimensions_tiles
        self.top_left = self.top_left_x, self.top_left_y = self.top_left_tiles_x * GRID_SIZE, self.top_left_tiles_y * GRID_SIZE
        self.dimensions = self.dimensions_x, self.dimensions_y = self.dimensions_tiles_x * GRID_SIZE, self.dimensions_tiles_y * GRID_SIZE

        self.name = name

        self.orientation = orientation
        self.sides = list(sides)
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
        main_walls = []
        side_walls = []

        # Create walls
        if self.orientation == "horizontal":
            halfway_y = self.top_left_y + 1/2 * self.dimensions_y
            if "up" in self.sides:
                main_walls.append((pg.Rect(self.top_left, (self.dimensions_x, halfway_y - self.top_left_y)), pi/2))
            if "down" in self.sides:
                main_walls.append((pg.Rect((self.top_left_x, halfway_y), (self.dimensions_x, halfway_y - self.top_left_y)), 3 * pi/2))
            if "left" in self.sides:
                side_walls.append((pg.Rect(self.top_left, (THIN_WALL_THICKNESS, self.dimensions_y)), pi))
            if "right" in self.sides:
                side_walls.append((pg.Rect((self.top_left_x + self.dimensions_x - THIN_WALL_THICKNESS, self.top_left_y), (THIN_WALL_THICKNESS, self.dimensions_y)), 0))
        elif self.orientation == "vertical":
            halfway_x = self.top_left_x + 1/2 * self.dimensions_x
            if "left" in self.sides:
                main_walls.append((pg.Rect(self.top_left, (halfway_x - self.top_left_x, self.dimensions_y)), pi))
            if "right" in self.sides:
                main_walls.append((pg.Rect((halfway_x, self.top_left_y), (halfway_x - self.top_left_x, self.dimensions_y)), 0))
            if "up" in self.sides:
                side_walls.append((pg.Rect(self.top_left, (self.dimensions_x, THIN_WALL_THICKNESS)), pi/2))
            if "down" in self.sides:
                side_walls.append((pg.Rect((self.top_left_x, self.top_left_y + self.dimensions_y - THIN_WALL_THICKNESS), (self.dimensions_x, THIN_WALL_THICKNESS)), 3 * pi/2))
        # Clipping to provide space for thin walls
        clip_rects = []
        if self.orientation == "horizontal":
            if "left" in self.sides:
                clip_rects.append(pg.Rect((self.top_left_x + CLIP_DEPTH, self.top_left_y), (self.dimensions_x - CLIP_DEPTH, self.dimensions_y)))
            if "right" in self.sides:
                clip_rects.append(pg.Rect(self.top_left, (self.dimensions_x - CLIP_DEPTH, self.dimensions_y)))
        if self.orientation == "vertical":
            if "up" in self.sides:
                clip_rects.append(pg.Rect((self.top_left_x, self.top_left_y + CLIP_DEPTH), (self.dimensions_x, self.dimensions_y - CLIP_DEPTH)))
            if "down" in self.sides:
                clip_rects.append(pg.Rect(self.top_left, (self.dimensions_x, self.dimensions_y - CLIP_DEPTH)))
        for clip_rect in clip_rects:
            new_main_walls = []
            for wall, angle in main_walls:
                new_main_walls.append((wall.clip(clip_rect), angle))
            main_walls = new_main_walls

        self.walls.extend(main_walls)
        self.walls.extend(side_walls)

        # if "right" in self.sides:
        #     if self.orientation == "horizontal":
        #         self.walls.append(
        #             (
        #                 pg.Rect(
        #                     self.top_left_x + self.dimensions_x - THIN_WALL_THICKNESS,
        #                     self.top_left_y,
        #                     THIN_WALL_THICKNESS,
        #                     self.dimensions_y
        #                 ),
        #                 0
        #             )
        #         )
        #     else:
        #         self.walls.append(
        #             (
        #                 pg.Rect(
        #                     self.top_left_x + self.dimensions_x/2,
        #                     self.top_left_y + 2*THIN_WALL_THICKNESS,
        #                     self.dimensions_x/2,
        #                     self.dimensions_y - 4*THIN_WALL_THICKNESS
        #                 ),
        #                 0
        #             )
        #         )
        # if "up" in self.sides:
        #     if self.orientation == "vertical":
        #         self.walls.append(
        #             (
        #                 pg.Rect(
        #                     self.top_left_x,
        #                     self.top_left_y,
        #                     self.dimensions_x,
        #                     THIN_WALL_THICKNESS
        #                 ),
        #                 pi/2
        #             )
        #         )
        #     else:
        #         self.walls.append(
        #             (
        #                 pg.Rect(
        #                     self.top_left_x + 2*THIN_WALL_THICKNESS,
        #                     self.top_left_y,
        #                     self.dimensions_x - 4*THIN_WALL_THICKNESS,
        #                     self.dimensions_y/2
        #                 ),
        #                 pi/2
        #             )
        #         )
        # if "left" in self.sides:
        #     if self.orientation == "horizontal":
        #         self.walls.append(
        #             (
        #                 pg.Rect(
        #                     self.top_left_x,
        #                     self.top_left_y,
        #                     THIN_WALL_THICKNESS,
        #                     self.dimensions_y
        #                 ),
        #                 pi
        #             )
        #         )
        #     else:
        #         self.walls.append(
        #             (
        #                 pg.Rect(
        #                     self.top_left_x,
        #                     self.top_left_y + 2 * THIN_WALL_THICKNESS,
        #                     self.dimensions_x/2,
        #                     self.dimensions_y - 4 * THIN_WALL_THICKNESS
        #                 ),
        #                 pi
        #             )
        #         )
        # if "down" in self.sides:
        #     if self.orientation == "vertical":
        #         self.walls.append(
        #             (
        #                 pg.Rect(
        #                     self.top_left_x,
        #                     self.top_left_y + self.dimensions_y - THIN_WALL_THICKNESS,
        #                     self.dimensions_x,
        #                     THIN_WALL_THICKNESS
        #                 ),
        #                 pi * 3/2
        #             )
        #         )
        #     else:
        #         self.walls.append(
        #             (
        #                 pg.Rect(
        #                     self.top_left_x + 2*THIN_WALL_THICKNESS,
        #                     self.top_left_y + self.dimensions_y/2,
        #                     self.dimensions_x - 4*THIN_WALL_THICKNESS,
        #                     self.dimensions_y/2
        #                 ),
        #                 pi * 3/2
        #             )
        #         )
