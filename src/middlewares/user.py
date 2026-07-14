from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message
import time
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.models import User

class UserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        if not event.from_user:
            return await handler(event, data)
            
        session: AsyncSession = data["session"]
        
        result = await session.execute(select(User).where(User.tgid == str(event.from_user.id)))
        user = result.scalar_one_or_none()
        
        if user is None:
            user = User(
                tgid=str(event.from_user.id),
                register_date=int(time.time()),
                first_name=event.from_user.first_name,
                last_name=event.from_user.last_name,
                username=event.from_user.username,
            )
            session.add(user)
        else:
            # Update info
            user.first_name = event.from_user.first_name
            user.last_name = event.from_user.last_name
            user.username = event.from_user.username
            
        await session.commit()
        
        data["user"] = user
        return await handler(event, data)
