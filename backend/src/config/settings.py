from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables
    """
    # Database
    database_url: str

    # JWT
    jwt_secret: str
    jwt_expiration: str = "24h"  # Default to 24 hours

    # App
    app_name: str = "Todo API"
    debug: bool = False
    version: str = "0.1.0"

    class Config:
        env_file = ".env"
        case_sensitive = True


# Create settings instance
settings = Settings()