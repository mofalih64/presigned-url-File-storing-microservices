from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://user:password@database:5432/commerce_db"
    storage_service_url: str = "http://storage-service:8001"
    presigned_secret_key: str = "super-secret"
    presigned_token_expiry: int = 900

    model_config = SettingsConfigDict(env_file=".env",
    extra="allow")

settings = Settings()
