from .utils import BaseService

try:
    from .audit import AuditService
except ModuleNotFoundError:

    class AuditService:
        def __init__(self, *args, **kwargs):
            raise ModuleNotFoundError()


try:
    from .data import DataService
except ModuleNotFoundError:

    class DataService:
        def __init__(self, *args, **kwargs):
            raise ModuleNotFoundError()


__all__ = [
    "BaseService",
    "AuditService",
    "DataService",
]
