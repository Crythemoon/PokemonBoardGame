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

class Pokemon_Team_Hud:
    """
    Initializing Pokemon Team HUD
    
    Args:
    - pokemon_team: a dictionary of the pokemon team [player_pokemon_id, pokemon_name]
    """
    def __init__(self,pokemon_team:dict[int,str]):
        self.manager = argui.UIManager()
        
        self.anchor = argui.UIAnchorLayout()
        
        self.is_alive = True
        self.is_selected = False
        
        self.button = argui.UITextureButton(
            texture=PARTY_SLOT,
            width=197,
            height=95
        )
        
    def create_team_view(self):
        team_view = argui.UIButtonRow(
            vertical=True,
        )
        team_view.with_padding(all=10)
        # Creating Button for each pokemon on the team
        