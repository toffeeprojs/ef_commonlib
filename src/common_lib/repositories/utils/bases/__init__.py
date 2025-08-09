from .main import BaseRepository

try:
    from .postgres import PostgresRepository
except ModuleNotFoundError:

    class PostgresRepository:
        def __init__(self, *args, **kwargs):
            raise ModuleNotFoundError()


try:
    from .clickhouse import ClickHouseRepository
except ModuleNotFoundError:

    class ClickHouseRepository:
        def __init__(self, *args, **kwargs):
            raise ModuleNotFoundError()


try:
    from .rabbitmq import RabbitMQRepository
except ModuleNotFoundError:

    class RabbitMQRepository:
        def __init__(self, *args, **kwargs):
            raise ModuleNotFoundError()


try:
    from .api import ApiRepository
except ModuleNotFoundError:

    class ApiRepository:
        def __init__(self, *args, **kwargs):
            raise ModuleNotFoundError()


__all__ = [
    "BaseRepository",
    "PostgresRepository",
    "ClickHouseRepository",
    "RabbitMQRepository",
    "ApiRepository",
]
