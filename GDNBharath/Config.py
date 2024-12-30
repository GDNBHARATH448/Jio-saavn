import os
from dotenv import load_dotenv

# config.py

class JioSaavnConfig:
    BASE_URL = 'https://www.jiosaavn.com'
    SEARCH_URL = BASE_URL + '/search/{query}'
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    
    # Add any other configurations you may need

class JioSaavnConfig:
    BASE_URL = 'https://www.jiosaavn.com'
    SEARCH_URL = BASE_URL + '/search/{query}'
    USER_AGENT = (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    )

class TelegramConfig:
    API_ID = 'YOUR_API_ID'
    API_HASH = 'YOUR_API_HASH'
    BOT_TOKEN = 'YOUR_BOT_TOKEN'
    SESSION_STRING = 'YOUR_SESSION_STRING'
    OWNER_ID = 'YOUR_OWNER_ID'
    LOGGER_GROUP = 'YOUR_LOGGER_GROUP'

class MongoDBConfig:
    CONNECTION_STRING = 'YOUR_MONGODB_CONNECTION_STRING'

# Example of initializing a logger
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

# Get environment variables with default values
START_IMG_URL = os.getenv("START_IMG_URL", "https://default.example.com/start.jpg")
PING_IMG_URL = os.getenv("PING_IMG_URL", "https://default.example.com/ping.jpg")
PLAYLIST_IMG_URL = os.getenv("PLAYLIST_IMG_URL", "https://default.example.com/playlist.jpg")
STATS_IMG_URL = os.getenv("STATS_IMG_URL", "https://default.example.com/stats.jpg")
TELEGRAM_AUDIO_URL = os.getenv("TELEGRAM_AUDIO_URL", "https://default.example.com/telegram_audio.jpg")
TELEGRAM_VIDEO_URL = os.getenv("TELEGRAM_VIDEO_URL", "https://default.example.com/telegram_video.jpg")
STREAM_IMG_URL = os.getenv("STREAM_IMG_URL", "https://default.example.com/stream.jpg")
SOUNCLOUD_IMG_URL = os.getenv("SOUNCLOUD_IMG_URL", "https://default.example.com/soundcloud.jpg")
JIOSAAVN_IMG_URL = os.getenv("JIOSAAVN_IMG_URL", "https://default.example.com/jiosaavn.jpg")
SPOTIFY_ARTIST_IMG_URL = os.getenv("SPOTIFY_ARTIST_IMG_URL", "https://default.example.com/spotify_artist.jpg")
SPOTIFY_ALBUM_IMG_URL = os.getenv("SPOTIFY_ALBUM_IMG_URL", "https://default.example.com/spotify_album.jpg")
SPOTIFY_PLAYLIST_IMG_URL = os.getenv("SPOTIFY_PLAYLIST_IMG_URL", "https://default.example.com/spotify_playlist.jpg")
