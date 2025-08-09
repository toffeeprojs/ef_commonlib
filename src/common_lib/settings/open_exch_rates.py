from pydantic_settings import BaseSettings, SettingsConfigDict


class OpenExchRatesSettings(BaseSettings):
    api_key: str

    model_config = SettingsConfigDict(env_prefix="openexchrates_", case_sensitive=False)


__all__ = ["OpenExchRatesSettings"]
