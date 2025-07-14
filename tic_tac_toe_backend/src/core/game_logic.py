"""
Core game logic for Tic Tac Toe.
Handles board manipulation and win checking.
"""

from typing import List, Optional, Literal

PlayerMark = Literal["X", "O"]

# PUBLIC_INTERFACE
def check_winner(board: List[Optional[PlayerMark]]) -> Optional[PlayerMark]:
    """Check if there's a winner. Returns 'X', 'O', or None."""
    combos = [
        (0,1,2), (3,4,5), (6,7,8), # rows
        (0,3,6), (1,4,7), (2,5,8), # cols
        (0,4,8), (2,4,6)           # diags
    ]
    for a, b, c in combos:
        if board[a] is not None and board[a] == board[b] == board[c]:
            return board[a]
    return None

# PUBLIC_INTERFACE
def is_board_full(board: List[Optional[PlayerMark]]) -> bool:
    """Returns True if the board is full."""
    return all(cell is not None for cell in board)

# PUBLIC_INTERFACE
def initial_board() -> List[Optional[PlayerMark]]:
    """Returns a blank board."""
    return [None] * 9
