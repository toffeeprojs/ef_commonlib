from .utils import BaseRegistry

try:
    from .clickhouse import ClickHouseRegistry
except ModuleNotFoundError:

    class ClickHouseRegistry:
        def __init__(self, *args, **kwargs):
            raise ModuleNotFoundError()


try:
    from .coin_market_cap import CoinMarketCapRegistry
    from .open_exch_rates import OpenExchRatesRegistry
    from .telegram import TelegramRegistry
except ModuleNotFoundError:

    class CoinMarketCapRegistry:
        def __init__(self, *args, **kwargs):
            raise ModuleNotFoundError()

    class OpenExchRatesRegistry:
        def __init__(self, *args, **kwargs):
            raise ModuleNotFoundError()

    class TelegramRegistry:
        def __init__(self, *args, **kwargs):
            raise ModuleNotFoundError()


try:
    from .postgres import PostgresRegistry
except ModuleNotFoundError:

    class PostgresRegistry:
        def __init__(self, *args, **kwargs):
            raise ModuleNotFoundError()


try:
    from .rabbitmq import RabbitMQRegistry
except ModuleNotFoundError:

    class RabbitMQRegistry:
        def __init__(self, *args, **kwargs):
            raise ModuleNotFoundError()


__all__ = [
    "BaseRegistry",
    "ClickHouseRegistry",
    "CoinMarketCapRegistry",
    "OpenExchRatesRegistry",
    "TelegramRegistry",
    "PostgresRegistry",
    "RabbitMQRegistry",
]
