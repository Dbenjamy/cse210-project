from game.action import Action
from game import constants

import arcade

class DrawActorsAction(Action):
    """A code template for drawing actors.
    
    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

    def __init__(self, output_service):
        """The class constructor.
        
        Args:
            _output_service (OutputService): An instance of OutputService.
        """
        self._output_service = output_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._output_service.clear_screen()

        # bricks = cast["bricks"]

        # for brick in bricks:
        #     self._output_service.draw_actor(brick)

        for dirt in cast["dirt"]:
            self._output_service.draw_actor(dirt)

        car = cast["car"][0] # there's only one
        self._output_service.draw_actor(car)

        self._output_service.flush_buffer()

