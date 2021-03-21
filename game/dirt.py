from game.point import Point
from game import constants

import arcade

class Dirt(arcade.Sprite):
    def __init__(self,image_file):

        super().__init__(image_file)
        self.center_x = int(constants.MAX_X/2)
        self.center_y = int(constants.MAX_Y/2)
        self.change_x = -5

    def add_track(self,the_cast):
        the_cast["dirt_top"].append(Dirt(constants.DIRT_TOP))
        the_cast["dirt_top"][1].center_x = the_cast["dirt_top"][0].center_x + constants.MAX_X
        the_cast["dirt_top"][1].center_y = the_cast["dirt_top"][0].center_y
        the_cast["dirt_bottom"].append(Dirt(constants.DIRT_BOTTOM))
        the_cast["dirt_bottom"][1].center_x = the_cast["dirt_bottom"][0].center_x + constants.MAX_X
        the_cast["dirt_bottom"][1].center_y = the_cast["dirt_bottom"][0].center_y