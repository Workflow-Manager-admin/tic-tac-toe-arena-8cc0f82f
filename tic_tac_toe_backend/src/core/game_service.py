"""
Simple in-memory game logic for Tic Tac Toe backend. NOT persistent!
Includes placeholder storage for demonstration.
"""

from typing import Dict, Optional
from src.models.game import GameStateResponse
from src.core.game_logic import initial_board

_GAMES_DB: Dict[str, dict] = {}  # game_id to game data

# PUBLIC_INTERFACE
def create_game(player_x: str, player_o: str) -> GameStateResponse:
    """Create new game between two users."""
    game_id = f"game_{len(_GAMES_DB)+1}"
    board = initial_board()
    game_data = {
        "game_id": game_id,
        "board": board,
        "current_turn": player_x,
        "status": "in_progress",
        "winner": None,
        "player_x": player_x,
        "player_o": player_o
    }
    _GAMES_DB[game_id] = game_data
    return GameStateResponse(**game_data)

# PUBLIC_INTERFACE
def get_game(game_id: str) -> Optional[GameStateResponse]:
    """Get current game state."""
    rec = _GAMES_DB.get(game_id)
    if not rec:
        return None
    return GameStateResponse(**rec)
