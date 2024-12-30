# jiosaavn/main.py

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pymongo import MongoClient
from .config import TelegramConfig, MongoDBConfig, logger
from .utils import get_song_url

# Initialize MongoDB client
mongo_client = MongoClient(MongoDBConfig.CONNECTION_STRING)
db = mongo_client['your_database_name']
collection = db['your_collection_name']

# Initialize Telegram bot
app = Client(
    "music_bot",
    api_id=TelegramConfig.API_ID,
    api_hash=TelegramConfig.API_HASH,
    bot_token=TelegramConfig.BOT_TOKEN,
    session_string=TelegramConfig.SESSION_STRING
)

@app.on_message(filters.command("song") & filters.user(int(TelegramConfig.OWNER_ID)))
async def send_song(client, message):
    song_name = message.text.split(" ", 1)[1]
    song_url = get_song_url(song_name)
    if song_url:
        # Send a message with an inline button
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton("More Info", callback_data=f"info:{song_name}")]]
        )
        await message.reply_text(f"Here is your song: {song_url}", reply_markup=keyboard)
        logger.info(f"User {message.from_user.id} searched for {song_name}")
        collection.insert_one({"user_id": message.from_user.id, "song_name": song_name, "song_url": song_url})
    else:
        await message.reply_text("Song not found.")
        logger.error(f"User {message.from_user.id} searched for {song_name}, but it was not found")

@app.on_callback_query(filters.regex(r"^info:(.+)"))
async def callback_info(client, callback_query: CallbackQuery):
    song_name = callback_query.data.split(":")[1]
    song_url = get_song_url(song_name)
    if song_url:
        await callback_query.message.edit_text(f"More info about {song_name}: {song_url}")
    else:
        await callback_query.message.edit_text("Song not found.")

# Run the bot
if __name__ == "__main__":
    app.run()
