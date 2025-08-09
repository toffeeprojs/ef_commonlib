from typing import TypeVar, Generic

_Connection = TypeVar("_Connection")


class BaseRepository(Generic[_Connection]):
    _connection_class: type[_Connection]
    _connection: _Connection

    def __init__(self, connection: _Connection):
        if not hasattr(self, "_connection_class"):
            raise NotImplementedError()

        if not isinstance(connection, self._connection_class):
            raise TypeError()

        self._connection = connection


__all__ = ["BaseRepository"]
