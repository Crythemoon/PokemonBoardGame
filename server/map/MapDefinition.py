from dataclasses import dataclass, field
from MapTileObject import Tile

@dataclass()
class MapDefinition:
   width: int = 0
   height: int = 0
   tile: list[Tile] = field(default_factory=list)