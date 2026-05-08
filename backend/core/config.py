from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    API_PREFIX: str = "/api"
    DEBUG: bool = False
    ALLOWED_ORIGINS: str = ""
    OPENAI_API_KEY: str
    
    @field_validator("ALLOWED_ORIGINS")
    def parse_allowed_origins(cls, value: str) -> List[str]:
        if not value:
            return []
        else:
            cleaned_origins = []
            for origin in value.split(","):
                cleaned_origins.append(origin.strip())
            return cleaned_origins

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()