from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.config import config
from src.database.models import User
from src.services.formatting import format_top_message
from src.utils.texts import NOT_FOUND
import time

router = Router(name="leaderboards")

async def send_top(message: Message, session: AsyncSession, stts: str):
    query = select(User)
    
    if stts == "top":
        query = query.order_by(User.cock_length.desc())
    elif stts == "atop":
        query = query.order_by(User.cock_length.asc())
    elif stts == "lngst":
        query = query.order_by(User.old_cock.desc())
    elif stts == "truet":
        # 604800 seconds = 1 week
        cutoff = int(time.time()) - 604800
        query = query.where(User.last_cock >= cutoff).order_by(User.cock_length.desc())
        
    query = query.limit(10)
    result = await session.execute(query)
    users = result.scalars().all()
    
    msg = format_top_message(users, stts)
    await message.answer(msg, disable_web_page_preview=True)

# Handles alias from /cock command
@router.message(Command("кок", "cock"))
async def cock_alias_cmd(message: Message, session: AsyncSession):
    msg_parts = message.text.split()
    if len(msg_parts) == 2:
        alias = msg_parts[1].lower()
        if alias in config.cock_top_aliases:
            await send_top(message, session, "top")
        elif alias in config.cock_atop_aliases:
            await send_top(message, session, "atop")
        elif alias in config.cock_lngst_aliases:
            await send_top(message, session, "lngst")
        elif alias in config.cock_ttop_aliases:
            await send_top(message, session, "truet")
        else:
            await message.reply(NOT_FOUND)

@router.message(Command("кокт", "top", "cockt", "топ"))
async def top_cmd(message: Message, session: AsyncSession):
    await send_top(message, session, "top")
    
@router.message(Command("кокат", "atop", "cockat", "атоп"))
async def atop_cmd(message: Message, session: AsyncSession):
    await send_top(message, session, "atop")

@router.message(Command("коклт", "ltop", "cocklt", "лтоп"))
async def ltop_cmd(message: Message, session: AsyncSession):
    await send_top(message, session, "lngst")

@router.message(Command("коктт", "ttop", "cocktt", "ттоп"))
async def ttop_cmd(message: Message, session: AsyncSession):
    await send_top(message, session, "truet")
