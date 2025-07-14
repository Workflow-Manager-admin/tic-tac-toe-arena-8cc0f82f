"""
Simple in-memory user logic placeholder. NOT for production!
"""

from typing import Optional, Dict
from src.models.user import UserRegisterRequest, UserProfile

_USERS_DB: Dict[str, dict] = {}

# PUBLIC_INTERFACE
def register_user(data: UserRegisterRequest) -> Optional[UserProfile]:
    """Register user in memory. Returns profile on success, None if user already exists."""
    if data.username in _USERS_DB:
        return None
    new_id = f"user_{len(_USERS_DB)+1}"
    _USERS_DB[data.username] = {
        "user_id": new_id,
        "username": data.username,
        "password": data.password, # WARNING: Not hashed!
    }
    return UserProfile(user_id=new_id, username=data.username)

# PUBLIC_INTERFACE
def authenticate_user(username: str, password: str) -> Optional[UserProfile]:
    """Authenticate user. Returns profile if valid, else None."""
    rec = _USERS_DB.get(username)
    if not rec or rec["password"] != password:
        return None
    return UserProfile(user_id=rec["user_id"], username=username)
