from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.config import config
from src.database.models import Base

engine = create_async_engine(config.database_url, echo=False)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

async def init_db():
    # Base.metadata.create_all is now handled by Alembic migrations
    pass
