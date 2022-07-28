from pyrogram import Client, filters
from pyrogram.errors import FloodWait

app = Client("my account", api_id='19843430', api_hash='ac08d881bbdeb593c8d37b7c655b043d')

@app.on_message(filters.command("startspam") & filters.me)
def spamfoo(_, message):
    a = 1
    app.delete_messages(chat_id=message.chat.id, message_ids=message.id, revoke=True)
    try:
        times = int(message.text.split(' ')[1])
        msgtext = message.text.split(' ')[2]
        while a < times:
            try:
                message.reply_text(msgtext)
                a += 1
            except FloodWait:
                pass
    except Exception as e:
        message.reply_text(e)

app.run()