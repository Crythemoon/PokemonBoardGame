from server.gameState import PlayerState,BoardState, PokemonState,gameState
import server.validation.validationSystem as validationSystem
import Card.CardDefenition as Card
import server.map.MapFactory as MapFactory
from config import MatchConfig, PlayerConfig
from server.database import Database as db
import json

class Game:
    def __init__(self, player_configs: PlayerConfig, match_configs: MatchConfig):
        
        self.player_configs = player_configs
        self.match_configs = match_configs

        # initialize game state
        self.game_state = gameState()
        
        
    """
    Populate the match data
        Populate match_id
        Generate map and updating map definition in GameState.BoardState
    """
    def load_match_data(self):
        
        # Populate match_id
        self.game_state.match_id = self.match_configs.match_id
        
        # Generate map and update map definition in BoardState
        map_definition = MapFactory.generate_map(self.match_configs.game_type)
        self.game_state.board_state.map_definition = map_definition
    
    """
    Populate each player's data with:
    - player_id
    - PokemonState
    - CardState
    """
    def load_player_data(self):
        
        # update player_id
        self.game_state.player1_state.player_id = self.player_configs[0].player1_id
        self.game_state.player2_state.player_id = self.player_configs[1].player2_id
        
        # load player's pokemon team
        

    """
    Load each player's pokemon team from the database
    
    Args:
    - player_id: the ID of the player
    """
    def load_player_pokemon_team(self, player_id: int):
        # Fetch the active Pokemon team for the given player_id from the database
        player_pokemon_team = db.get_player_active_pokemon_team(player_id)
        
        # Create PokemonState instances for each Pokemon in the team and add them to the player's state
        for pokemon_id in player_pokemon_team:
            pokemon_json_data = db.get_pokemon_data(player_id, pokemon_id)  # Fetch Pokemon data from the database
            pokemon_data = json.loads(pokemon_json_data)  # Convert JSON string to Python dictionary
            
            # Create PokemonState instance and populate it with the fetched data
            pokemon_state = PokemonState(
                player_id = player_id,
                pokemon_id = pokemon_data["pokemon_id"],
                name = pokemon_data["name"],
                primary_type = pokemon_data["primary_type"],
                secondary_type = pokemon_data["secondary_type"] if "secondary_type" in pokemon_data else None,
                base_hp = pokemon_data["stats"]["hp"],
                base_attack = pokemon_data["stats"]["attack"],
                base_defense = pokemon_data["stats"]["defense"],
                base_sp_attack = pokemon_data["stats"]["sp_attack"],
                base_sp_defense = pokemon_data["stats"]["sp_defense"],
                base_speed = pokemon_data["stats"]["speed"],
            )

            #Create MoveDefinition instances for each move in the Pokemon's data
            player_pokemon_moves_json = db.get_pokemon_moves(player_id, pokemon_id)
            player_pokemon_moves = json.loads(player_pokemon_moves_json)
    """
    Setup phase for the game, placing pokemon, shuffling and dealing card,
    and deciding who goes first
    
    Args:
    """
    def setup(self):
        # Placing pokemon on the board
        # Shuffling the decks and drawing initial hands
        # Figuring out who goes first
        pass
    
    def use_card(self, playerID: int, cardID: int, target: CardDefenition.TargetRef):
        
        # Validate the player's turn and card
        validationSystem.validatePlayerTurn(playerID)
        validationSystem.validatePlayerCard(playerID, cardID)
        
        # Validate the card's restrictions against the target
        