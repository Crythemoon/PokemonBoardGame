from dataclasses import dataclass

@dataclass
class MatchConfig:
    match_id: str
    player1_id: int
    player2_id: int
    