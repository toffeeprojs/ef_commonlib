from aiohttp import ClientSession, TCPConnector
from common_lib.settings import OpenExchRatesSettings
from common_lib.repositories import OERCurrenciesRepository
from .utils import SmallRegistry


class OpenExchRatesRegistry(
    SmallRegistry[OpenExchRatesSettings, ClientSession, OERCurrenciesRepository]
):
    _settings_class = OpenExchRatesSettings
    _repository_class = OERCurrenciesRepository

    async def _get_connection(self):
        return ClientSession(
            base_url="https://openexchangerates.org/api",
            headers={"Authorization": f"Token {self._settings.api_key}"},
            raise_for_status=True,
            connector=TCPConnector(limit_per_host=2, keepalive_timeout=3660),
        )

    async def _close_connection(self):
        await self._connection.close()


__all__ = ["OpenExchRatesRegistry"]
