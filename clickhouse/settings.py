from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, computed_field
from typing import Optional

class ClickHouseSettings(BaseSettings):
    host: str = "localhost"
    port: int = 9000
    user: str = "default"
    password: Optional[str] = None
    database: Optional[str] = Field(None, validation_alias="db")

    model_config = SettingsConfigDict(env_prefix="clickhouse_", case_sensitive=False)

    @computed_field
    @property
    def dsn(self) -> str:
        return (
            f"clickhouse://{self.user}"
            f"{"" if self.password is None else f":{self.password}"}"
            "@{self.host}:{self.port}/{self.database or self.user}"
        )

__all__ = [
    "ClickHouseSettings"
]
