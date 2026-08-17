import arcade
import os

MAIN_PATH = os.path.dirname(os.path.abspath(__file__))
MENU_OBJECT = os.path.join(MAIN_PATH, "pokesprite","Menu")

#FONT

DEFAULT_FONT = ("Kenny Future", "arial")

#Menu

MAIN_MENU_BACKGROUND = arcade.load_texture(f'{MENU_OBJECT}\\MenuBackground.png')
PAUSE_MENU_BACKGROUND = arcade.load_texture("background.png")

PLAY_BUTTON_NORMAL = arcade.load_texture("play_normal.png")
PLAY_BUTTON_HOVER = arcade.load_texture("play_hover.png")
PLAY_BUTTON_PRESS = arcade.load_texture("play_press.png")

SETTINGS_BUTTON_NORMAL = arcade.load_texture("settings_normal.png")
SETTINGS_BUTTON_HOVER = arcade.load_texture("settings_hover.png")
SETTINGS_BUTTON_PRESS = arcade.load_texture("settings_press.png")

EXIT_BUTTON_NORMAL = arcade.load_texture("exit_normal.png")
EXIT_BUTTON_HOVER = arcade.load_texture("exit_hover.png")
EXIT_BUTTON_PRESS = arcade.load_texture("exit_press.png")