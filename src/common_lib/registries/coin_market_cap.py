from aiohttp import TCPConnector, ClientSession
from common_lib.settings import CoinMarketCapSettings
from common_lib.repositories import CMCCurrenciesRepository
from .utils import SmallRegistry


class CoinMarketCapRegistry(
    SmallRegistry[CoinMarketCapSettings, ClientSession, CMCCurrenciesRepository]
):
    _settings_class = CoinMarketCapSettings
    _repository_class = CMCCurrenciesRepository

    async def _get_connection(self):
        return ClientSession(
            base_url="https://pro-api.coinmarketcap.com",
            headers={"X-CMC_PRO_API_KEY": self._settings.api_key},
            raise_for_status=True,
            connector=TCPConnector(limit_per_host=2, keepalive_timeout=3660),
        )

    async def _close_connection(self):
        await self._connection.close()


__all__ = ["CoinMarketCapRegistry"]
