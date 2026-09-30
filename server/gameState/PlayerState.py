class PlayerState:
    def __init__(self, player: list[1]):
        self.playerID = player.get("playerID")
        self.turn = False
        self.hand = []
        self.deck = player.get("deck")
        self.discard_pile = []
        self.active_pokemon = []
        self.dead_pokemon = []

    def getPlayerTurn(self, playerID: int)-> bool:
        """
        Get the boolean for whether it is the player's turn

        Args:
            playerID (int): The ID of the player

        Returns:
            bool: True if it is the player's turn, False otherwise
        
        Raises:
            Exception: If the playerID is invalid or not found
        """
        pass


    def getPlayerHand(self, playerID: int)-> list:
        """
        Get the player's hand

        Args:
            playerID (int): The ID of the player

        Returns:
            List[Card]: The list of cards the player has in hand

        Raises:
            Exception: If the playerID is invalid or not found
        """
        pass