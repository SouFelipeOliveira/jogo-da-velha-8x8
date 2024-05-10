import pygame as pg
import numpy as np


#|------ PIXELS ------|


WIDTH = 800
HEIGHT = 800

ROWS = 8
COLS = 8

SQUARE_SIZE = WIDTH // COLS


LINE_WIDTH = 10
CIRC_WIDTH = 15
CROSS_WIDTH = 20

RADIUS = SQUARE_SIZE // 4

OFFSET = 50

screen = pg.display.set_mode((WIDTH, HEIGHT))

#|------ COLORS ------|

BG_COLOR = (125, 129, 148)
LINE_COLOR = (80, 85, 111)
CIRC_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
LINE_RED = (255, 8, 0)