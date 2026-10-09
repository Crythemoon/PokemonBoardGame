from dataclasses import dataclass, field
from server.config import PlayerConfig
from PokemonState import PokemonState
from CardState import CardState

@dataclass
class PlayerState:
    player_id: int
    pokemon: list[PokemonState] = field(default_factory=list)
    hand: list[CardState] = field(default_factory=list)
    deck: list[CardState] = field(default_factory=list)
    discard_pile: list[CardState] = field(default_factory=list)
    turn: bool = False
    