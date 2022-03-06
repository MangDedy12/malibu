import os

from dotenv import load_dotenv
from telethon import TelegramClient, events

load_dotenv()

api_id = os.getenv("9175719")
api_hash = os.getenv("24bf733220dff7a6ede29381ef7c92c5")

phone = os.getenv("+6285743300481")
session_file = os.getenv("@Baim2bos")
password = os.getenv("TELEGRAM_PASSWORD")

toggle_auto_reply = False

client = TelegramClient(session_file, api_id, api_hash, sequential_updates=True).start(phone, password)

message = "This is auto-reply beta feature. I'm currently unavailable. Please wait, I'll check it later."

@client.on(events.NewMessage(pattern='#message', forwards=False))
async def custom_message(event):
    if event.to_id.user_id == event.from_id:
        global message
        msg = event.message.message.split(" ")
        message = ' '.join(msg[1:])
        await event.message.delete()
        await event.respond("Message set to : "+message)

@client.on(events.NewMessage(pattern='#toggle', forwards=False))
async def toggle_panel(event):
    if event.to_id.user_id == event.from_id:
        global toggle_auto_reply
        if toggle_auto_reply == False:
            toggle_auto_reply = True
        else:
            toggle_auto_reply = False
            pass
        await event.message.delete()
        await event.respond("Toggle set "+str(toggle_auto_reply))

@client.on(events.NewMessage)
async def auto_reply(event):
    global toggle_auto_reply
    if (event.is_private and toggle_auto_reply) and (event.to_id.user_id != event.from_id):
        await event.reply(message)

client.run_until_disconnected()
