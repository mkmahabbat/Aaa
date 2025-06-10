from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from keep_alive import keep_alive
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")

CHANNELS = [
    "https://t.me/MKClubOfficial",
    "https://t.me/+ez_75uB_qYoyYjQ1",
    "https://t.me/FreeSourceCodeHub"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("✅ Join All Channels", url=link)] for link in CHANNELS]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🚀 Please join all channels below to use the bot:", reply_markup=reply_markup)

keep_alive()

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
