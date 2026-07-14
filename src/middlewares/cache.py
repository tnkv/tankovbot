from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message
from src.services.cache_manager import cache_manager

class CacheMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        
        tgid = str(event.from_user.id) if event.from_user else None
        chat_id = str(event.chat.id)
        message_id = event.message_id
        date = int(event.date.timestamp())
        text = event.text or event.caption
        
        await cache_manager.add_record(
            tgid=tgid,
            chat_id=chat_id,
            message_id=message_id,
            date=date,
            text=text
        )
        
        return await handler(event, data)
