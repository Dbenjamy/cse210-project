from game.point import Point
from game import constants

import arcade

class Dirt(arcade.Sprite):
    def __init__(self,image_file):

        super().__init__(image_file)
        self.center_x = int(constants.MAX_X/2)
        self.center_y = int(constants.MAX_Y/2)
        self.change_x = -5
        
