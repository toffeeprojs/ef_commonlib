from asyncpg import Pool
from .main import BaseRepository


class PostgresRepository(BaseRepository[Pool]):
    _connection_class = Pool


__all__ = ["PostgresRepository"]
