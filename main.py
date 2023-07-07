from time import sleep
import telegram
import os 
TOKEN = os.environ['TOKEN']
bot = telegram.Bot(TOKEN)
m=0
while True:
    update=bot.getUpdates()
    text=update[-1].message.text
    photo=update[-1].message.photo
    video=update[-1].message.video
    sticker=update[-1].message.sticker
    vedio_note=update[-1].message.video_note
    contact=update[-1].message.contact
    chat_id=update[-1].message.chat_id
    audio=update[-1].message.audio
    voice=update[-1].message.voice
    document=update[-1].message.document
    if len(update)!=m:
        if text!=None:
            text=update[-1].message.text
            tex=bot.send_message(chat_id,text)
            print(tex)
        if photo!=None and text==None and video==None and sticker==None and vedio_note==None and contact==None and audio==None and voice==None and document==None:
            photo=update[-1].message.photo[0]
            rasm=bot.send_photo(chat_id,photo)
            print(rasm)
        if video!=None and text==None and sticker==None:
            video=update[-1].message.video.file_id
            vedio=bot.send_video(chat_id,video)
            print(vedio)
        if sticker!=None and video==None:
            sticker=update[-1].message.sticker.file_id
            stiker=bot.send_sticker(chat_id,sticker)
            print(stiker)
        if vedio_note!=None:
            vedio_note=update[-1].message.video_note.file_id
            vedio_n=bot.send_video_note(chat_id,vedio_note)
            print(vedio_n)
        if contact!=None:
            name=update[-1].message.contact.first_name
            number=update[-1].message.contact.phone_number
            telifon=bot.send_contact(phone_number=number,first_name=name,chat_id=chat_id)
            print(telifon)
        if audio!=None:
            audio=update[-1].message.audio.file_id
            qushiq=bot.send_audio(chat_id,audio)
            print(audio)
        if voice!=None:
            voice=update[-1].message.voice.file_id
            voyes=bot.send_voice(chat_id,voice)
            print(voyes)
        if document!=None:
            document=update[-1].message.document.file_id
            dokument=bot.send_document(chat_id,document)
            print(dokument)
    m=len(update)
    sleep(2)