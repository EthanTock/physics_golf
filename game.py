import pygame as pg
from game_assets.ball import Ball
from game_assets.wall_box import WallBox
from game_assets.grid_showcase import GridShowcase
from game_assets.button import Button
from colorsets import COLORSETS
from game_config import GRID_SIZE, BUTTON_DARKNESS
import math

# Constants
WINDOW_DIMENSIONS = WINDOW_X, WINDOW_Y = 1080, 720
SCREEN_CENTER = SCREEN_CENTER_X, SCREEN_CENTER_Y = WINDOW_X / 2, WINDOW_Y / 2
FRAMERATE = 60

CHOSEN_COLORSET = COLORSETS["neon_sewers"]
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
    (pg.Rect(0, 0, 1080, 5), math.pi * 3/2),
    (pg.Rect(0, 0, 5, 720), 0),
    (pg.Rect(0, 720-5, 1080, 5), math.pi / 2),
    (pg.Rect(1080-5, 0, 5, 720), math.pi),
    (pg.Rect(540-40, 370, 40, 100), math.pi),   # Create a Box object out of these 3, 4th wall added.
    (pg.Rect(540, 370, 40, 100), 0),            # An idea here is to create a cornerboost mechanic.
    (pg.Rect(540-40, 360, 80, 5), math.pi / 2),
    (pg.Rect(540-40, 475, 80, 5), math.pi * 3/2)
]
walls.extend(
    WallBox((5, 5), (5, 3)).walls
)
walls.extend(
    WallBox((15, 7), (7, 7), "horizontal", ("up", "left")).walls
)

buttons = [
    Button((5, 15), (2, 2), False, False, print, ("hello world!", "h"), {"end": "lol\n", "sep": "       "})
]

grid_showcase = GridShowcase(screen, WINDOW_DIMENSIONS, GRID_SIZE)

ball = Ball((SCREEN_CENTER_X - 10, 200), color=BALL_COLOR)

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
        pg.draw.rect(screen, WALL_COLOR, wall[0])
        if ball.hitbox.colliderect(wall_rect):
            print(ball.speed())
            while ball.hitbox.colliderect(wall_rect):
                ball.shift_angular(1, wall_angle)
            reflected_angle = 2 * wall_angle - ball.angle() - math.pi
            ball.set_velocity_angular(ball.speed(), reflected_angle)

    # Interact-able
    for button in buttons:
        if ball.hitbox.colliderect(button.interact_box):
            button.down()
            pg.draw.rect(screen, tuple([b * BUTTON_DARKNESS for b in OBJ_COLOR]), button.interact_box)
        else:
            button.up()
            pg.draw.rect(screen, OBJ_COLOR, button.interact_box)

    # Draw my boy
    pg.draw.rect(screen, ball.color, ball.hitbox)

    if keys_down[pg.K_RIGHT]:
        ball.add_to_velocity(0.1, 0)
    if keys_down[pg.K_LEFT]:
        ball.add_to_velocity(-0.1, 0)
    if keys_down[pg.K_DOWN]:
        ball.add_to_velocity(0, 0.1)
    if keys_down[pg.K_UP]:
        ball.add_to_velocity(0, -0.1)
    ball.move()

    if keys_down[pg.K_g]:
        grid_showcase.draw_lines()

    pg.display.flip()

    dt = clock.tick(FRAMERATE) / 1000
