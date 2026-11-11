import pytest
from server.config.PlayerConfig import PlayerConfig

@pytest.fixture
def player_config():
    return PlayerConfig(
        player_id=0,
        name="John Doe",
        team_id=0,
        deck_id=0
    )

def test_player_config_data_storage(player_config):
    assert player_config.player_id == 0
    assert player_config.name == "John Doe"
    assert player_config.team_id == 0
    assert player_config.deck_id == 0