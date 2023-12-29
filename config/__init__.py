from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='config/.env', env_file_encoding='utf-8')
    bot_token: SecretStr
    server_url: SecretStr
    db_url: SecretStr


config = Settings()
