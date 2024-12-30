from pyrogram import Client
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped

api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
session_name = 'YOUR_SESSION_NAME'

app = Client(session_name, api_id, api_hash)
pytgcalls = PyTgCalls(app)

@app.on_message(filters.command("play"))
async def play(client, message):
    chat_id = message.chat.id
    song_name = message.text.split(" ", 1)[1]

    song_url = get_song_url(song_name)
    if song_url:
        await pytgcalls.join_group_call(
            chat_id,
            AudioPiped(song_url)
        )
        await message.reply(f"Playing {song_name} in voice chat.")
    else:
        await message.reply("Song not found.")

app.start()
pytgcalls.start()
idle()
