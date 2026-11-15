from server.config.PlayerConfig import PlayerConfig
from server.config.MatchConfig import MatchConfig

class ValidationSystem:
    
    """
        Validate if the player's config is valid

        Args:
        - player_configs: the PlayerConfig class
        
        Exception:
        - PlayerConfigValidationError()
    """
    def validate_player_config(player_config:PlayerConfig):
        pass
    
    
    """
        validate if the match's config is valid and not null
        
        Args:
        - match_configs: the MatchConfig class
        
        Exception:
        - MatchConfigValidationError()
    """
    def validate_match_config(match_config:MatchConfig):
        pass