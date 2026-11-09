from dataclasses import dataclass, field
from enum import Enum
from server.Definition.CardDefinition import CardDefintion

class CardStateEnum(Enum):
    IN_HAND = 1
    IN_DECK = 2
    IN_DISCARD_PILE = 3
    IN_PLAY = 4

@dataclass
class CardState:
    player_id: int = 0
    state: CardStateEnum = CardStateEnum.IN_DECK
    card_defintion: CardDefintion = field(default_factory=CardDefintion)