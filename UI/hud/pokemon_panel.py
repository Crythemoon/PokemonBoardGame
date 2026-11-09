from arcade import load_texture as Alt
from arcade import gui as argui
from pathlib import Path

HUD_DIR = Path(__file__).resolve().parent
GUI_DIR = HUD_DIR.parent / "gui"
PARTY_DIR = GUI_DIR / "party"

# Loading party slot texture
PARTY_SLOT = Alt(f'{PARTY_DIR}/party_slot.png')
PARTY_SLOT_ACTIVE = Alt(f'{PARTY_DIR}/party_slot_active.png')
PARTY_SLOT_COLLAPSED = Alt(f'{PARTY_DIR}/party_slot_collapsed.png')
PARTY_SLOT_FAINTED_ACTIVE = Alt(f'{PARTY_DIR}/party_slot_fainted_active.png')
PARTY_SLOT_FAINTED = Alt(f'{PARTY_DIR}/party_slot_fainted.png')
PARTY_SLOT_STATUS_BURN = Alt(f'{PARTY_DIR}/status_brn.png')
PARTY_SLOT_STATUS_FREEZE = Alt(f'{PARTY_DIR}/status_frz.png')
PARTY_SLOT_STATUS_PARALIZED = Alt(f'{PARTY_DIR}/status_par.png')
PARTY_SLOT_STATUS_POSION = Alt(f'{PARTY_DIR}/status_psn.png')
PARTY_SLOT_STATUS_SLEEP = Alt(f'{PARTY_DIR}/status_slp.png')
PARTY_SLOT_STATUS_TOXIC = Alt(f'{PARTY_DIR}/status_tox.png')
PARTY_SLOT_BACKGROUND = Alt(f'{PARTY_DIR}/party_slot_portrait_background.png')

BUTTON_TEXTURE = {
    "alive_active": PARTY_SLOT_ACTIVE,
    "alive_inactive": PARTY_SLOT,
    "fainted_active": PARTY_SLOT_FAINTED_ACTIVE,
    "fainted_inactive": PARTY_SLOT_FAINTED,
}

BUTTON_WIDTH = 197
BUTTON_HEIGHT = 95

class Pokemon_Team_Hud:
    def __init__(self):              
        self.team_layout = argui.UIBoxLayout(
            vertical = True
        )
        # Creating Button for each pokemon on the team
        for i in range(6):
            #Creating the base for the button
            team_base_button = Pokemon_Team_Button()
            self.team_layout.add(team_base_button.button)
            #Creating the background for the pokemon avatar
            @team_base_button.button.event("on_click")
            def on_click(event):
                team_base_button.is_selected = not team_base_button.is_selected
                team_base_button.update_button_texture()
            
        
class Pokemon_Team_Button():
    def __init__(self):
        self.is_alive = True
        self.is_selected = False
        
        self.button = argui.UITextureButton(
            texture=PARTY_SLOT,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT
        )
        
    def update_button_texture(self):
        status = "alive" if self.is_alive else "fainted"
        selection = "active" if self.is_selected else "inactive"
        texture_key = f"{status}_{selection}"
        self.button.texture = BUTTON_TEXTURE[texture_key]
        self.button.update_texture()