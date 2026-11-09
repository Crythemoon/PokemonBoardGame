"""Unit tests for Game's implemented data-loading methods.

Place this file in ``tests/test_game.py`` and run ``python -m pytest -v``
from the repository root. No live database is needed.
"""

import importlib
import json
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest


@pytest.fixture
def game_module():
    """Supports game.py at project root or server/game.py."""
    try:
        return importlib.import_module("server.game")
    except ModuleNotFoundError as exc:
        if exc.name not in ("server.game", "server"):
            raise
        return importlib.import_module("game")


@pytest.fixture
def player_state():
    return SimpleNamespace(player_id=None, pokemon=(), deck=[])


@pytest.fixture
def game(game_module):
    """Avoid initializing real game state; test each loader independently."""
    instance = game_module.Game.__new__(game_module.Game)
    instance.player_configs = (
        SimpleNamespace(player_id=1, team_id=11, deck_id=21),
        SimpleNamespace(player_id=2, team_id=12, deck_id=22),
    )
    instance.match_configs = SimpleNamespace(match_id=99, game_type="small")
    instance.game_state = SimpleNamespace(
        match_id=None,
        board_state=SimpleNamespace(map_definition=None),
        player1_state=SimpleNamespace(player_id=None, pokemon=(), deck=[]),
        player2_state=SimpleNamespace(player_id=None, pokemon=(), deck=[]),
    )
    return instance


def test_initialization_stores_configs_and_creates_state(game_module, monkeypatch):
    state = object()
    state_constructor = MagicMock(return_value=state)
    monkeypatch.setattr(game_module.gameState, "gameState", state_constructor)
    players = (object(), object())
    match = object()

    game = game_module.Game(players, match)

    assert game.player_configs is players
    assert game.match_configs is match
    assert game.game_state is state
    state_constructor.assert_called_once_with()


def test_load_match_data_sets_id_and_generated_map(game_module, game, monkeypatch):
    generated = object()
    generate = MagicMock(return_value=generated)
    monkeypatch.setattr(game_module.MapFactory, "generate_map", generate)

    game.load_match_data()

    assert game.game_state.match_id == 99
    assert game.game_state.board_state.map_definition is generated
    generate.assert_called_once_with("small")


def test_load_player_data_assigns_both_players_and_loads_teams(game, monkeypatch):
    load_team = MagicMock()
    monkeypatch.setattr(game, "load_player_pokemon_team", load_team)

    game.load_player_data()

    assert game.game_state.player1_state.player_id == 1
    assert game.game_state.player2_state.player_id == 2
    assert load_team.call_count == 2
    assert load_team.call_args_list[0].args == (1, 11, game.game_state.player1_state)
    assert load_team.call_args_list[1].args == (2, 12, game.game_state.player2_state)


def test_load_empty_pokemon_team(game_module, game, player_state, monkeypatch):
    get_team = MagicMock(return_value=json.dumps([]))
    get_pokemon = MagicMock()
    monkeypatch.setattr(game_module.db, "get_player_pokemon_team", get_team)
    monkeypatch.setattr(game_module.db, "get_pokemon_data", get_pokemon)

    game.load_player_pokemon_team(1, 11, player_state)

