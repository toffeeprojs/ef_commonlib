from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field

class RabbitMQSettings(BaseSettings):
    host: str = "localhost"
    port: int = 9000
    default_user: str = "guest"
    default_password: str = "guest"
    default_vhost: str = "/"

    model_config = SettingsConfigDict(env_prefix="rabbitmq_", case_sensitive=False)

    @computed_field
    @property
    def url(self) -> str:
        return f"amqp://{self.default_user}:{self.default_password}@{self.host}:{self.port}/{self.default_vhost}"

__all__ = [
    "RabbitMQSettings"
]
