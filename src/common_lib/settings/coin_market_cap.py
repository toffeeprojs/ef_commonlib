from pydantic_settings import BaseSettings, SettingsConfigDict


class CoinMarketCapSettings(BaseSettings):
    api_key: str

    model_config = SettingsConfigDict(env_prefix="coinmarketcap_", case_sensitive=False)


__all__ = ["CoinMarketCapSettings"]
