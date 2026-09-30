from server.gameState import PlayerState
import server.validation.validationSystem as validationSystem
import Card.CardDefenition as Card
import map.MapFactory as MapFactory

class Game:
    def __init__(self, player_configs, map_size):
        
        # initialize player states for each player
        player_states = {}
        for player in player_configs:
            player_states[player.get("playerID")] = PlayerState(player)
            
        # initialize board state
        board_state = MapFactory.create_map(map_size=map_size)
        
        # initialize game state
        
    
    
        """
        Setup phase for the game, placing pokemon, shuffling and dealing card,
        and deciding who goes first
        
        Args:
        """4
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
        