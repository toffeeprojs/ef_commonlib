from typing import Literal
from asyncpg import Pool, create_pool
from common_lib.settings import PostgresSettings
from common_lib.repositories import (
    CurrenciesRepository,
    ExchangesRepository,
    UsersRepository,
)
from .utils import BigRegistry


class PostgresRegistry(
    BigRegistry[PostgresSettings, Pool, Literal["currencies", "exchanges", "users"]]
):
    _settings_class = PostgresSettings
    _repository_classes = {
        "currencies": CurrenciesRepository,
        "exchanges": ExchangesRepository,
        "users": UsersRepository,
    }

    async def _get_connection(self):
        return await create_pool(
            host=self._settings.host,
            port=self._settings.port,
            user=self._settings.user,
            password=self._settings.password,
            database=self._settings.db,
        )

    async def _close_connection(self):
        await self._connection.close()


__all__ = ["PostgresRegistry"]
