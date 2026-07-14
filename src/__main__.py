import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from src.config import config
from src.database.database import init_db
from src.handlers import get_routers
from src.middlewares.block import BlockMiddleware
from src.middlewares.db import DbSessionMiddleware
from src.middlewares.user import UserMiddleware
from src.middlewares.cache import CacheMiddleware
from src.services.cache_manager import cache_manager

async def on_startup(bot: Bot):
    await cache_manager.start()

async def on_shutdown(bot: Bot):
    await cache_manager.stop()

async def main():
    logging.basicConfig(
        level=logging.WARNING,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    
    await init_db()
    
    bot = Bot(
        token=config.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    
    # Register startup and shutdown
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    # Register middlewares
    dp.message.middleware(CacheMiddleware())
    dp.message.middleware(BlockMiddleware())
    dp.message.middleware(DbSessionMiddleware())
    dp.message.middleware(UserMiddleware())
    
    # Register routers
    dp.include_routers(*get_routers())
    
    logging.info("Starting bot...")
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped.")
