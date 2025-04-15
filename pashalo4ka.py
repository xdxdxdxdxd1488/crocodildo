# bot.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

# 🔧 ЗАМЕНИ на свой токен
BOT_TOKEN = "8090911585:AAHS6ZoflPgGa51_tW7ULNTzWd1dE17uj20"

logging.basicConfig(level=logging.INFO)

# Ответы на команды
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет!")

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Тут пусто!")

async def bye(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Пока!")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ping", ping))
app.add_handler(CommandHandler("bye", bye))

print("🤖 Бот запущен!")
app.run_polling()
