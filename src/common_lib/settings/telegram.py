from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class TelegramSettings(BaseSettings):
    bot_token: str
    chat_id: Optional[int] = None

    model_config = SettingsConfigDict(env_prefix="telegram_", case_sensitive=False)


__all__ = ["TelegramSettings"]
