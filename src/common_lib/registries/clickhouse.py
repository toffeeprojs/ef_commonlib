from typing import Literal
from asynch import Pool
from common_lib.settings import ClickHouseSettings
from common_lib.repositories import DatabaseUpdatesRepository, HandlerCallsRepository
from .utils import BigRegistry


class ClickHouseRegistry(
    BigRegistry[ClickHouseSettings, Pool, Literal["database_updates", "handler_calls"]]
):
    _settings_class = ClickHouseSettings
    _repository_classes = {
        "database_updates": DatabaseUpdatesRepository,
        "handler_calls": HandlerCallsRepository,
    }

    async def _get_connection(self):
        connection = Pool(
            user=self._settings.user,
            password=self._settings.password,
            host=self._settings.host,
            port=self._settings.port,
            database=self._settings.db,
        )

        await connection.startup()

        return connection

    async def _close_connection(self):
        await self._connection.shutdown()


__all__ = ["ClickHouseRegistry"]
