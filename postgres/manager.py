from typing import Optional
import asyncpg

from .settings import PostgresSettings


class PostgresManager:
    _pool: Optional[asyncpg.Pool] = None

    def __init__(self, settings: PostgresSettings):
        self.settings = settings

    async def connect(self):
        if self._pool is None:
            self._pool = await asyncpg.create_pool(self.settings.dsn)

    async def disconnect(self):
        if self._pool:
            await self._pool.close()

            self._pool = None


__all__ = [
    "PostgresManager"
]
