class GameTimeError(Exception):
    pass

class InvalidCardError(Exception):
    pass

class InvalidTargetError(Exception):
    pass

class MatchIDInvalidError(Exception):
    pass

class MatchCreationFailure(Exception):
    pass

class PlayerDataInvalid(Exception):
    def __init__(self, player_id:int, missing_fields:tuple):
        self.player_id = player_id
        self.mising_fields = missing_fields
        super().__init__(
            f"Player {player_id} is missing: {', '.join(missing_fields)}"
        )