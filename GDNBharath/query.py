# jiosaavn/utils.py

import requests
from bs4 import BeautifulSoup
from .config import JioSaavnConfig

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
                return f"{JioSaavnConfig.BASE_URL}{song_link['href']}"
    return None
