from common_lib.registries import ClickHouseRegistry, TelegramRegistry
from .utils import BaseService


class AuditService(BaseService):
    _registry_classes = {
        "clickhouse": ClickHouseRegistry,
        "telegram": TelegramRegistry
    }


__all__ = ["AuditService"]
