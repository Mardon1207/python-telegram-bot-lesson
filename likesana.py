from telegram.ext import CallbackContext, Updater, MessageHandler, Filters, CommandHandler
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
import json
import os 

TOKEN = os.environ['TOKEN']

def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    bot = context.bot
    # like emoji unicode: U+1F44D
    # dislike emoji unicode: U+1F44E
    like = KeyboardButton(text = '\U0001F44D')
    dislike = KeyboardButton(text = '\U0001F44E')
    keyboard = ReplyKeyboardMarkup([
        [like, dislike]
    ], resize_keyboard=True)
    with open('data.json', 'r') as f:
        data = json.load(f)
    if chat_id not in data:
        data[chat_id] = {
            "like": 0,
            "dislike": 0,}
    bot.sendMessage(chat_id=chat_id, text="Click like or dislike", reply_markup=keyboard)

def text(update: Update, context: CallbackContext):

    with open('data.json', 'r') as f:
        data = json.load(f)
        
    like = '\U0001F44D'
    dislike = '\U0001F44E'
    bot = context.bot
    message = update.message.text
    chat_id = update.message.chat.id
    
    if message == like:
        data[f'{chat_id}']['like'] += 1
    elif message == dislike:
        data[f'{chat_id}']['dislike'] += 1

    with open('data.json', 'w') as f:
        data_json = json.dumps(data, indent=4)
        f.write(data_json)
        
    text = f"LIKE: {data[f'{chat_id}']['like']} \t DISLIKE: {data[f'{chat_id}']['dislike']}"
    bot.sendMessage(chat_id=chat_id, text=text)

updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, text))

updater.start_polling()
