"""
Game models for Tic Tac Toe backend.
"""

from pydantic import BaseModel, Field
from typing import List, Optional, Literal

# PUBLIC_INTERFACE
class CreateGameRequest(BaseModel):
    """Request to create a new game."""
    opponent_username: Optional[str] = Field(None, description="Username of the opponent to invite, or None for public/random match.")

# PUBLIC_INTERFACE
class GameMoveRequest(BaseModel):
    """Represents a move made by a player."""
    game_id: str
    position: int = Field(..., ge=0, le=8, description="Board position (0-8)")

# PUBLIC_INTERFACE
class GameStateResponse(BaseModel):
    """Current state of a Tic Tac Toe game."""
    game_id: str
    board: List[Optional[Literal["X", "O"]]] = Field(..., description="3x3 board as a flat list, 0-8, with 'X', 'O', or None")
    current_turn: str = Field(..., description="Username whose turn it is")
    status: Literal["waiting", "in_progress", "completed"] = Field(..., description="Game lifecycle status")
    winner: Optional[str] = Field(None, description="Winner username if game is over")
    player_x: str
    player_o: str

# PUBLIC_INTERFACE
class GameHistoryItem(BaseModel):
    """One game's summary for history listing."""
    game_id: str
    opponent: str
    result: Literal["win", "loss", "draw"]
    timestamp: str

# PUBLIC_INTERFACE
class ScoreEntry(BaseModel):
    """Player's score for leaderboard."""
    username: str
    wins: int
    losses: int
    draws: int
