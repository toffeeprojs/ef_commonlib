try:
    from .cmc_currencies import CMCCurrenciesRepository
    from .notifications import NotificationsRepository
    from .oer_currenies import OERCurrenciesRepository
except ModuleNotFoundError:

    class CMCCurrenciesRepository:
        def __init__(self, *args, **kwargs):
            raise ModuleNotFoundError()

    class NotificationsRepository:
        def __init__(self, *args, **kwargs):
            raise ModuleNotFoundError()

    class OERCurrenciesRepository:
        def __init__(self, *args, **kwargs):
            raise ModuleNotFoundError()


try:
    from .currencies import CurrenciesRepository
    from .exchanges import ExchangesRepository
    from .users import UsersRepository
except ModuleNotFoundError:

    class CurrenciesRepository:
        def __init__(self, *args, **kwargs):
            raise ModuleNotFoundError()

    class ExchangesRepository:
        def __init__(self, *args, **kwargs):
            raise ModuleNotFoundError()

    class UsersRepository:
        def __init__(self, *args, **kwargs):
            raise ModuleNotFoundError()


try:
    from .database_updates import DatabaseUpdatesRepository
    from .handler_calls import HandlerCallsRepository
except ModuleNotFoundError:

    class DatabaseUpdatesRepository:
        def __init__(self, *args, **kwargs):
            raise ModuleNotFoundError()

    class HandlerCallsRepository:
        def __init__(self, *args, **kwargs):
            raise ModuleNotFoundError()


try:
    from .messages import MessagesRepository
except ModuleNotFoundError:

    class MessagesRepository:
        def __init__(self, *args, **kwargs):
            raise ModuleNotFoundError()


__all__ = [
    "CMCCurrenciesRepository",
    "NotificationsRepository",
    "OERCurrenciesRepository",
    "CurrenciesRepository",
    "ExchangesRepository",
    "UsersRepository",
    "DatabaseUpdatesRepository",
    "HandlerCallsRepository",
    "MessagesRepository",
]
