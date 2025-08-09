from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class PostgresSettings(BaseSettings):
    host: str = "localhost"
    port: int = 5432
    user: str = "postgres"
    password: str
    db: Optional[str] = None

    model_config = SettingsConfigDict(env_prefix="postgres_", case_sensitive=False)


__all__ = ["PostgresSettings"]
