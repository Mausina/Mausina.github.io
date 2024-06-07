from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask, render_template
import threading

TOKEN = 'TOKEN'

WEB_APP_URL = 'https://mausina.github.io/'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    username = user.username
    message = f"Hello {username}! Welcome to our Factory"


    keyboard = [
        [InlineKeyboardButton("Let's Click!⛏", web_app=WebAppInfo(url=WEB_APP_URL))],
        [InlineKeyboardButton("Visit Our Telegram Channel", url="https://t.me/exampleFactoryy111")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(message, reply_markup=reply_markup)

def run_flask():
    app.run(debug=True, use_reloader=False)

def main():
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    
    application.run_polling()

if __name__ == '__main__':
    main()