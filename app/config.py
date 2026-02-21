from pydantic import BaseSettings

class Settings(BaseSettings):
    TELEGRAM_TOKEN: str
    MONGO_URI: str
    COC_PROXY_URL: str
    OPENAI_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()