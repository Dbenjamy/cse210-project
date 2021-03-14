import random
from game import constants
from game.action import Action
from game.dirt import Dirt

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    
    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        car = cast["car"][0]

        if cast["dirt_top"][0].center_x <= constants.MAX_X / 2 * -1:
            cast["dirt_top"].pop(0)
            cast["dirt_bottom"].pop(0)
            self._add_track(cast)


        dirt_slow = False
        for dirt in cast["dirt_top"]:
            if dirt_slow:
                break
            if self._handle_car_collision(car,dirt):
                dirt_slow = True

        for dirt in cast["dirt_bottom"]:
            if dirt_slow:
                break
            if self._handle_car_collision(car,dirt):
                dirt_slow = True
                break

        if dirt_slow:
            for dirt in cast["dirt_top"]:
                dirt.change_x = -1
            for dirt in cast["dirt_bottom"]:
                dirt.change_x = -1
        elif not dirt_slow:
            for dirt in cast["dirt_top"]:
                dirt.change_x = -5
            for dirt in cast["dirt_bottom"]:
                dirt.change_x = -5



    def _add_track(self,cast):
        cast["dirt_top"].append(Dirt(constants.DIRT_TOP))
        cast["dirt_top"][1].center_x = cast["dirt_top"][0].center_x + constants.MAX_X
        cast["dirt_top"][1].center_y = cast["dirt_top"][0].center_y
        cast["dirt_bottom"].append(Dirt(constants.DIRT_BOTTOM))
        cast["dirt_bottom"][1].center_x = cast["dirt_bottom"][0].center_x + constants.MAX_X
        cast["dirt_bottom"][1].center_y = cast["dirt_bottom"][0].center_y

    def _handle_car_collision(self,car,dirt):
        return car.collides_with_sprite(dirt)
