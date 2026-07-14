import time
import asyncio
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession
from src.config import config
from src.database.models import User
from src.services.game import calculate_cock_growth
from src.utils.texts import cock_msg, wait_msg

router = Router(name="game")

@router.message(Command("кок", "cock"))
async def cock_cmd(message: Message, user: User, session: AsyncSession):
    msg_parts = message.text.split()
    
    # If the user typed an alias, let the leaderboards router handle it
    if len(msg_parts) == 2:
        alias = msg_parts[1].lower()
        if (alias in config.cock_top_aliases or 
            alias in config.cock_atop_aliases or 
            alias in config.cock_lngst_aliases or 
            alias in config.cock_ttop_aliases):
            return
            
    from datetime import datetime, timedelta
    
    current_time = int(time.time())
    
    # Check cooldown (resets at midnight)
    last_roll_date = datetime.fromtimestamp(user.last_cock).date() if user.last_cock else None
    now = datetime.fromtimestamp(current_time)
    
    if last_roll_date == now.date():
        next_midnight = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        remaining_time = int((next_midnight - now).total_seconds())
        wait_m = wait_msg(remaining_time)
        msg_we = await message.reply(wait_m)
        
        await asyncio.sleep(10)
        try:
            await message.delete()
            await msg_we.delete()
        except Exception:
            pass
        return

    # Send initial rolling message
    roll_msg = await message.reply("🎲 Крутим кок...")

    # Calculate growth
    action, event_text = calculate_cock_growth(user)
    
    if isinstance(action, int):
        user.cock_length += action
        symbol = "+" if action >= 0 else "-"
        final_msg = cock_msg(symbol, abs(action), user.cock_length)
    else:
        if action == "x2":
            user.cock_length *= 2
            final_msg = cock_msg("x2", 0, user.cock_length)
        else: # otval
            final_msg = cock_msg("otval", user.cock_length)
            if user.old_cock < user.cock_length:
                user.old_cock = user.cock_length
            user.cock_length = 0
            
    user.last_cock = current_time
    await session.commit()
    
    # Animate roll in background
    async def animate_roll(msg, final_text, event_description):
        import random
        # Animation loop
        for _ in range(3):
            r_val = random.randint(-20, 20)
            sign = "+" if r_val >= 0 else ""
            try:
                await msg.edit_text(f"🎲 Крутим кок...\n\n<i>Ммм, может {sign}{r_val}?</i>")
            except Exception:
                pass
            await asyncio.sleep(0.7)
        
        # final text
        text = f"<b>{event_description}</b>\n\n{final_text}"
        try:
            await msg.edit_text(text)
        except Exception:
            pass
            
    asyncio.create_task(animate_roll(roll_msg, final_msg, event_text))

@router.message(Command("reset"))
async def reset_cmd(message: Message, session: AsyncSession):
    if message.from_user.id not in config.admin_ids:
        return
        
    msg_parts = message.text.split()
    if len(msg_parts) >= 2:
        target_tgid = msg_parts[1]
        
        from sqlalchemy import select
        result = await session.execute(select(User).where(User.tgid == target_tgid))
        target_user = result.scalar_one_or_none()
        
        if target_user:
            if len(msg_parts) == 3 and msg_parts[2] == "full":
                target_user.cock_length = 0
                target_user.last_cock = 0
                target_user.old_cock = 0
            else:
                target_user.cock_length = 0
                target_user.old_cock = 0
                
            await session.commit()
            await message.reply(f"User {target_tgid} reset.")
        else:
            await message.reply("User not found.")
