from aiohttp import ClientSession, TCPConnector
from common_lib.settings import TelegramSettings
from common_lib.repositories import NotificationsRepository
from .utils import SmallRegistry


class TelegramRegistry(
    SmallRegistry[TelegramSettings, ClientSession, NotificationsRepository]
):
    _settings_class = TelegramSettings
    _repository_class = NotificationsRepository

    async def _get_connection(self):
        return ClientSession(
            base_url=f"https://api.telegram.org/bot{self._settings.bot_token}",
            raise_for_status=True,
            connector=TCPConnector(limit_per_host=10, keepalive_timeout=1810),
        )

    async def _close_connection(self):
        await self._connection.close()


__all__ = ["TelegramRegistry"]
