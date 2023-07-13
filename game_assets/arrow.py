import pygame as pg
import math


class Arrow:
    def __init__(self, tail_pos, angle, length, max_length, thickness, color):
        self.tail_pos = tail_pos
        self.angle = angle
        self.length = length
        self.max_length = max_length
        self.head_pos = self.calculate_head_pos()
        self.thickness = thickness
        self.color = color

        self.main_line_kwargs = {"color": self.color, "start_pos": self.tail_pos, "end_pos": self.head_pos, "width": self.thickness}

    def draw(self, screen):
        pg.draw.line(screen, **self.main_line_kwargs)

    def calculate_head_pos(self):
        return self.tail_pos[0] + math.cos(self.angle) * self.length, self.tail_pos[1] - math.sin(self.angle) * self.length

    def update_main_line_kwargs(self):
        self.main_line_kwargs = {"color": self.color, "start_pos": self.tail_pos, "end_pos": self.head_pos, "width": self.thickness}

    def update_tail_pos(self, new_tail_pos):
        self.tail_pos = new_tail_pos
        self.head_pos = self.calculate_head_pos()
        self.update_main_line_kwargs()

    def update_length(self, new_length):
        if 0 <= new_length < self.max_length:
            self.length = new_length
        self.head_pos = self.calculate_head_pos()
        self.update_main_line_kwargs()

    def update_angle(self, new_angle):
        while new_angle > 2 * math.pi:
            new_angle -= 2 * math.pi
        while new_angle < 0:
            new_angle += 2 * math.pi
        self.angle = new_angle
        self.head_pos = self.calculate_head_pos()
        self.update_main_line_kwargs()
