import requests
from bs4 import BeautifulSoup

def get_song_url(song_name):
    # URL to search for the song on JioSaavn
    search_url = f'https://www.jiosaavn.com/search/{song_name}'
    
    # Send a GET request to the search URL
    response = requests.get(search_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the first song link (this part may vary depending on the page structure)
        song_link = soup.find('a', class_='u-display_block')
        if song_link:
            song_url = song_link['href']
            return f'https://www.jiosaavn.com{song_url}'
    return None

# Example usage
song_name = "Shape of You"
song_url = get_song_url(song_name)
print(f"Song URL: {song_url}")
