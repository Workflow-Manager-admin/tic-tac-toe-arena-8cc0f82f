"""
User models for Tic Tac Toe backend.
"""

from pydantic import BaseModel, Field

# PUBLIC_INTERFACE
class UserRegisterRequest(BaseModel):
    """Request model for user registration."""
    username: str = Field(..., description="Desired username")
    password: str = Field(..., min_length=3, description="Desired password")

# PUBLIC_INTERFACE
class UserLoginRequest(BaseModel):
    """Request model for user login."""
    username: str = Field(..., description="Username")
    password: str = Field(..., description="Password")

# PUBLIC_INTERFACE
class UserProfile(BaseModel):
    """Represents the user's profile information."""
    user_id: str
    username: str

# PUBLIC_INTERFACE
class TokenResponse(BaseModel):
    """Response model for authentication tokens."""
    access_token: str
    token_type: str = "bearer"
