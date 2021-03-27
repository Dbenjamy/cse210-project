from game.point import Point
from game import constants

import arcade

class Dirt(arcade.Sprite):
    def __init__(self,image_file):

        super().__init__(image_file)
        self.center_x = int(constants.MAX_X/2)
        self.center_y = int(constants.MAX_Y/2)
        self.change_x = -5
        self.counter = 1
        self.finished = False

    def add_track(self,the_cast):
        self.counter += 1
        the_cast["dirt_top"].append(Dirt(constants.DIRT_TOP))
        the_cast["dirt_top"][1].center_x = the_cast["dirt_top"][0].center_x + constants.MAX_X
        the_cast["dirt_top"][1].center_y = the_cast["dirt_top"][0].center_y
        the_cast["dirt_bottom"].append(Dirt(constants.DIRT_BOTTOM))
        the_cast["dirt_bottom"][1].center_x = the_cast["dirt_bottom"][0].center_x + constants.MAX_X
        the_cast["dirt_bottom"][1].center_y = the_cast["dirt_bottom"][0].center_y
        if self.counter == 3:
            self.show_finish(the_cast)      

    def show_finish(self,cast):

        cast["FINISH_LINE"].append(Dirt(constants.FINISH_LINE))
        cast["FINISH_LINE"][0].center_y = constants.MAX_Y / 2
        cast["FINISH_LINE"][0].center_x = constants.MAX_X + 180

        self.finished = True
