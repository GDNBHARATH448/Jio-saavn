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
