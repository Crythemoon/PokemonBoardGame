import game
import gameState.PlayerState
import Exception.Exception

class ValidationSystem:
    def validatePlayerTurn(playerID):
        if not gameState.PlayerState.getPlayerTurn(playerID):
            raise Exception.Exception.GameTimeError("It's not the player's turn.")

    def validatePlayerCard(playerID, cardID):
        hand = gameState.PlayerState.getPlayerHand(playerID)
        for card in hand:
            if card == cardID:
                return True
        raise Exception.Exception.InvalidCardError("The specified card is not in the player's hand.")

    def validateCardRestriction(cardID, target):
        restriction = game.Card.card.CardDefenition.getCardRestriction(cardID)
        pokemonStatus = gameState.PokemonState.getPokemonStatus(target.get("playerID"), target.get("pokemonID"))

        # Check if the target is valid based on the card's restriction
        if restriction.get("owner") == "owner":
            if target.get("playerID") != playerID:
                raise Exception.Exception.InvalidTargetError("The card can only be used on your Pokemon.")
        elif restriction.get("owner") != "owner":
            if target.get("playerID") == playerID:
                raise Exception.Exception.InvalidTargetError("The card can only be used on the opponent's Pokemon.")
        
        # Check if pokemon is alive
        if pokemonStatus.get("status") != "alive":
            raise Exception.Exception.InvalidTargetError("The target Pokemon is not alive.")

        # Check if target is full health for heal items
        if restriction.get("health") is not None:
            if pokemonStatus.get("currentHealth") == pokemonStatus.get("maxHealth"):
                raise Exception.Exception.InvalidTargetError("The target Pokemon is already at full health.")

        #