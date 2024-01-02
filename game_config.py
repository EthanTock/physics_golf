import pygame as pg

GRID_DIMENSIONS = GRID_X, GRID_Y = 54, 36
GRID_SIZE = 20
WINDOW_DIMENSIONS = WINDOW_X, WINDOW_Y = GRID_X * GRID_SIZE, GRID_Y * GRID_SIZE
SCREEN_CENTER = SCREEN_CENTER_X, SCREEN_CENTER_Y = WINDOW_X / 2, WINDOW_Y / 2

BUTTON_DARKNESS = .90

DEBUG_FONT = "./PTMono.ttc"
DEBUG_FONT_SIZE = 15

FUNCTION_KEYS = {
    "exit": pg.K_ESCAPE,
    "terminal": pg.K_4,
    "show_grid": pg.K_g,
    "tool_pointer": pg.K_v,
    "tool_rect": pg.K_r,
    "tool_rect_orient_horizontal": pg.K_RIGHT,
    "tool_rect_orient_vertical": pg.K_UP,
    "tool_rect_finalize": pg.K_RETURN
}

DEFAULT_LEVEL = "empty"
