class Database:
    
    """
    Get the player active pokemon team
    
    Args:
    - player_id: the ID of the player
    
    Returns:
    - list of pokemon_id
    
    Exceptions:
    - Database connections error
    """
    def get_player_pokemon_team(player_id,team_id:int):
        
        # Fetch the Pokemon team for the given player_id from the database
        pass
    
    """
    Get the Pokemon data for a given pokemon_id
    
    Args:
    - pokemon_id: the ID of the Pokemon
    
    Returns:
    - json object containing the Pokemon data
    {
        "pokemon_id": int,
        "name": str,
        "description": str,
        "primary_type": int,
        "secondary_type": int | None
        "stats": {
            "hp": int,
            "attack": int,
            "defense": int,
            "sp_attack": int,
            "sp_defense": int,
            "speed": int
        }
    }
    """
    def get_pokemon_data(self, pokemon_id: int):
        # Fetch Pokemon data from the database
        pass
    
    
        """
        Get the moveID from the PokemonMove table by searching the
        PlayerPokemonID from the PlayerPokemon table using pokemonID
        and playerID
        
        Args:
        - player_id: the ID of the player
        - pokemon_id: the ID of teh pokemon
        
        Returns:
        - json object of the two moves:
        {
            "first_move": int,
            "second_move": int   
        }
        """
    def get_pokemon_moves(player_id, pokemon_id):
        # Fetch moveID from PokemonMove
        pass
    
        """
        Get all data related to MoveDefintion from MoveDefinition table
        by searching using moveID
        
        Args:
        - moveID: the ID of the move
        
        Returns:
        - json object of the moves:
        {
            "move_id": int,
            "name": str,
            "description": str,
            
            "move_type": str,
            "category": str,
            
            "power": int,
            "accuracy": int,
            
            "cost": int,
            
            "target": str,
            
        }
        """
    def get_move_data(move_id : int):
        # Fetch the move data from MoveDefinition
        pass

        """
        Get the chance and all data related to the effect that a move has

        Args:
        - moveID: the ID of the move

        Returns:
        - json object of the data:
        {
            "effect_id": int
            "name": str,
            "description": str,

            "category": str,

            "chance": float,
            "duration": int,

            "parameter": dict
        }
        """
    def get_move_effect_data(move_effect_id: int):
        # Fetch the chance and the effect data from MoveEffect and Effect table
        pass


        """
        Get all move_effect_id from the MoveEffectTable

        Args:
        - move_id: the ID of the move

        Returns:
        - json object of all move_id
        {
            "moveEffectID": [int]
        }
        """
    def get_move_effect_id(move_id: int):
        # Fetch all move_effect_id from the MoveEffect table
        pass

    """
    Get all cardID from the selected deck from the Deck table

    Args:
    - player_id: the ID of the player
    - deck_id: the ID of the selected deck

    Returns:
    - json object of all card_id:
    {
        "cards": [int]
    }
    """
    def get_deck_card(player_id: int,deck_id: int):
        # Fetch all cardID from the Deck table
        pass