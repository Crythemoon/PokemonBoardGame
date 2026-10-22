from dataclasses import dataclass, field
from enum import Enum
from server.Move.MoveDefinintion import MoveDefintion

class PokemonStateEnum(Enum):
    IDLE = 0
    ACTIVE = 1
    DEAD = 2

@dataclass
class PokemonState:
    player_id: int = 0
    pokemon_id: int = 0
    name: str = ""
    
    primary_type: str = ""
    secondary_type: str = "" | None
    
    state: PokemonStateEnum = PokemonStateEnum.IDLE
    
    base_hp: int = 0
    base_attack: int = 0
    base_defense: int = 0
    base_sp_attack: int = 0
    base_sp_defense: int = 0
    base_speed: int = 0
    
    available_moves: tuple[MoveDefintion] = field(default_factory=tuple)
    