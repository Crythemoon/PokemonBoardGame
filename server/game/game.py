from server.gameState import PlayerState,PokemonState,gameState
import server.map.MapFactory as MapFactory
from config import MatchConfig, PlayerConfig
from server.database.Database import Database as db
from server.Move.MoveDefinintion import MoveDefinition, MoveCategoryEnum, MoveCost, MoveTargetingEnum, MoveEffect, MoveEffectCategory
from server.Pokemon.PokemonObject import PokemonTypeEnum
import json

class Game:
    def __init__(self, player_configs: tuple[PlayerConfig.PlayerConfig], match_configs: MatchConfig.MatchConfig):
        
        self.player_configs = player_configs
        self.match_configs = match_configs

        # initialize game state
        self.game_state = gameState.gameState()
        
        
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
        
        # get player_id from config
        player1_id = self.player_configs[0].player_id
        player2_id = self.player_configs[1].player_id
        
        # update player_id
        self.game_state.player1_state.player_id = player1_id
        self.game_state.player2_state.player_id = player2_id
        
        # load player's pokemon team
        player1_team_id = self.player_configs[0].team_id
        player2_team_id = self.player_configs[1].team_id
        self.load_player_pokemon_team(player1_id,player1_team_id,self.game_state.player1_state)
        self.load_player_pokemon_team(player2_id,player2_team_id,self.game_state.player2_state)

        # Load player's deck
        player1_deck_id = self.player_configs[0].deck_id
        player2_deck_id = self.player_configs[1].deck_id


    """
    Load each player's pokemon team from the database
    
    Args:
    - player_id (int): the ID of the player
    - player_state (PlayerState): the PlayerState class of a player saved in GameState
    - team_id (int): the ID of the active team the player chose
    """
    def load_player_pokemon_team(self, player_id: int,team_id: int,player_state : PlayerState.PlayerState):
        # Fetch the active Pokemon team for the given player_id from the database
        player_pokemon_team = json.loads(db.get_player_pokemon_team(player_id,team_id))
        
        # Create PokemonState instances for each Pokemon in the team and add them to the player's state
        for pokemon_id in player_pokemon_team:
            # Fetch Pokemon data from the database
            pokemon_data = json.loads(db.get_pokemon_data(player_id, pokemon_id))  # Convert JSON string to Python dictionary
            
            # Create PokemonState instance and populate it with the fetched data
            pokemon_state = PokemonState.PokemonState(
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
            player_pokemon_moves = json.loads(db.get_pokemon_moves(player_id,pokemon_data["pokemon_id"]))
            
            
            # get move's data, create MoveDefinition and add it to PokemonState
            for move_id in player_pokemon_moves.values():
                # get player move data from db
                player_move_data = json.loads(db.get_move_data(move_id))
                # create move_definition
                move_definition = MoveDefinition(
                    move_id = player_move_data["move_id"],
                    name = player_move_data["name"],
                    description = player_move_data["description"],

                    move_type = PokemonTypeEnum(player_move_data["move_type"]),
                    category = MoveCategoryEnum(player_move_data["category"]),

                    power = player_move_data["power"],
                    accuracy = player_move_data["accuracy"],

                    cost = MoveCost(dict[PokemonTypeEnum(player_move_data["move_type"]), player_move_data["cost"]]),
                    targeting = MoveTargetingEnum(player_move_data["target"])
                )
                # get move effect from db
                move_effect_ids = json.loads(db.get_move_effect_id(move_id))
                for move_effect_id in move_effect_ids:
                    move_effect_data = json.loads(db.get_move_effect_data(move_effect_id))
                    # create move effect
                    move_effect = MoveEffect(
                        effect_id = move_effect_data["effect_id"],
                        name = move_effect_data["name"],
                        description = move_effect_data["description"],

                        effect_type = MoveEffectCategory(move_effect_data["category"]),

                        chance = move_effect_data["chance"],
                        duration = move_effect_data["duration"],

                        parameter = move_effect_data["parameter"]
                    )
                    # add to move definition effect
                    move_definition.effects += (move_effect,)

                # add moves to available moves in PokemonState
                pokemon_state.available_moves += (move_definition,)

            # add pokemon to team
            player_state.pokemon += (pokemon_state,)

    """
    Getting the card from a player active deck from the database, then creating a
    CardDefinition for each card and placing it into a PlayerState deck in GameState

    Args:
    - player_id (int): the id of the player
    - deck_id (int): the id of the selected deck from player
    - player_state (PlayerState): the PlayerState of the corresponding player
      saved in GameState
    """
    def load_player_deck(player_id: int,deck_id: int,player_state: PlayerState.PlayerState):
        # Get cardID from the active Deck in the database
        cards = json.loads(db.get_deck_card(player_id,deck_id))

        for card in cards["cards"]:
            # Get card definition from the database from each card

        # Create CardDefinition using the data
        # Adding the card to the deck in PlayerState
        
            pass
    
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
    
    def use_card(self):
        # Validate the player's turn and card
        
        # Validate the card's restrictions against the target
        pass