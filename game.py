import pygame as pg
from game_assets.ball import Ball
from game_assets.wall_box import WallBox
from game_assets.grid_showcase import GridShowcase
from game_assets.button import Button
from game_assets.arrow import Arrow
from colorsets import COLORSETS
from levels import LEVELS
from game_config import GRID_SIZE, BUTTON_DARKNESS
import math

# Constants
GRID_DIMENSIONS = GRID_X, GRID_Y = 54, 36
WINDOW_DIMENSIONS = WINDOW_X, WINDOW_Y = GRID_X * GRID_SIZE, GRID_Y * GRID_SIZE
SCREEN_CENTER = SCREEN_CENTER_X, SCREEN_CENTER_Y = WINDOW_X / 2, WINDOW_Y / 2
FRAMERATE = 60

# Init statements
pg.init()

# Display
screen = pg.display.set_mode(WINDOW_DIMENSIONS)

# Time
clock = pg.time.Clock()
dt = 0

# Objects in-game
outer_walls = [
    (pg.Rect(0, 0, 1080, 20), math.pi * 3/2),
    (pg.Rect(0, 0, 20, 720), 0),
    (pg.Rect(0, 720-20, 1080, 20), math.pi / 2),
    (pg.Rect(1080-20, 0, 20, 720), math.pi),
]

current_level = LEVELS["1"]
all_walls = outer_walls
for w in current_level.wall_boxes:
    all_walls.extend(w.walls)
for w in current_level.named_wall_boxes.values():
    all_walls.extend(w.walls)

grid_showcase = GridShowcase(screen, WINDOW_DIMENSIONS, ("tan", "blue", "magenta", "red"), (1, 1, 2, 3), (1, 2, 5, 10))  # ("steelblue4", "springgreen3", "tan1")

ball = Ball((SCREEN_CENTER_X - 10, 200), color=current_level.ball_color)

ball_arrow = Arrow(ball.center(), 0, 30, 48, 3, "white")

# Game
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(current_level.bg_color)

    keys_down = pg.key.get_pressed()

    # Draw walls
    for wall in all_walls:
        wall_rect = wall[0]
        wall_angle = wall[1]
        pg.draw.rect(screen, current_level.wall_color, wall[0])
        if ball.hitbox.colliderect(wall_rect):
            while ball.hitbox.colliderect(wall_rect):
                ball.shift_angular(1, wall_angle)
            reflected_angle = 2 * wall_angle - ball.angle() - math.pi
            ball.set_velocity_angular(ball.speed(), reflected_angle)

    # Interact-able
    for button in current_level.buttons:
        if ball.hitbox.colliderect(button.interact_box):
            button.down()
            pg.draw.rect(screen, tuple([b * BUTTON_DARKNESS for b in current_level.obj_color]), button.interact_box)
        else:
            button.up()
            pg.draw.rect(screen, current_level.obj_color, button.interact_box)

    # Draw ball
    pg.draw.rect(screen, ball.color, ball.hitbox)

    # Draw ball arrow
    ball_arrow.draw(screen)

    # Ball motion
    if keys_down[pg.K_RIGHT]:
        ball_arrow.update_angle(ball_arrow.angle - math.pi/90)
    if keys_down[pg.K_LEFT]:
        ball_arrow.update_angle(ball_arrow.angle + math.pi/90)
    if keys_down[pg.K_DOWN]:
        ball_arrow.update_length(ball_arrow.length - 1)
    if keys_down[pg.K_UP]:
        ball_arrow.update_length(ball_arrow.length + 1)
    if keys_down[pg.K_SPACE] and not ball.in_motion():
        # TODO Set a timer for the next time space can be hit...
        ball.set_velocity_angular(ball_arrow.length/3, ball_arrow.angle)
    ball.move()
    ball_arrow.update_tail_pos(ball.center())

    if keys_down[pg.K_g]:
        grid_showcase.draw_lines()

    pg.display.flip()

    dt = clock.tick(FRAMERATE) / 1000
