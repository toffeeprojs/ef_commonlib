from typing import TypeVar, Generic, Literal
from abc import ABC
from common_lib.repositories.utils import BaseRepository
from .main import BaseRegistry

_Settings = TypeVar("_Settings", bound=object)
_Connection = TypeVar("_Connection")
_Repositories = TypeVar("_Repositories", bound=Literal | str)


class BigRegistry(
    BaseRegistry[_Settings, _Connection],
    Generic[_Settings, _Connection, _Repositories],
    ABC,
):
    _repository_classes: dict[str, type[BaseRepository[_Connection]]]

    def repository(self, key: _Repositories) -> BaseRepository[_Connection] | None:
        if not hasattr(self, "_repository_classes"):
            raise NotImplementedError()

        if repository_class := self._repository_classes.get(key):
            return repository_class(self._connection)

        return None


__all__ = ["BigRegistry"]
