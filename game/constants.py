import os
from pathlib import Path
DIR = Path(__file__).resolve().parent
DIRROOT = DIR.resolve().parent

MAX_X = 800
MAX_Y = 600
NUM_BALLS = 5

BALL_SPEED = 3
BALL_Y = MAX_Y / 2

CAR_X = 25

CAR_MOVE_SCALE = 10

BRICK_WIDTH = 25
BRICK_HEIGHT = 15
BRICK_SPACE = 10

BALLS_CAN_DIE = False

BALL_IMAGE = DIRROOT.joinpath("images/ball-0.png")

DIRT_TOP = DIRROOT.joinpath("images/DIRT_IMAGES/top1.png")
DIRT_BOTTOM = DIRROOT.joinpath("images/DIRT_IMAGES/bottom1.png")


CAR_IMAGE = DIRROOT.joinpath("images/paddle-0.png")
BRICK_IMAGE = DIRROOT.joinpath("images/brick-0.png")
