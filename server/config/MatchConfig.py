from dataclasses import dataclass

@dataclass
class MatchConfig:
    match_id: int
    player1_id: int
    player2_id: int
    