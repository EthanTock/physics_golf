import pygame as pg
from boye import Boye
from colorsets import COLORSETS
import math

# Constants
WINDOW_DIMENSIONS = WINDOW_X, WINDOW_Y = 1080, 720
SCREEN_CENTER = SCREEN_CENTER_X, SCREEN_CENTER_Y = WINDOW_X / 2, WINDOW_Y / 2
FRAMERATE = 60

CHOSEN_COLORSET = COLORSETS["neon_city"]
BG_COLOR = CHOSEN_COLORSET["bg"]
WALL_COLOR = CHOSEN_COLORSET["wall"]
BALL_COLOR = CHOSEN_COLORSET["ball"]
OBJ_COLOR = CHOSEN_COLORSET["obj"]

# Init statements
pg.init()

# Display
screen = pg.display.set_mode(WINDOW_DIMENSIONS)

# Time
clock = pg.time.Clock()
dt = 0

# Objects in-game
walls = [
    (pg.Rect(0, 0, 1080, 100), math.pi * 3/2),
    (pg.Rect(0, 0, 100, 720), 0),
    (pg.Rect(0, 720 - 100, 1080, 100), math.pi / 2),
    (pg.Rect(1080 - 100, 0, 100, 720), math.pi),
    (pg.Rect(540-40, 360+10, 40, 360), math.pi),
    (pg.Rect(540-40, 360, 80, 20), math.pi / 2),
    (pg.Rect(540, 360+10, 40, 360), 0),
]

my_boy = Boye(SCREEN_CENTER, color=BALL_COLOR)

# Game
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(BG_COLOR)

    keys_down = pg.key.get_pressed()

    # Draw walls
    for wall in walls:
        wall_rect = wall[0]
        wall_angle = wall[1]
        pg.draw.rect(screen, WALL_COLOR, wall_rect)
        if my_boy.hitbox.colliderect(wall_rect):
            while my_boy.hitbox.colliderect(wall_rect):
                my_boy.shift_angular(1, wall_angle)
            reflected_angle = 2*wall_angle - my_boy.angle() - math.pi
            my_boy.set_velocity_angular(my_boy.speed(), reflected_angle)

    pg.draw.rect(screen, OBJ_COLOR, pg.Rect(200, 200, 50, 50))

    # Draw my boy
    pg.draw.rect(screen, my_boy.color, my_boy.hitbox)

    if keys_down[pg.K_RIGHT]:
        my_boy.add_to_velocity(0.1, 0)
    if keys_down[pg.K_LEFT]:
        my_boy.add_to_velocity(-0.1, 0)
    if keys_down[pg.K_DOWN]:
        my_boy.add_to_velocity(0, 0.1)
    if keys_down[pg.K_UP]:
        my_boy.add_to_velocity(0, -0.1)
    my_boy.move()

    pg.display.flip()

    dt = clock.tick(FRAMERATE) / 1000
