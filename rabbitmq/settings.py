from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, computed_field

class RabbitMQSettings(BaseSettings):
    host: str = "localhost"
    port: int = 9000
    user: str = Field("guest", validation_alias="default_user")
    password: str = Field("guest", validation_alias="default_password")
    vhost: str = Field("/", validation_alias="default_vhost")

    model_config = SettingsConfigDict(env_prefix="rabbitmq_", case_sensitive=False)

    @computed_field
    @property
    def url(self) -> str:
        return f"amqp://{self.user}:{self.password}@{self.host}:{self.port}/{self.vhost}"

__all__ = [
    "RabbitMQSettings"
]
