import validationSystem

class Game:
    def use_card(self, playerID, cardID, target):
        validationSystem.validatePlayerTurn(playerID)
        validationSystem.validatePlayerCard(playerID, cardID)
        