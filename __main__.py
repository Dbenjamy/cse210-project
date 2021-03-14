import random
from game import constants
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.arcade_input_service import ArcadeInputService
from game.arcade_output_service import ArcadeOutputService

from game.car import Car
from game.dirt import Dirt

from game.director import Director
import arcade

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    car = Car()
    cast["car"] = [car]

    cast["dirt_top"] = []
    cast["dirt_bottom"] = []
    cast["dirt_top"].append(Dirt(constants.DIRT_TOP))
    cast["dirt_top"].append(Dirt(constants.DIRT_TOP))
    cast["dirt_bottom"].append(Dirt(constants.DIRT_BOTTOM))
    cast["dirt_bottom"].append(Dirt(constants.DIRT_BOTTOM))


    cast["dirt_top"][0].center_y = constants.MAX_Y / 25
    cast["dirt_bottom"][0].center_y = 0 + constants.MAX_Y / 25

    cast["dirt_top"][1].center_x += constants.MAX_X
    cast["dirt_top"][1].center_y = constants.MAX_Y / 25
    cast["dirt_bottom"][1].center_x += constants.MAX_X
    cast["dirt_bottom"][1].center_y = 0 + constants.MAX_Y / 25


    # create the script {key: tag, value: list}
    script = {}

    input_service = ArcadeInputService()
    output_service = ArcadeOutputService()
    
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script, input_service)
    director.setup()
    arcade.run()


if __name__ == "__main__":
    main()