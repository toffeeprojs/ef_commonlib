from typing import Optional
import asyncpg

from .settings import PostgresSettings


class PostgresManager:
    _pool: Optional[asyncpg.Pool] = None

    def __init__(self):
        self.settings = PostgresSettings()

    async def connect(self):
        if self._pool is None:
            self._pool = await asyncpg.create_pool(self.settings.dsn)

    async def disconnect(self):
        if self._pool:
            await self._pool.close()

            self._pool = None

postgres_manager = PostgresManager()


__all__ = [
    "postgres_manager",
    "PostgresManager"
]
