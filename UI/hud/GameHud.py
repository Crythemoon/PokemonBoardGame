import arcade.gui

class GameHUD:
    def __init__(self):
        self.selected_slot = None
        self.team_buttons = []

    def select_pokemon(self,slot:int):
        if self.selected_slot == slot:
            self.selected_slot = None
        else:
            self.selected_slot = slot

        for button in self.team_buttons:
            button.set_selected(
                button.slot == self.selected_slot
            )