from aiohttp import ClientSession
from .main import BaseRepository


class ApiRepository(BaseRepository[ClientSession]):
    _connection_class = ClientSession


__all__ = ["ApiRepository"]
