
from dataclasses import dataclass
import enum

class GamePhase(enum.Enum):
    pass

@dataclass
class gameState:
    match_id: int
    phase: GamePhase