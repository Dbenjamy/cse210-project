import arcade
import time
from game import constants
from game.newtimer import Timer
import datetime

class Director(arcade.View):
    def __init__(self, cast, script, input_service):
        """Initialize the game
        """
        super().__init__()

        self._cast = cast
        self._script = script
        self._input_service = input_service
        self.total_time = 0.0
        self.timer = Timer()
        self.slow_music = None
        self._sound_dictionary = {'engine':':resources:music/funkyrobot.mp3','slow_engine':':resources:sounds/gameover2.wav'}

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)
        # self.set_pause(False)
        self.play_song()

    # def set_pause(self, pause):
    #     self.game_paused = pause

    def on_update(self, delta_time):
        from game.arcade_input_service import ArcadeInputService
        self.pause_key = ArcadeInputService()
        # self.pause_key.set_parameter(self._cast, self._script, self._input_service)
        # self.pause_key.get_view()

        # if self.game_paused == False:
        if not(self.pause_key.get_view() == "P"):
            self._cue_action("update")
            self.total_time += delta_time
            self.timer.timer_draw(self.total_time)
        if self.pause_key.get_view() == "P":
            from game.pause import Pause_Menu
            pause_screen = Pause_Menu()
            pause_screen.set_parameter(self._cast, self._script, self._input_service)
            print("Made it this far")
            self.window.show_view(pause_screen)
            # self.set_pause(False)
        else:
            self._cue_action("update")
            self.total_time += delta_time
            self.timer.timer_draw(self.total_time)

    def on_draw(self):
        self._cue_action("output")

    def on_key_press(self, symbol, modifiers):
        self._input_service.set_key(symbol, modifiers)
        self._cue_action("input")

    def on_key_release(self, symbol, modifiers):
        self._input_service.remove_key(symbol, modifiers)
        self._cue_action("input")

    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)
            
    def play_song(self):
        """ Play the song. """
        # Stop what is currently playing.
        print('This works')
        if self.slow_music:
            self.slow_music.stop()
        self.slow_music = arcade.Sound(self._sound_dictionary['engine'], streaming = True)
        self.slow_music.play(volume=1)
