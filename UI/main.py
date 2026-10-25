import arcade
from views.game_view import GameView

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Pokemon Board Game"

def main():
    window = arcade.Window(
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        SCREEN_TITLE,
        resizable=True
    )

    game_view = GameView()
    window.show_view(game_view)

    arcade.run()

if __name__ == "__main__":
    main()