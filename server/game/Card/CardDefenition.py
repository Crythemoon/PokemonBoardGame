from dataclasses import dataclass, field
from enum import Enum
from typing import Any
from abc import ABC, abstractmethod

class CardType(Enum):
    ITEM = "item"
    SUPPORT = "support"
    TRAINER = "trainer"
    
class TargetType(Enum):
    SELF = "self"
    FRIENDLY_POKEMON = "friendly_pokemon"
    ENEMY_POKEMON = "enemy_pokemon"
    ANY_POKEMON = "any_pokemon"
    
@dataclass(frozen=True)
class TargetRef:
    target_type: TargetType
    target_id: int
    
class CardEffect(ABC):
    
    @abstractmethod
    def apply(self, target: Any):
        pass

class CardRequirement(Enum):
    ENERGY = "energy"
    POKEMON_TYPE = "pokemon_type"
    STATUS = "status"

class CardRestriction(Enum):
    NONE = "none"
    ONCE_PER_BATTLE = "once_per_battle"
    ONCE_PER_TURN = "once_per_turn"

@dataclass(frozen=True)
class CardDefintion:
    cardID: int
    name: str
    description: str
    
    card_type: CardType
    target_type: TargetType
    
    effects: tuple[CardEffect, ...] = ()
    requirements: tuple[CardRequirement, ...] = ()
    restrictions: tuple[CardRestriction, ...] = ()
    
    max_targets: int = 1
    
    """
    This class returns the restriction of the card based on the cardID. The restriction is a dictionary that contains the following keys:
    """
    def getCardRestriction(cardID):
        pass
    
    """
    This class returns the card object based on the cardID. The card object contains the following attributes:
    - cardID: The ID of the card
    
    """
    def getCard(cardID):
        pass