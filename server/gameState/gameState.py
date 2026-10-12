from dataclasses import dataclass
import enum
from PlayerState import PlayerState as PlayerState
from BoardState import BoardState as BoardState

class GamePhase(enum.Enum):
    INITIALIZING = 0
    PLAYING = 1
    ENDED = 2

@dataclass
class gameState:
    match_id: int = 0
    phase: GamePhase = GamePhase.INITIALIZING
    player1_state: PlayerState = PlayerState()
    player2_state: PlayerState = PlayerState()
    board_state: BoardState = BoardState()
    