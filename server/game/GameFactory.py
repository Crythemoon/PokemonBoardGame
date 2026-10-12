from game import Game
from config import PlayerConfig, MatchConfig

class GameFactory:
    def __init__(self, player_configs: PlayerConfig, match_configs: MatchConfig):
        #initialize the game with the provided player and match configurations
        self.game = Game(player_configs, match_configs)
        
        #populate match data
        self.game.populate_match_data()
        
        #populate player's data
        self.game.populate_player_data()