from dataclasses import dataclass
from enum import Enum

class CardStateEnum(Enum):
    IN_HAND = 1
    IN_DECK = 2
    IN_DISCARD_PILE = 3
    IN_PLAY = 4

@dataclass
class CardState:
    player_id: int
    card_id: int
    name: str
    type: str
    state: CardStateEnum