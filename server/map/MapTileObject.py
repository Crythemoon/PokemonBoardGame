from enum import IntEnum
from dataclasses import dataclass

class Terrain(IntEnum):
    WATER = 0
    DIRT = 1
    BASE_MOUNTAIN = 2
    MIDDLE_MOUTAIN = 3
    TOP_MOUNTAIN = 4
    
class Obstacle(IntEnum):
    TREE = 0
    ROCK = 1
    BUSH = 2
    
@dataclass(frozen=True)
class Position:
    x: int
    y: int

@dataclass
class Tile:
    __slots__ = ("terrain")
    terrain: Terrain
    obstacle: Obstacle | None = None
    position: Position