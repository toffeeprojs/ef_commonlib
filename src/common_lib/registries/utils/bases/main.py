from typing import TypeVar, Generic
from abc import ABC, abstractmethod

_Settings = TypeVar("_Settings", bound=object)
_Connection = TypeVar("_Connection")


class BaseRegistry(Generic[_Settings, _Connection], ABC):
    _settings_class: type[_Settings]
    _settings: _Settings

    _connection: _Connection | None = None

    def __init__(self, settings: _Settings | None = None):
        if not hasattr(self, "_settings_class"):
            raise NotImplementedError()

        if settings:
            if not isinstance(settings, self._settings_class):
                raise TypeError()

            self._settings = settings
        else:
            self._settings = self._settings_class()

    async def connect(self):
        if self._connection is None:
            self._connection = await self._get_connection()

    async def disconnect(self):
        if self._connection:
            await self._close_connection()
            self._connection = None

    @abstractmethod
    async def _get_connection(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def _close_connection(self) -> None:
        raise NotImplementedError()


__all__ = ["BaseRegistry"]
