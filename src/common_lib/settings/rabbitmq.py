from pydantic_settings import BaseSettings, SettingsConfigDict


class RabbitMQSettings(BaseSettings):
    host: str = "localhost"
    port: int = 9000
    default_user: str = "guest"
    default_password: str = "guest"
    default_vhost: str = "/"

    model_config = SettingsConfigDict(env_prefix="rabbitmq_", case_sensitive=False)


__all__ = ["RabbitMQSettings"]
