import pygame as pg
import math

DEFAULT_COLOR = "red"
BASE_SIZE = 20
MAX_SPEED = 25  # TODO Figure out how to incorporate a max speed and a deceleration
DECELERATION_POWER = .01
SPEED_LOWER_THRESHOLD = 0.05


class Ball:
    def __init__(self, position_tl, size=BASE_SIZE, color=DEFAULT_COLOR):
        self.color = color

        self.size = size

        self.position_tl = self.position_tl_x, self.position_tl_y = position_tl
        self.velocity = self.velocity_x, self.velocity_y = (0, 0)
        self.acceleration = self.acceleration_x, self.acceleration_y = (0, 0)

        self.hitbox = pg.Rect(position_tl, (size, size))

    def shift(self, dx, dy):
        # check if hitbox is colliding with anything...
        self.position_tl_x += dx
        self.position_tl_y += dy
        self.position_tl = (self.position_tl_x, self.position_tl_y)

        self.hitbox.update(self.position_tl, (self.size, self.size))

    def shift_angular(self, distance, angle):
        dx = math.cos(angle) * distance
        dy = math.sin(angle) * distance * -1
        self.shift(dx, dy)

    def move(self):
        self.shift(self.velocity_x, self.velocity_y)
        self.decelerate()
        if self.speed() < SPEED_LOWER_THRESHOLD:
            self.velocity = self.velocity_x, self.velocity_y = (0, 0)

    def set_velocity(self, v_x, v_y):
        self.velocity_x = v_x
        self.velocity_y = v_y

    def set_velocity_angular(self, magnitude, angle):
        v_x = math.cos(angle) * magnitude
        v_y = math.sin(angle) * magnitude * -1
        self.set_velocity(v_x, v_y)

    def add_to_velocity(self, add_x, add_y):
        if self.speed() < MAX_SPEED:
            self.velocity_x += add_x
            self.velocity_y += add_y

    def add_to_velocity_angular(self, magnitude, angle):
        add_x = math.cos(angle) * magnitude
        add_y = math.sin(angle) * magnitude * -1
        self.add_to_velocity(add_x, add_y)

    def speed(self):
        return math.sqrt(self.velocity_x ** 2 + self.velocity_y ** 2)

    def angle(self):
        if abs(self.speed()) > 0:
            x_angle = math.acos(self.velocity_x / self.speed())
            y_angle = math.asin(-self.velocity_y / self.speed())
            if y_angle < 0:
                return math.pi * 2 - x_angle
            else:
                return x_angle
        return 0

    def invert_velocity(self):
        self.set_velocity(-self.velocity_x, -self.velocity_y)

    def decelerate(self, power=DECELERATION_POWER):
        self.velocity_x *= 1 - power
        self.velocity_y *= 1 - power
        self.velocity = (self.velocity_x, self.velocity_y)

    def update_color(self, new_color):
        self.color = new_color
