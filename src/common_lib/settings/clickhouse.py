from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class ClickHouseSettings(BaseSettings):
    host: str = "localhost"
    port: int = 9000
    user: str = "default"
    password: Optional[str] = None
    db: Optional[str] = None

    model_config = SettingsConfigDict(env_prefix="clickhouse_", case_sensitive=False)


__all__ = ["ClickHouseSettings"]
