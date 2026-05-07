from enum import IntEnum

class Terrain(IntEnum):
    WATER = 0
    DIRT = 1
    BASE_MOUNTAIN = 2
    MIDDLE_MOUTAIN = 3
    TOP_MOUNTAIN = 4

class Tile:
    __slots__ = ("terrain")
    def __init__(self,terrain: Terrain):
        self.terrain = terrain