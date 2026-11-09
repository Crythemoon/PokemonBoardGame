from dataclasses import dataclass, field
from enum import Enum

class EffectCategoryEnum(Enum):
    HEALTH = "HEALTH"
    STATUS = "STATUS"
    STAT_MODIFIER = "STAT_MODIFIER"
    DAMAGE_MODIFIER = "DAMAGE_MODIFIER"
    ACTION_RESTRICTION = "ACTION_RESTRICTION"
    POSITION = "POSITION"
    BATTLEFIELD = "BATTLEFIELD"
    CARD_MANIPULATION = "CARD_MANIPULATION"
    ENERGY_MANIPULATION = "ENERGY_MANIPULATION"
    SPECIAL = "SPECIAL"

@dataclass(frozen=True)
class EffectDefinition:
    effect_id: int = 0
    name: str = ""
    category: EffectCategoryEnum = EffectCategoryEnum.HEALTH
    description: str = ""
    duration: int = 0 # Duration 0 for permanent effects
    parameter: dict[str, any] = field(default_factory=dict) # Additional parameters for the effect, can be empty