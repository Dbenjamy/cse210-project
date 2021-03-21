from game.point import Point
from game import constants
from random import choice as choice
import arcade

class Obstacles(arcade.Sprite):
    def __init__(self,x_coordinate=None,y_coordinate=None):

        super().__init__(choice(constants.OBSTACLES_LIST))
        if x_coordinate != None:
            self.center_x = x_coordinate
        else:
            self.center_x = int(constants.MAX_X/2)
        
        if y_coordinate != None:
            self.center_y = y_coordinate
        else:
            self.center_y = int(constants.MAX_Y/2)
        self.change_x = -5

    def add_obstacle(self,obstacles):
        obstacles.append(Obstacles)