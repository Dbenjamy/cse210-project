import sys
from game.point import Point

import arcade

class ArcadeInputService:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _keys (list): up, dn, lt, rt.
    """

    def __init__(self):
        """The class constructor."""
        self._keys = []
    
    def set_key(self, key, modifiers):
        #Ignoring modifies ar this point...
        self._keys.append(key)

    def remove_key(self, key, modifiers):
        self._keys.remove(key)

    def get_direction(self):
        """Gets the selected direction for the given player.

        Returns:
            Point: The selected direction.
        """
        x = 0
        y = 0

        # EDIT: Car will not move forward and backward. Removed funcionality for
        # letting user change x value
        
        #if arcade.key.LEFT in self._keys:
            #x = -1
        #elif arcade.key.RIGHT in self._keys:
            #x = 1

        if arcade.key.UP in self._keys:
            y = 1
        elif arcade.key.DOWN in self._keys:
            y = -1

        velocity = Point(x, y)
        return velocity

    def set_parameter(self, cast, script, input_service):
        self._cast = cast
        self._script = script
        self._input_service = input_service
            
    def get_view(self):
        from game.director import Director
        director = Director(self._cast, self._script, self._input_service)
        if arcade.key.P in self._keys:
            self.director.set_pause(True)
        
    # def on_key_press(self, symbol):
    #     if symbol == arcade.key.P:
    #         return "P"