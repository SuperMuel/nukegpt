# create a AppSettings using pydantic-settings

from pydantic_settings import SettingsConfigDict, BaseSettings
from pydantic import Field


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    LANGCHAIN_PROJECT: str = "nukegpt"
    LANGCHAIN_API_KEY: str = Field(default=...)
    LANGCHAIN_TRACING_V2: str = "true"
