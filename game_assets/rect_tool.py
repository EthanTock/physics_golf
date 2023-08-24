from game_assets.wall_box import WallBox
from game_assets.selection_box import SelectionBox
from game_config import WINDOW_DIMENSIONS
import pygame as pg


class RectTool:
    def __init__(self, game_screen, color, opacity):
        self.color = color
        self.opacity = opacity

        self.game_screen = game_screen
        self.incomplete_rect_transparent_surface = pg.Surface(WINDOW_DIMENSIONS)
        self.incomplete_rect_transparent_surface.set_alpha(self.opacity)
        self.incomplete_rect_transparent_surface.set_colorkey("black")

        self.current_selection_box = None
        self.current_selection_wall_box_args = None
        self.new_wall_box = None
        self.state = 0
        # State 0: not selected.
        # State 1: moving selection.
        # State 2: stationary selection & edit.
        # State 3: rect is ready.
        self.will_undo = False

        self.keys_down = []
        self.previous_keys_down = []
        self.mouse_position = (0, 0)
        self.mouse_buttons_down = pg.mouse.get_pressed()
        self.previous_mouse_state = "up"

    def listen(self, keys_down):
        mouse_position = pg.mouse.get_pos()
        mouse_buttons_down = pg.mouse.get_pressed()
        self.update_keys_down(keys_down)
        self.update_mouse_state(mouse_position, mouse_buttons_down)
        self.handle_events()
        self.draw()

    def update_mouse_state(self, position, buttons_down):
        self.previous_mouse_state = "up"
        for button in self.mouse_buttons_down:
            if button:
                self.previous_mouse_state = "down"
        self.mouse_position = position
        self.mouse_buttons_down = buttons_down

    def update_keys_down(self, keys_down):
        self.previous_keys_down = self.keys_down
        self.keys_down = keys_down

    def handle_events(self):
        if self.keys_down[pg.K_u] and not self.previous_keys_down[pg.K_u]:
            self.will_undo = True

        left_click, right_click = False, False
        if self.previous_mouse_state == "up":
            if self.mouse_buttons_down[0]:
                left_click = True
            elif self.mouse_buttons_down[2]:
                right_click = True

        if self.state == 0 and left_click:
            self.init_selection()
        elif self.state == 1 and left_click:
            self.finalize_selection()
        elif self.state == 2:
            for side_pair in ((pg.K_UP, "up"), (pg.K_LEFT, "left"), (pg.K_DOWN, "down"), (pg.K_RIGHT, "right")):
                if self.keys_down[side_pair[0]] and not self.previous_keys_down[side_pair[0]]:
                    self.new_wall_box.toggle_side(side_pair[1])
            if self.keys_down[pg.K_SPACE] and not self.previous_keys_down[pg.K_SPACE]:
                self.new_wall_box.rotate()
            if self.keys_down[pg.K_QUOTE] and not self.previous_keys_down[pg.K_QUOTE]:
                pass  # TODO do something for naming here
            if left_click:
                self.place_rect()
            pass
        elif right_click:
            self.reset()

    def init_selection(self):
        self.current_selection_box = SelectionBox(self.game_screen, self.mouse_position, self.opacity, self.color)
        self.state = 1

    def finalize_selection(self):
        self.current_selection_wall_box_args = self.current_selection_box.get_wall_box_args()
        self.new_wall_box = WallBox(*self.current_selection_wall_box_args)
        self.state = 2

    def place_rect(self):
        self.state = 3

    def draw(self):
        self.incomplete_rect_transparent_surface.fill("black")
        if self.state == 1:
            self.draw_selection()
        elif self.state == 2:
            self.draw_incomplete_rect()

    def draw_selection(self):
        self.current_selection_box.draw()

    def draw_incomplete_rect(self):
        for wall in self.new_wall_box.walls:
            pg.draw.rect(self.incomplete_rect_transparent_surface, self.color, wall[0])
        self.game_screen.blit(self.incomplete_rect_transparent_surface, (0, 0))

    def reset(self):
        self.state = 0

    def rect_is_ready(self):
        if self.state == 3:
            self.state = 0
            return True
        return False

    def check_undo(self):
        if self.will_undo:
            self.will_undo = False
            return True
        return False
