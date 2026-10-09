from dataclasses import dataclass, field
from map.MapDefinition import MapDefinition as MapDefinition
from map.MapTileObject import Position as Position

@dataclass
class BoardState:
    map_definition: MapDefinition = field(default_factory=MapDefinition)
    player1_occupants: dict[Position, int] = field(default_factory=dict)
    player2_occupants: dict[Position, int] = field(default_factory=dict)