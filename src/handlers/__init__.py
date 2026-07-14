from aiogram import Router
from .basic import router as basic_router
from .game import router as game_router
from .leaderboards import router as leaderboards_router

def get_routers() -> tuple[Router, ...]:
    return (
        basic_router,
        leaderboards_router,
        game_router,
    )
