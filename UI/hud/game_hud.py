import arcade.gui

class GameHUD:
    def __init__(self, on_end_turn):
        self.manager = arcade.gui.UIManager()
        self.on_end_turn = on_end_turn

        # Main layout covering the window
        self.anchor = arcade.gui.UIAnchorLayout()

        self.manager.add(self.anchor)

        self._body = arcade.gui.UIAnchorLayout(size_hint=(0.7,1))

    def pokemon_party(self):
        box = arcade.gui.UIBoxLayout(
            vertical=True,
            size_hint=(1,1),
            align="left",
            space_between=10
        )