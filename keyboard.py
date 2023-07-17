import telegram
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import os 

TOKEN = os.environ["TOKEN"]

bot = telegram.Bot(TOKEN)

button1 = KeyboardButton(text='Button1', request_contact=True)
button2 = KeyboardButton(text='Button2', request_location=True)

in_button1 = InlineKeyboardButton(text='in Button1', callback_data="in_button1")
in_button2 = InlineKeyboardButton(text='in Button2', callback_data="in_button2")

buttons = [
    [in_button1],
    [in_button2]
]

keyboard = InlineKeyboardMarkup(buttons)

update = bot.getUpdates()[-1]
chat_id = update.message.chat.id

msg = bot.sendMessage(chat_id, "Keyboard", reply_markup = keyboard)

print(msg)
