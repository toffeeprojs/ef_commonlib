from aio_pika import Connection
from .main import BaseRepository


class RabbitMQRepository(BaseRepository[Connection]):
    _connection_class = Connection


__all__ = ["RabbitMQRepository"]
