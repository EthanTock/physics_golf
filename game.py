import pygame as pg
from game_assets.ball import Ball
from game_assets.grid_showcase import GridShowcase
from game_assets.arrow import Arrow
from game_assets.wall_box import WallBox
from game_assets.terminal import Terminal
from game_assets.level_command_executor import LevelCommandExecutor
from game_assets.selection_box import SelectionBox
from levels import LEVELS
from game_config import WINDOW_DIMENSIONS, WINDOW_X, WINDOW_Y, GRID_SIZE, BUTTON_DARKNESS, DEBUG_FONT, DEBUG_FONT_SIZE, FUNCTION_KEYS
import math

# Constants
SCREEN_CENTER = SCREEN_CENTER_X, SCREEN_CENTER_Y = WINDOW_X / 2, WINDOW_Y / 2
FRAMERATE = 60

# Init statements
pg.init()

# Display
screen = pg.display.set_mode(WINDOW_DIMENSIONS)
pg.display.set_caption("Physics Golf")
app_icon = pg.image.load("./static/sharkboi.png")
pg.display.set_icon(app_icon)
alpha_layer = pg.Surface(WINDOW_DIMENSIONS)
alpha_layer.set_alpha(30)

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
previous_level = current_level


def get_all_walls():
    all_walls = outer_walls.copy()
    for w in current_level.wall_boxes:
        all_walls.extend(w.walls)
    for w in current_level.named_wall_boxes.values():
        all_walls.extend(w.walls)
    return all_walls


# grid_showcase = GridShowcase(screen, 256, ("blue", "red", "yellow", "white"), (1, 1, 2, 3), (1, 2, 5, 10))  # ("steelblue4", "springgreen3", "tan1")
grid_showcase = GridShowcase(screen, 64, ["white"], [1], [1])

ball = Ball((SCREEN_CENTER_X - 10, 200), color=current_level.ball_color)

ball_arrow = Arrow(ball.center(), 0, 30, 48, 3, "white")

level_command_executor = LevelCommandExecutor(current_level)
terminal = Terminal(screen, level_command_executor)

TEST_SELECTION_BOX = SelectionBox(screen, (100, 100), 100, "white")
current_selection_box = None
rect_args_complete = False

current_tool = "pointer"

# Command States
zoomies = False
grid_on = False

# Game
editor_mode = False
running = True
events = []
previous_mouse_position = "up"
current_mouse_position = "up"
while running:
    # print(previous_mouse_position, current_mouse_position)
    previous_mouse_position = current_mouse_position
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            current_mouse_position = "down"
        elif event.type == pg.MOUSEBUTTONUP:
            current_mouse_position = "up"

    screen.fill(current_level.bg_color)

    keys_down = pg.key.get_pressed()

    if keys_down[FUNCTION_KEYS["exit"]]:
        running = False

    # Draw walls
    for wall in get_all_walls():
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

    if not editor_mode:
        # == PLAY MODE ==
        # Draw ball
        pg.draw.rect(screen, current_level.ball_color, ball.hitbox)

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
        if keys_down[pg.K_SPACE] and (zoomies or not ball.in_motion()):
            ball.set_velocity_angular(ball_arrow.length/3, ball_arrow.angle)
        ball.move()
        ball_arrow.update_tail_pos(ball.center())
    else:
        # == EDITOR MODE ==
        # Tool selection
        if keys_down[FUNCTION_KEYS["tool_pointer"]]:
            current_tool = "pointer"
        elif keys_down[FUNCTION_KEYS["tool_rect"]]:
            current_tool = "rect"
        tool_text = pg.font.Font(DEBUG_FONT, DEBUG_FONT_SIZE).render(f"{current_tool} ({pg.key.name(FUNCTION_KEYS['tool_' + current_tool])})", False, "white")
        screen.blit(tool_text, (WINDOW_X - 10 * GRID_SIZE, 0))

        title_text = pg.font.Font(DEBUG_FONT, DEBUG_FONT_SIZE).render(f"'{current_level.name}'", False, "white")
        screen.blit(title_text, (0, 0))

        if current_tool == "rect":
            # Left click to begin box
            if not current_selection_box and pg.mouse.get_pressed()[0] and previous_mouse_position == "up":
                if not current_selection_box:
                    current_selection_box = SelectionBox(screen, pg.mouse.get_pos(), 50, "white")
                    new_wall_box = None
                    rect_args_complete = False
            # Left click to end box
            elif current_selection_box and pg.mouse.get_pressed()[0] and previous_mouse_position == "up":
                if current_selection_box.is_active:
                    new_wall_box = WallBox(*current_selection_box.get_wall_box_args())
                    current_selection_box.is_active = False
            # Take args, await enter to finish box
            if current_selection_box and not current_selection_box.is_active:
                if not rect_args_complete:
                    if keys_down[FUNCTION_KEYS["tool_rect_orient_vertical"]]:
                        new_wall_box.orientation = "vertical"
                        new_wall_box.create_walls()
                    elif keys_down[FUNCTION_KEYS["tool_rect_orient_horizontal"]]:
                        new_wall_box.orientation = "horizontal"
                        new_wall_box.create_walls()
                    if keys_down[FUNCTION_KEYS["tool_rect_finalize"]]:
                        rect_args_complete = True
                else:
                    current_level.wall_boxes.append(new_wall_box)
                    rect_args_complete = False
                    current_selection_box = None
            # Right click
            if pg.mouse.get_pressed()[2]:
                current_selection_box = None
            if current_selection_box:
                current_selection_box.draw()

        # have a saving feature to the LEVELS dict...

    if keys_down[FUNCTION_KEYS["show_grid"]] or grid_on:
        grid_showcase.draw_lines()
        pg.mouse.set_cursor(pg.cursors.broken_x)
        coords_raw_text = str(tuple([p // GRID_SIZE for p in pg.mouse.get_pos()]))
        coords_font = pg.font.Font(DEBUG_FONT, DEBUG_FONT_SIZE)
        coords_text = coords_font.render(coords_raw_text, False, "white")
        coords_rect = coords_text.get_rect(topleft=pg.mouse.get_pos())
        screen.blit(coords_text, coords_rect)
    else:
        pg.mouse.set_cursor(pg.cursors.arrow)

    if keys_down[FUNCTION_KEYS["terminal"]]:
        terminal.turn_on()
    if terminal.is_on:
        terminal.run(events)

    for command in level_command_executor.commands:
        if command == "change":
            current_level = level_command_executor.level
            level_command_executor.on_new_level = False
        elif command == "edit":
            editor_mode = True
        elif command == "play":
            editor_mode = False
        elif command == "zoomies":
            zoomies = True
        elif command == "nozoomies":
            zoomies = False
        elif command == "grid":
            grid_on = True
        elif command == "nogrid":
            grid_on = False

    pg.display.flip()

    dt = clock.tick(FRAMERATE) / 1000
