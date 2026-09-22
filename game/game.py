import validationSystem
import Card.CardDefenition as CardDefenition

class Game:
    def use_card(self, playerID: int, cardID: int, target: CardDefenition.TargetRef):
        
        # Validate the player's turn and card
        validationSystem.validatePlayerTurn(playerID)
        validationSystem.validatePlayerCard(playerID, cardID)
        
        # Validate the card's restrictions against the target
        card = 
        