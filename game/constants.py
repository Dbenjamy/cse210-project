import os
from pathlib import Path
DIR = Path(__file__).resolve().parent
DIRROOT = DIR.resolve().parent

MAX_X = 800
MAX_Y = 600


CAR_X = 25

CAR_MOVE_SCALE = 10

DIRT_TOP = DIRROOT.joinpath("images/DIRT_IMAGES/top1.png")
DIRT_BOTTOM = DIRROOT.joinpath("images/DIRT_IMAGES/bottom1.png")


CAR_IMAGE = DIRROOT.joinpath("images/paddle-0.png")