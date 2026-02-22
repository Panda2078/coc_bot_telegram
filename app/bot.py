from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import settings  # tu archivo de configuración con TELEGRAM_TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola! El bot está activo.")

# Crear aplicación
app = ApplicationBuilder().token(settings.TELEGRAM_TOKEN).build()

# Agregar comandos
app.add_handler(CommandHandler("start", start))

# Ejecutar
app.run_polling()