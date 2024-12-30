import requests
from bs4 import BeautifulSoup

def search_jiosaavn(song_name):
    """Searches for a song on JioSaavn and returns the title and URL of the first result."""
    query = song_name.replace(' ', '+')
    url = f'https://www.jiosaavn.com/search/{query}'
    
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        first_song = soup.find('div', class_='o-block__header')
        if first_song:
            song_title = first_song.find('a', class_='u-color-js-gray').text.strip()
            song_url = f"https://www.jiosaavn.com{first_song.find('a', class_='u-color-js-gray')['href']}"
            return song_title, song_url
        else:
            return None, None
    else:
        return None, None

def get_song_details(song_url):
    """Retrieves details of a song from its JioSaavn URL."""
    response = requests.get(song_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        song_title = soup.find('h1', class_='page-title').text.strip()
        song_artist = soup.find('span', class_='u-color-js-gray').text.strip()
        album_art = soup.find('img', class_='u-img--block')['src']
        return song_title, song_artist, album_art
    else:
        return None, None, None

def main():
    print("Welcome to JioSaavn Helper!")
    while True:
        print("\nMenu:")
        print("1. Search for a song")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            song_name = input("Enter the song name to search: ")
            title, url = search_jiosaavn(song_name)
            if title and url:
                print(f"Found song: {title}")
                print(f"Listen here: {url}")

                # Getting song details
                song_title, song_artist, album_art = get_song_details(url)
                if song_title and song_artist and album_art:
                    print(f"Song Title: {song_title}")
                    print(f"Artist: {song_artist}")
                    print(f"Album Art: {album_art}")
                else:
                    print("Could not retrieve song details.")
            else:
                print("Song not found.")
        elif choice == '2':
            print("Exiting JioSaavn Helper. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
