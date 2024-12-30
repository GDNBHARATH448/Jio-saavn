from pyrogram import Client, filters

# Replace with your own API ID and API Hash
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
bot_token = 'YOUR_BOT_TOKEN'

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("play"))
async def play(client, message):
    chat_id = message.chat.id
    song_name = message.text.split(" ", 1)[1]

    song_url = get_song_url(song_name)
    if song_url:
        await message.reply(f"Playing {song_name}: {song_url}")
    else:
        await message.reply("Song not found.")

app.run()
