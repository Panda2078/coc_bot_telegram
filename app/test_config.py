from app.config import settings  # Esto ya funciona correctamente

print("TELEGRAM:", settings.TELEGRAM_TOKEN)
print("MONGO_URI:", settings.MONGO_URI)
print("PROXY_URL:", settings.PROXY_URL)
print("OPENAI_API_KEY:", settings.OPENAI_API_KEY)