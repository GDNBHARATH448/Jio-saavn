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
    API_ID = "28362850")
    API_HASH = "34f9cb93364db16fc45d003e4c81d97a")
    BOT_TOKEN = "8090896989:AAE7bk39swdkDdQYFfPJQYCP7KU3AFSKYfY")
    SESSION_STRING = "BQGwyGIAftr5-GvlLME-t62ZBQp_YyXnwGTqi1SOGBQRzcegBX3nvkj0zotHXrQDCjEq-Sth9sRcG4jjRSXqP9cG1DgnNRpmj6vjLn5bF1b0GuU7b_sBapdwh3dU3fx8EowfamyfjH56FlP9SWHX_jO8nwJkBDIB23bSXjk3L6wI7mJW4aMM_cMK83ruH3a-SUDJ0nO60eUFFtBMQ0DmInKQIJ1xsbPZbWkMXjQpvwJBcAqpKMCKKR12G-CxU7m7UgSp8njtv-K2CLDklW-Lrq3W8zY0As-u5LpRcPXFaOqvC7SiYqcAeqSBOJnaUxQF1QNhtssgoWtDjkwJ9Jpfvha1SMwUzgAAAAHETnMdAA")
    OWNER_ID = "7635867946")
    LOGGER_GROUP = "-1002141779241")
    

class MongoDBConfig:
CONNECTION_STRING = "mongodb+srv://VamsixD:VamsixD@vamsi.x7gyybv.mongodb.net/?retryWrites=true&w=majority")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/GDNBHARATH448/Jio-saavn")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)  # Fill this variable if your upstream repository is private


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
