from dataclasses import dataclass, field
from enum import Enum
from typing import Any
from abc import ABC, abstractmethod
from EffectDefinition import EffectDefinition

class CardType(Enum):
    ITEM = "ITEM"
    SUPPORT = "SUPPORT"
    STADIUM = "STADIUM"
    TOOL = "TOOL"
    
class TargetType(Enum):
    SELF_POKEMON = "SELF_POKEMON"
    OPPONENT_POKEMON = "OPPONENT_POKEMON"
    ALL_POKEMON = "ALL_POKEMON"
    PLAYER = "PLAYER"
    TILE = "TILE"
    GLOBAL = "GLOBAL"

@dataclass(frozen=True)
class CardDefintion:
    card_id: int = 0
    name: str = ""
    description: str = ""
    card_type: CardType = CardType.ITEM
    target_type: TargetType = TargetType.SELF_POKEMON
    effects: tuple[EffectDefinition, ...] = field(default_factory=tuple)  # A tuple of EffectDefinition objects