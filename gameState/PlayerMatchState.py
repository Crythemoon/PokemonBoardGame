from enum import Enum

class PlayerMatchState(Enum):
    IDLE = 0
    QUEUED = 1
    MATCH_FOUND = 2
    IN_GAME = 3