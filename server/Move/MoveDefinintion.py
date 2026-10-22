from dataclasses import dataclass, field
from Pokemon.PokemonObject import PokemonTypeEnum as PokemonTypeEnum
from enum import IntEnum, Enum


class MoveCategoryEnum(IntEnum):
    PHYSICAL = 0
    SPECIAL = 1
    STATUS = 2


# Enum for all move effect
class MoveEffectTypeEnum(str, Enum):
    NONE = "none"

    # Status conditions
    BURN = "burn"
    POISON = "poison"
    BADLY_POISON = "badly_poison"
    PARALYSIS = "paralysis"
    SLEEP = "sleep"
    FREEZE = "freeze"
    CONFUSION = "confusion"

    # Stat modifications
    ATTACK_UP = "attack_up"
    ATTACK_DOWN = "attack_down"
    DEFENSE_UP = "defense_up"
    DEFENSE_DOWN = "defense_down"
    SP_ATTACK_UP = "sp_attack_up"
    SP_ATTACK_DOWN = "sp_attack_down"
    SP_DEFENSE_UP = "sp_defense_up"
    SP_DEFENSE_DOWN = "sp_defense_down"
    SPEED_UP = "speed_up"
    SPEED_DOWN = "speed_down"
    ACCURACY_UP = "accuracy_up"
    ACCURACY_DOWN = "accuracy_down"
    EVASION_UP = "evasion_up"
    EVASION_DOWN = "evasion_down"

    # Health effects
    HEAL = "heal"
    REGENERATION = "regeneration"
    DRAIN = "drain"
    RECOIL = "recoil"

    # Damage modifiers
    DAMAGE_BOOST = "damage_boost"
    DAMAGE_REDUCTION = "damage_reduction"
    SHIELD = "shield"
    VULNERABLE = "vulnerable"

    # Action restrictions
    STUN = "stun"
    SILENCE = "silence"
    ROOT = "root"
    TAUNT = "taunt"
    DISABLE = "disable"

    # Position and battlefield effects
    KNOCKBACK = "knockback"
    PULL = "pull"
    TELEPORT = "teleport"
    TRAP = "trap"

    # Special effects
    LEECH_SEED = "leech_seed"
    CURSE = "curse"
    PROTECT = "protect"
    REFLECT = "reflect"
    CLEANSE = "cleanse"
    IMMUNITY = "immunity"

# Enum for all move effect category
class MoveEffectCategory(str, Enum):
    NONE = "none"
    STATUS = "status"
    STAT_MODIFIER = "stat_modifier"
    HEALTH = "health"
    DAMAGE_MODIFIER = "damage_modifier"
    ACTION_RESTRICTION = "action_restriction"
    POSITION = "position"
    BATTLEFIELD = "battlefield"
    SPECIAL = "special"

# Enum for all valid type of target
class MoveTargetingEnum(IntEnum):
    SELF = 0
    OPPONENT = 1
    ALLY = 2
    ALL_POKEMON = 3
    TILE = 4

@dataclass(frozen=True)
class MoveCost:
    cost: dict[PokemonTypeEnum, int] = field(default_factory=dict)

@dataclass
class MoveEffect:
    effect_id: int = 0
    name: str = ""
    description: str = ""

    effect_type: MoveEffectCategory = MoveEffectCategory.NONE

    chance: float = 0.0
    duration: int = 0

    parameter: dict = field(default_factory=dict)

@dataclass(frozen=True)
class MoveDefinition:
    move_id: int = 0
    name: str = ""
    description: str = ""
    
    move_type: PokemonTypeEnum = PokemonTypeEnum.NORMAL
    category: MoveCategoryEnum = MoveCategoryEnum.PHYSICAL
    
    power: int = 0 #base damage, 0 for non damaging moves
    accuracy: float = 1.0
    
    cost: MoveCost = field(default_factory=lambda: MoveCost(cost={})) #type,cost
    targeting: MoveTargetingEnum = MoveTargetingEnum.OPPONENT
    
    effects: tuple[MoveEffect] = field(default_factory=tuple())