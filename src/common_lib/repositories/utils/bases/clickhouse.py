from asynch import Pool
from .main import BaseRepository


class ClickHouseRepository(BaseRepository[Pool]):
    _connection_class = Pool


__all__ = ["ClickHouseRepository"]
