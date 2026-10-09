from dataclasses import dataclass

@dataclass
class DeckConfig:
    player_id: int
    deck_id: int
    name: str
    cards: list