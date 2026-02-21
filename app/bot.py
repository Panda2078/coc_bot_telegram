from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from app.config import settings
from app.database import mongo

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mongo.save_user(update.effective_user.id, update.effective_user.username)
    await update.message.reply_text(f"Hola {update.effective_user.first_name}! Bot activo ✅")

async def test_coC(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Proxy y bot funcionan correctamente!")

app = ApplicationBuilder().token(settings.TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("test", test_coC))

if __name__ == "__main__":
    print("Bot iniciado...")
    app.run_polling()