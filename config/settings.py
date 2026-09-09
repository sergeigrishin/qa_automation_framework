from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    API_BASE_URL: str

    model_config = SettingsConfigDict(env_file=".env")
