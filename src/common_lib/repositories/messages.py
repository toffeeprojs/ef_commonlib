from .utils import RabbitMQRepository


class MessagesRepository(RabbitMQRepository):
    pass


__all__ = ["MessagesRepository"]
