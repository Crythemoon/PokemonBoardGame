import arcade
from game_hud import GameHUD as ghud


SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

class test(arcade.View):
    def __init__(self):
        super().__init__()
        self.HUD = ghud()
        
    def on_show_view(self):
        arcade.set_background_color(arcade.color.WHITE)
        self.HUD.enable()
        
    def on_hide_view(self):
        self.HUD.disable()
    
    def on_draw(self):
        self.clear()
        self.HUD.draw()
        
def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Test")
    test_view = test()
    window.show_view(test_view)
    arcade.run()
    
if __name__ == "__main__":
    main()