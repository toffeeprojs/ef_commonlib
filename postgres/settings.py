from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, computed_field
from typing import Optional


class PostgresSettings(BaseSettings):
    host: str = "localhost"
    port: int = 5432
    user: str = "postgres"
    password: str
    database: Optional[str] = Field(None, validation_alias="db")

    model_config = SettingsConfigDict(env_prefix="postgres_", case_sensitive=False)

    @computed_field
    @property
    def dsn(self) -> str:
        return f"postgres://{self.user}:{self.password}@{self.host}:{self.port}/{self.database or self.user}"


__all__ = [
    "PostgresSettings"
]
