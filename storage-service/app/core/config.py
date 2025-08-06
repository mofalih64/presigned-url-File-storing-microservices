from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://user:password@database:5432/files_db"
    BASE_URL: str = "http://localhost:8001"
    STATIC_DIR: str = "./static"
    presigned_secret_key: str = "super-secret"
    presigned_token_expiry: int = 900

    model_config = SettingsConfigDict(env_file=".env",
    extra="allow")

settings = Settings()
