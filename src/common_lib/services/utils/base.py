from typing import TypeVar, Generic
from common_lib.registries import BaseRegistry

_Registry = TypeVar("_Registry", bound=BaseRegistry)


class BaseService(Generic[_Registry]):
    _registry_classes: dict[str, type[_Registry]]
    _registries: dict[str, _Registry | None]

    def __init__(self, **settings: object):
        if not hasattr(self, '_registry_classes'):
            raise NotImplementedError()

        for name, registry_class in self._registry_classes.items():
            try:
                registry = registry_class(settings.get(name))
            except NotImplementedError():
                self._registries[name] = None
            else:
                self._registries[name] = registry

    async def connect(self):
        for manager in self._registries.values():
            await manager.connect()

    async def disconnect(self):
        for manager in self._registries.values():
            await manager.disconnect()


__all__ = ["BaseService"]
