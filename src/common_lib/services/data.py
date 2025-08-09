from common_lib.registries import (
    CoinMarketCapRegistry,
    OpenExchRatesRegistry,
    PostgresRegistry,
    RabbitMQRegistry,
)
from .utils import BaseService


class DataService(BaseService):
    _registry_classes = {
        "coin_market_cap": CoinMarketCapRegistry,
        "open_exch_rates": OpenExchRatesRegistry,
        "postgres": PostgresRegistry,
        "rabbitmq": RabbitMQRegistry,
    }


__all__ = ["DataService"]
