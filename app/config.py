import os
from pydantic import BaseSettings, ValidationError

class Settings(BaseSettings):
    TELEGRAM_TOKEN: str
    MONGO_URI: str
    COC_PROXY_URL: str
    OPENAI_API_KEY: str

    class Config:
        env_file = ".env"  # Solo para desarrollo local
        env_file_encoding = "utf-8"

try:
    settings = Settings()
except ValidationError as e:
    print("❌ Error de configuración de entorno:")
    print(e.json())
    raise