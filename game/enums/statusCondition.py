from enum import Enum, auto

class StatusCondition(Enum):
    POISONED = auto()
    BADLY_POISONED = auto()
    BURNED = auto()
    PARALYZED = auto()
    ASLEEP = auto()
    FROZEN = auto()
    CONFUSED = auto()

class StatType(Enum):
    ATTACK = auto()
    DEFENSE = auto()
    SPECIAL_ATTACK = auto()
    SPECIAL_DEFENSE = auto()
    SPEED = auto()
    ACCURACY = auto()
    EVASION = auto()
    MOVEMENT = auto()

class RestrictionType(Enum):
    CANNOT_MOVE = auto()
    CANNOT_ATTACK = auto()
    CANNOT_HEAL = auto()
    CANNOT_USE_CARDS = auto()
    CANNOT_BE_TARGETED = auto()