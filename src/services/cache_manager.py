import asyncio
import logging
from typing import List, Dict, Any
from sqlalchemy import insert
from src.database.database import AsyncSessionLocal
from src.database.models import CacheRecord

class CacheManager:
    def __init__(self, flush_interval: int = 5, max_batch_size: int = 100):
        self.flush_interval = flush_interval
        self.max_batch_size = max_batch_size
        self._batch: List[Dict[str, Any]] = []
        self._lock = asyncio.Lock()
        self._task: asyncio.Task | None = None
        self._running = False
        self.logger = logging.getLogger(__name__)

    async def add_record(self, tgid: str | None, chat_id: str, message_id: int, date: int, text: str | None):
        async with self._lock:
            self._batch.append({
                "tgid": tgid,
                "chat_id": chat_id,
                "message_id": message_id,
                "date": date,
                "text": text
            })

    async def _flush(self):
        async with self._lock:
            if not self._batch:
                return
            batch_to_insert = self._batch[:self.max_batch_size]
            self._batch = self._batch[len(batch_to_insert):]
            
        if batch_to_insert:
            try:
                async with AsyncSessionLocal() as session:
                    await session.execute(insert(CacheRecord).values(batch_to_insert))
                    await session.commit()
            except Exception as e:
                self.logger.error(f"Failed to flush cache records to db: {e}")

    async def _loop(self):
        while self._running:
            await asyncio.sleep(self.flush_interval)
            await self._flush()

    async def start(self):
        if not self._running:
            self._running = True
            self._task = asyncio.create_task(self._loop())
            self.logger.info("CacheManager started.")

    async def stop(self):
        if self._running:
            self._running = False
            if self._task:
                self._task.cancel()
                try:
                    await self._task
                except asyncio.CancelledError:
                    pass
            while self._batch:
                await self._flush()
            self.logger.info("CacheManager stopped.")

cache_manager = CacheManager()
