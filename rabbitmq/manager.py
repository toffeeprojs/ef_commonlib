from typing import Optional
import aio_pika

from .settings import RabbitMQSettings


class RabbitMQManager:
    _connection: Optional[aio_pika.Connection] = None

    def __init__(self, settings: RabbitMQSettings):
        self.settings = settings

    async def connect(self):
        if self._connection is None:
            self._connection = await aio_pika.connect_robust(
                self.settings.url
            )
    async def disconnect(self):
        if self._connection:
            await self._connection.close()

            self._connection = None


__all__ = [
    "RabbitMQManager"
]
