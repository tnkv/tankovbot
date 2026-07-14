from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message
from src.config import config
from src.utils.texts import ACCESS_DENIED

class BlockMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        if event.from_user and event.from_user.id in config.blocked_ids:
            try:
                await event.answer(ACCESS_DENIED)
            except Exception:
                pass
            return
                
        return await handler(event, data)
