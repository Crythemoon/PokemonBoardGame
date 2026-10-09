
from dataclasses import dataclass
import enum

class GamePhase(enum.Enum):
    INITIALIZING = 0
    PLAYING = 1
    ENDED = 2

@dataclass
class gameState:
    match_id: int = 0
    phase: GamePhase = GamePhase.INITIALIZING