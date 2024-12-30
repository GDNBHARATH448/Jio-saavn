import requests
from bs4 import BeautifulSoup

def search_resso(song_name):
    """Searches for a song on Resso and returns the title and URL of the first result."""
    query = song_name.replace(' ', '%20')
    url = f'https://www.resso.com/search/{query}'
    
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        first_song = soup.find('div', class_='song-item')
        if first_song:
            song_title = first_song.find('div', class_='song-title').text.strip()
            song_url = f"https://www.resso.com{first_song.find('a')['href']}"
            song_artist = first_song.find('div', class_='song-artist').text.strip()
            return song_title, song_artist, song_url
        else:
            return None, None, None
    else:
        return None, None, None

def main():
    song_name = input("Enter the song name to search: ")
    title, artist, url = search_resso(song_name)
    if title and artist and url:
        print(f"Found song: {title}")
        print(f"Artist: {artist}")
        print(f"Listen here: {url}")
    else:
        print("Song not found.")

if __name__ == "__main__":
    main()
