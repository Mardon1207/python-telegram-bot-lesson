from telegram.ext import CallbackContext, Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
import json
import os 
from db import LikeDB
db = LikeDB("users.json")
TOKEN = os.environ['TOKEN']

def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    bot = context.bot
    # like emoji unicode: U+1F44D
    # dislike emoji unicode: U+1F44E

    db.add_user(chat_id)
    like = InlineKeyboardButton(text = '\U0001F44D', callback_data="like")
    dislike = InlineKeyboardButton(text = '\U0001F44E', callback_data="dislike")

    keyboard = InlineKeyboardMarkup([
        [like, dislike]
    ], resize_keyboard=True)

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
        db.add_like(chat_id)
    elif message == dislike:
        db.add_dislike(chat_id)

    data = db.get_likes()[str(chat_id)]

    text = f"LIKE: {data['like']} \t DISLIKE: {data['dislike']}"
    bot.sendMessage(chat_id=chat_id, text=text)

def callback_func(update: Update, context: CallbackContext):
    query = update.callback_query
    chat_id = query.message.chat.id

    callback_data = query.data

    if callback_data == 'like':
        db.add_like(chat_id)
    elif callback_data == 'dislike':
        db.add_dislike(chat_id)

    data = db.get_likes()[str(chat_id)]

    like = InlineKeyboardButton(text = f'\U0001F44D {data["like"]}', callback_data="like")
    dislike = InlineKeyboardButton(text = f'\U0001F44E {data["dislike"]}', callback_data="dislike")

    keyboard = InlineKeyboardMarkup([
        [like, dislike]
    ], resize_keyboard=True)

    text = f"Like or Dislike: {data['like']}/{data['dislike']}"
    query.edit_message_text(text, reply_markup=keyboard)


updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, text))
updater.dispatcher.add_handler(CallbackQueryHandler(callback_func))
updater.start_polling()