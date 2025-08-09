from aio_pika import Connection, connect_robust
from common_lib.settings import RabbitMQSettings
from common_lib.repositories import MessagesRepository
from .utils import SmallRegistry


class RabbitMQRegistry(SmallRegistry[RabbitMQSettings, Connection, MessagesRepository]):
    _settings_class = RabbitMQSettings
    _repository_class = MessagesRepository

    async def _get_connection(self):
        return await connect_robust(
            host=self._settings.host,
            port=self._settings.port,
            login=self._settings.default_user,
            password=self._settings.default_password,
            virtualhost=self._settings.default_vhost,
        )

    async def _close_connection(self):
        await self._connection.close()


__all__ = ["RabbitMQRegistry"]
