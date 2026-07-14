import pytest
from unittest.mock import AsyncMock, MagicMock
from aiogram.types import Message
from aiogram.filters.command import CommandObject

from src.handlers.leaderboards import IsLeaderboardAlias
from src.config import config

@pytest.mark.asyncio
async def test_is_leaderboard_alias():
    filter_instance = IsLeaderboardAlias()
    
    # Test 1: No arguments
    msg = MagicMock(spec=Message)
    cmd_obj = CommandObject(prefix="/", command="cock", mention=None, args=None)
    result = await filter_instance(msg, cmd_obj)
    assert result is False
    
    # Test 2: Valid alias
    cmd_obj = CommandObject(prefix="/", command="cock", mention=None, args="top")
    result = await filter_instance(msg, cmd_obj)
    assert result == {"alias": "top"}
    
    # Test 3: Valid alias (another one)
    cmd_obj = CommandObject(prefix="/", command="cock", mention=None, args="lngst")
    result = await filter_instance(msg, cmd_obj)
    assert result == {"alias": "lngst"}
    
    # Test 4: Invalid alias (random text)
    cmd_obj = CommandObject(prefix="/", command="cock", mention=None, args="random_joke")
    result = await filter_instance(msg, cmd_obj)
    assert result is False
    
    # Test 5: Multiple arguments
    cmd_obj = CommandObject(prefix="/", command="cock", mention=None, args="top 123")
    result = await filter_instance(msg, cmd_obj)
    assert result is False

@pytest.mark.asyncio
async def test_router_order():
    from src.handlers import get_routers
    routers = get_routers()
    
    # Leaderboards must be before Game
    leaderboards_idx = next(i for i, r in enumerate(routers) if r.name == "leaderboards")
    game_idx = next(i for i, r in enumerate(routers) if r.name == "game")
    
    assert leaderboards_idx < game_idx, "Leaderboards router must be registered before Game router!"
