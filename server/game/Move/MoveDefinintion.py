from dataclasses import dataclass, field
from Pokemon.PokemonObject import PokemonTypeEnum as PokemonTypeEnum
from enum import IntEnum

class MoveCategoryEnum(IntEnum):
    PHYSICAL = 0
    SPECIAL = 1
    STATUS = 2
    
@dataclass(frozen=True)
class MoveCost:
    cost: dict[PokemonTypeEnum, int]
    
class MoveTargetingEnum(IntEnum):
    SELF = 0
    OPPONENT = 1
    ALLY = 2
    ALL_POKEMON = 3
    TILE = 4

@dataclass(frozen=True)
class MoveDefintion:
    move_id: int = 0
    name: str = ""
    description: str = ""
    
    move_type: PokemonTypeEnum = PokemonTypeEnum.NORMAL
    category: MoveCategoryEnum = MoveCategoryEnum.PHYSICAL
    
    power: int = 0
    accuracy: float = 1.0
    
    cost: MoveCost = field(default_factory=lambda: MoveCost(cost={}))
    targeting: MoveTargetingEnum = MoveTargetingEnum.OPPONENT
    
    effects: tuple = field(default_factory=tuple)