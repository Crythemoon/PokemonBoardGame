from arcade import load_texture as Alt
import arcade.gui as argui
from .pokemon_panel import Pokemon_Team_Hud

class GameHUD:
    def __init__(self):
        #HUD manager
        self.manager = argui.UIManager()
        
        #HUD UI anchor
        self.anchor = argui.UIAnchorLayout()
        
        self.anchor.add(
            Pokemon_Team_Hud().team_layout,
            anchor_x = "left",
            anchor_y = "center",
            )
        
        self.manager.add(self.anchor)
    
    def enable(self):
        self.manager.enable()
    
    def disable(self):
        self.manager.disable()
    
    def draw(self):
        self.manager.draw()