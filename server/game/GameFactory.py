import json
from uuid import uuid4
from server.Exception.Exception import (
    MatchIDInvalidError, 
    PlayerDataInvalid, 
    MatchCreationFailure, 
    GameObjectCreationFailed, 
    PlayerConfigValidationError,
    MatchConfigValidationError
)
from game import Game
from server.config.PlayerConfig import PlayerConfig as player_con
from server.config.MatchConfig import MatchConfig as match_con
from server.database.Database import Database as db
from server.validation.validationSystem import ValidationSystem

class GameFactory:
    def __init__(self, player1_id, player2_id):
        self.player1_id = player1_id
        self.player2_id = player2_id
        
    def create_game(self):
        # Create player's config
        try:
            player_configs = self.create_player_configs(
                player1_id=self.player1_id,
                player2_id=self.player2_id
            )
            # Validate player's configs
            for config in player_configs:
                ValidationSystem.validate_player_config(config)
        except RuntimeError & PlayerConfigValidationError:
            raise MatchCreationFailure("Loading player's data failed")
        
        # Create match's config
        try:
            match_config = self.create_match_config()
            
            # Validate match's config
            ValidationSystem.validate_match_config(match_config)
            
        except RuntimeError & MatchConfigValidationError:
            raise MatchCreationFailure("Creating match's id failed")
        
        try:
            #initialize the game with the provided player and match configurations
            self.game = Game(player_configs, match_config)
        except:
            raise GameObjectCreationFailed("Initializing game object failed")
        
        #populate match data
        self.game.populate_match_data()
        
        #populate player's data
        self.game.populate_player_data()
        return self.game
        
    def create_player_configs(self,player1_id:int,player2_id:int,max_attempts=3):
        player_id_invalid:int
        missing_fields:tuple
        for attempt in max_attempts: 
            try:
                # Get player's name, team and deck from database
                player1_config_data = json.loads(db.get_player_config_data(player1_id))
                player2_config_data = json.loads(db.get_player_config_data(player2_id))
            except PlayerDataInvalid as error:
                player_id_invalid = error.player_id
                missing_fields = error.mising_fields
                continue
            else:
                # Create player's config for each player
                player1_config = player_con(
                    player_id=player1_config_data["player_id"],
                    name=player1_config_data["name"],
                    team_id=player1_config_data["team_id"],
                    deck_id=player1_config_data["deck_id"]
                )
                player2_config = player_con(
                    player_id=player2_config_data["player_id"],
                    name=player2_config_data["name"],
                    team_id=player2_config_data["team_id"],
                    deck_id=player2_config_data["deck_id"]
                )
                return (player1_config,player2_config)
            
        raise RuntimeError(f'Player {player_id_invalid} is missing {', '.join(missing_fields)}')
    
    def create_match_config(self):
        # Create match_id
        try:
            match_id = self.create_match_id()
        except RuntimeError:
            raise RuntimeError("Cannot create match's config")
        else:
            return match_con(
                match_id=match_id,
                player1_id=self.player1_id,
                player2_id=self.player2_id
            )
            
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
        