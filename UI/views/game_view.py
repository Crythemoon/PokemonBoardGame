import arcade
import arcade.gui

class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        self.background_color = arcade.color.WHITE

        self.ui = arcade.gui.UIManager()

        