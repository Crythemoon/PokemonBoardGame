import json
from uuid import uuid4
from server.Exception.Exception import MatchIDInvalidError, PlayerDataInvalid
from game import Game
from server.config.PlayerConfig import PlayerConfig as player_con
from config import PlayerConfig, MatchConfig
from server.database.Database import Database as db

class GameFactory:
    def __init__(self, player1_id, player2_id):
        # Create player's config
        player_configs = self.create_player_configs(
            player1_id=player1_id,
            player2_id=player2_id
        )
        
        # Create match's config
            
        
        #initialize the game with the provided player and match configurations
        self.game = Game(player_configs, match_configs)
        
        #populate match data
        self.game.populate_match_data()
        
        #populate player's data
        self.game.populate_player_data()
        
    def create_player_configs(self,player1_id:int,player2_id:int,max_attempts=3):
        for attempt in max_attempts:
            try:            
                # Get player's name, team and deck from database
                player1_config_data = json.loads(db.get_player_config_data(player1_id))
                player2_config_data = json.loads(db.get_player_config_data(player2_id))
            except PlayerDataInvalid:
                continue
            else:
                # Create player's config for each player
                player1_config = player_con(
                    player_id=player1_config["player_id"],
                    name=player1_config["name"],
                    team_id=player1_config["team_id"],
                    deck_id=player1_config["deck_id"]
                )
                player2_config = player_con(
                    player_id=player2_config["player_id"],
                    name=player2_config["name"],
                    team_id=player2_config["team_id"],
                    deck_id=player2_config["deck_id"]
                )
                
                return (player1_config,player2_config)
        raise RuntimeError("Player's data is missing")
    
    def create_match_config(self):
        # Create match_id
        try:
            match_id = self.create_match_id()
        except RuntimeError:
            pass
            
    def create_match_id(max_attempts=10):
        for attempt in max_attempts:
            match_id = uuid4()
        
            try:
                db.put_match_id(match_id)
            except MatchIDInvalidError:
                continue
            else:
                return match_id
        raise RuntimeError("Could not create match's ID")
        