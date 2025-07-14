"""
User registration and authentication endpoints.
"""

from fastapi import APIRouter, HTTPException, status
from src.models.user import UserRegisterRequest, UserLoginRequest, UserProfile, TokenResponse
from src.core.user_service import register_user, authenticate_user

router = APIRouter(tags=["User"])

# PUBLIC_INTERFACE
@router.post("/register", response_model=UserProfile, summary="Register a new user")
def register(payload: UserRegisterRequest):
    """
    Register a new Tic Tac Toe user.
    """
    res = register_user(payload)
    if not res:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Username already exists"
        )
    return res

# PUBLIC_INTERFACE
@router.post("/login", response_model=TokenResponse, summary="Authenticate a user and return bearer token")
def login(payload: UserLoginRequest):
    """
    Authenticate and return a JWT-like token (placeholder).
    """
    profile = authenticate_user(payload.username, payload.password)
    if not profile:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    # Placeholder token for demonstration purposes only!
    token = f"fake-token-for-{profile.username}"
    return TokenResponse(access_token=token)
