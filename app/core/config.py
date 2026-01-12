

from pydantic import Field
from pydantic_settings import BaseSettings,SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    JWT_SECRET: str = Field(..., env="JWT_SECRET")
    JWT_ALG: str = Field(default="HS256", env="JWT_ALG")
    JWT_EXPIRES_MIN: int = Field(default=60*24, env="JWT_EXPIRES_MIN")
    PROJECT_NAME: str = Field(default="FastAPI Devinote", env="PROJECT_NAME")
    POSTGRES_DB: str = Field(default="devinote", env="POSTGRES_DB")
    POSTGRES_USER: str = Field(default="devinote", env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field(default="devinote_password", env="POSTGRES_PASSWORD")
    POSTGRES_HOST: str = Field(default="db", env="POSTGRES_HOST")
    POSTGRES_PORT: int = Field(default=5432, env="POSTGRES_PORT")
    

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
    
settings = Settings()

