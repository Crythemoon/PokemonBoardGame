from dataclasses import dataclass

@dataclass
class PlayerConfig:
    player_id: int
    name: str
    team_id: int
    deck_id: int