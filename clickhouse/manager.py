from typing import Optional
import asynch

from .settings import ClickHouseSettings


class ClickHouseManager:
    _pool: Optional[asynch.Pool] = None

    def __init__(self):
        self.settings = ClickHouseSettings()

    async def connect(self):
        if self._pool is None:
            self._pool = asynch.Pool(dsn=self.settings.dsn)

            await self._pool.startup()

    async def disconnect(self):
        if self._pool:
            await self._pool.shutdown()

            self._pool = None

clickhouse_manager = ClickHouseManager()


__all__ = [
    "clickhouse_manager",
    "ClickHouseManager"
]
