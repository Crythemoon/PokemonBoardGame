from server.gameState import PlayerState,BoardState,gameState
import server.validation.validationSystem as validationSystem
import Card.CardDefenition as Card
import server.map.MapFactory as MapFactory
from config import MatchConfig, PlayerConfig

class Game:
    def __init__(self, player_configs: PlayerConfig, match_configs: MatchConfig):
        
        self.player_configs = player_configs
        self.match_configs = match_configs

        # initialize player states for each player
        self.player1_state = PlayerState()
        self.player2_state = PlayerState()
            
        # initialize board state
        self.board_state = BoardState()
        
        # initialize game state
        
        """
        Populate the match data
            Populate match_id
            Generate map and updating map definition in BoardState
        """
    def populate_match_data(self):
        
        # Populate match_id
        self.board_state.match_id = self.match_configs.match_id
        
        # Generate map and update map definition in BoardState
        map_definition = MapFactory.generate_map(self.match_configs)
        self.board_state.map_definition = map_definition
    
    
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
        