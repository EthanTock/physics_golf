import pygame as pg

GRID_DIMENSIONS = GRID_X, GRID_Y = 54, 36
GRID_SIZE = 20
WINDOW_DIMENSIONS = WINDOW_X, WINDOW_Y = GRID_X * GRID_SIZE, GRID_Y * GRID_SIZE

BUTTON_DARKNESS = .90

DEBUG_FONT = "./PTMono.ttc"
DEBUG_FONT_SIZE = 15

FUNCTION_KEYS = {
    "exit": pg.K_ESCAPE,
    "terminal": pg.K_4,
    "show_grid": pg.K_g
}
