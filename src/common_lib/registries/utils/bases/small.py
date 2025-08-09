from typing import TypeVar, Generic
from abc import ABC
from common_lib.repositories.utils import BaseRepository
from .main import BaseRegistry

_Settings = TypeVar("_Settings", bound=object)
_Connection = TypeVar("_Connection")
_Repository = TypeVar("_Repository", bound=BaseRepository)


class SmallRegistry(
    BaseRegistry[_Settings, _Connection],
    Generic[_Settings, _Connection, _Repository],
    ABC,
):
    _repository_class: type[_Repository]

    def repository(self) -> _Repository:
        if not hasattr(self, "_repository_class"):
            raise NotImplementedError()

        return self._repository_class(self._connection)


__all__ = ["SmallRegistry"]
