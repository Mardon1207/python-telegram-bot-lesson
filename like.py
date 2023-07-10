from telegram.ext import CallbackContext, Updater, MessageHandler, Filters, CommandHandler
from telegram import Update
import json

import os 

TOKEN = os.environ['TOKEN']

def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    bot = context.bot

    bot.sendMessage(chat_id, "Bizning botga hush kelibsiz!")

like=0
dislike=0
data={
        "like":0,
        "dislike":0,
        "chat_id":[]
    }
def text(update: Update, context: CallbackContext):
    bot = context.bot
    message = update.message.text
    chat_id = update.message.chat.id
    if chat_id not in data["chat_id"]:
        data["like"]=0
        data["dislike"]=0
        data["chat_id"].append(chat_id)
    if message=="👍":
        data["like"]+=1
    if message=="👎":
        data["dislike"]+=1
    like=data["like"]
    dislike=data["dislike"]
    text = f"LIKE: {like}\nDISLIKE: {dislike}"
    
    bot.sendMessage(chat_id=chat_id, text=text)
updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, text))

updater.start_polling()

# export TOKEN='6031625012:AAFdxBk9YBo_m2U4llpFUk854ZoLXTPWSZ0'