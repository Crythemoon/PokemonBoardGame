import pytest
from server.config.MatchConfig import MatchConfig

@pytest.fixture
def match_config():
    return MatchConfig(
        match_id=0,
        player1_id=0,
        player2_id=1
    )
    
def test_match_config_data_storage(match_config):
    assert match_config.match_id == 0
    assert match_config.player1_id == 0
    assert match_config.player2_id == 1