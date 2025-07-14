from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes_user import router as user_router
from src.api.routes_game import router as game_router

app = FastAPI(
    title="Tic Tac Toe Arena API",
    description="Backend API for multiplayer Tic Tac Toe, managing users, games, scores.",
    version="0.1.0",
    openapi_tags=[
        {"name": "User", "description": "User registration and authentication"},
        {"name": "Game", "description": "Gameplay actions and state"},
    ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(game_router)

@app.get("/", tags=["Misc"])
def health_check():
    """
    Health check endpoint.
    """
    return {"message": "Healthy"}
