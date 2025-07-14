"""
Game-related endpoints: create, move, state, history, and scores.
"""

from fastapi import APIRouter, HTTPException
from src.models.game import (
    CreateGameRequest,
    GameStateResponse,
    GameHistoryItem,
    ScoreEntry,
)
from src.core.game_service import create_game, get_game

router = APIRouter(tags=["Game"])

# PUBLIC_INTERFACE
@router.post("/game", response_model=GameStateResponse, summary="Create a new game")
def create_game_route(payload: CreateGameRequest):
    """
    Create a new Tic Tac Toe game. Opponent matching is simplified.
    """
    # Placeholder: Use player_x and player_o as static users
    player_x = "alice"
    player_o = payload.opponent_username or "bob"
    game = create_game(player_x, player_o)
    return game

# PUBLIC_INTERFACE
@router.get("/game/{game_id}", response_model=GameStateResponse, summary="Get game state")
def get_game_route(game_id: str):
    """
    Get the state of the game with provided ID.
    """
    game = get_game(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game

# Placeholder for other endpoints

# PUBLIC_INTERFACE
@router.get("/scores", response_model=list[ScoreEntry], summary="Get leaderboard scores")
def get_scores():
    """
    Retrieve global leaderboard scores (not implemented).
    """
    return []

# PUBLIC_INTERFACE
@router.get("/history/{username}", response_model=list[GameHistoryItem], summary="Get player's game history")
def get_history(username: str):
    """
    Retrieve played game history for the specified user (not implemented).
    """
    return []
