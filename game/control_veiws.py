import arcade
from game import constants
# from game.action import Action
# from game.menu import Main_Menu
# from game.pause import Pause_Menu
from game.arcade_input_service import ArcadeInputService

class Views():

    def __init__(self):
        # self.main_menu = Main_Menu()
        # window = arcade.Window(constants.MAX_X,constants.MAX_Y,constants.GAME_TITLE)
        # self._view = view
        # self.pause_menu = Pause_Menu()
        # self._input_service = ArcadeInputService()
        # self.set_window(window)
        self.window = arcade.Window(constants.MAX_X,constants.MAX_Y,constants.GAME_TITLE)
        
    # def get_window(self):
    #     windowsave = self.window
    #     self.set_window(windowsave)

    def execute_main(self, view):
        print("this works too")
        self.window.show_view(view)

    def execute_game(self, view):
        print("made it")
        self.window.show_view(view)
