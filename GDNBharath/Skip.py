import requests
from bs4 import BeautifulSoup
from pyrogram import Client, filters
from config import JioSaavnConfig

# Replace with your own API ID, API Hash, and Bot Token
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
bot_token = 'YOUR_BOT_TOKEN'

app = Client("music_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Playlist management
playlist = []
current_song_index = -1

def get_song_url(song_name):
    search_url = JioSaavnConfig.SEARCH_URL.format(query=song_name)
    headers = {'User-Agent': JioSaavnConfig.USER_AGENT}
    response = requests.get(search_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        song_div = soup.find('div', class_='u-flex u-items-center u-margin-right-xs')
        if song_div:
            song_link = song_div.find('a', class_='u-display_block')
            if song_link:
                song_url = song_link['href']
                return f'{JioSaavnConfig.BASE_URL}{song_url}'
    return None

@app.on_message(filters.command("addsong"))
async def add_song(client, message):
    global playlist
    song_name = message.text.split(" ", 1)[1]
    song_url = get_song_url(song_name)
    if song_url:
        playlist.append(song_url)
        await message.reply_text(f"Added {song_name} to the playlist.")
    else:
        await message.reply_text("Song not found.")

@app.on_message(filters.command("skip"))
async def skip_song(client, message):
    global current_song_index
    if len(playlist) == 0:
        await message.reply_text("The playlist is empty.")
        return
    
    current_song_index += 1
    if current_song_index >= len(playlist):
        current_song_index = 0  # Loop back to the start of the playlist

    await message.reply_text(f"Skipping to next song: {playlist[current_song_index]}")

@app.on_message(filters.command("playlist"))
async def show_playlist(client, message):
    if len(playlist) == 0:
        await message.reply_text("The playlist is empty.")
    else:
        playlist_text = "\n".join([f"{idx + 1}. {url}" for idx, url in enumerate(playlist)])
        await message.reply_text(f"Current Playlist:\n{playlist_text}")

app.run()
