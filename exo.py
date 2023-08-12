from flask import Flask,request
import telegram
app = Flask(__name__)
TOKEN="6031625012:AAFdxBk9YBo_m2U4llpFUk854ZoLXTPWSZ0"
bot = telegram.Bot(TOKEN)
data=request.get_json()
m=0
@app.route("/bot")
def bot():
    if request.method=="POST":
        update=bot.getUpdates()
        chat_id=update[-1].message.chat.id
        if len(update)!=m:
            if update[-1].message.text!=None:
                text=update[-1].message.text
                tex=bot.send_message(chat_id,text)
                print(tex)
            if update[-1].message.photo!=None:
                photo=update[-1].message.photo[0]
                rasm=bot.send_photo(chat_id,photo)
                print(rasm)
            if update[-1].message.video!=None:
                video=update[-1].message.video.file_id
                vedio=bot.send_video(chat_id,video)
                print(vedio)
            if update[-1].message.sticker!=None:
                sticker=update[-1].message.sticker.file_id
                stiker=bot.send_sticker(chat_id,sticker)
                print(stiker)
            if update[-1].message.video_note!=None:
                vedio_note=update[-1].message.video_note.file_id
                vedio_n=bot.send_video_note(chat_id,vedio_note)
                print(vedio_n)
            if update[-1].message.contact!=None:
                name=update[-1].message.contact.first_name
                number=update[-1].message.contact.phone_number
                telifon=bot.send_contact(phone_number=number,first_name=name,chat_id=chat_id)
                print(telifon)
            if update[-1].message.audio!=None:
                audio=update[-1].message.audio.file_id
                qushiq=bot.send_audio(chat_id,audio)
                print(audio)
            if update[-1].message.voice!=None:
                voice=update[-1].message.voice.file_id
                voyes=bot.send_voice(chat_id,voice)
                print(voyes)
            if update[-1].message.document!=None:
                document=update[-1].message.document.file_id
                dokument=bot.send_document(chat_id,document)
                print(dokument)
        m=len(update)