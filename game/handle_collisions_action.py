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
                dirt.change_x = -2
            for dirt in cast["dirt_bottom"]:
                dirt.change_x = -2



    def _add_track(self,cast):
        cast["dirt_top"].append(Dirt(constants.DIRT_TOP))
        cast["dirt_top"][1].center_x = cast["dirt_top"][0].center_x + constants.MAX_X
        cast["dirt_bottom"].append(Dirt(constants.DIRT_BOTTOM))
        cast["dirt_bottom"][1].center_x = cast["dirt_bottom"][0].center_x + constants.MAX_X

    def _handle_car_collision(self,car,dirt):
        return car.collides_with_sprite(dirt)

    def _handle_paddle_bounce(self, ball, paddle):
        # This makes use of the `Sprite` functionality
        if paddle.collides_with_sprite(ball):
            # Ball and paddle collide!
            ball.bounce_horizontal()

    def _handle_brick_collision(self, ball, bricks):
        brick_to_remove = None

        for brick in bricks:
            # This makes use of the `Sprite` functionality
            if ball.collides_with_sprite(brick):
                ball.bounce_horizontal()
                brick_to_remove = brick
        
        if brick_to_remove != None:
            bricks.remove(brick_to_remove)

    def _is_off_screen(self, ball):
        return ball.center_y < 0