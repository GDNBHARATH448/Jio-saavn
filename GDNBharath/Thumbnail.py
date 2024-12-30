import requests
from bs4 import BeautifulSoup

def get_song_thumbnail(song_name):
    # URL to search for the song on JioSaavn
    search_url = f'https://www.jiosaavn.com/search/{song_name}'
    
    # Send a GET request to the search URL
    response = requests.get(search_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the first song link (this part may vary depending on the page structure)
        song_div = soup.find('div', class_='u-flex u-items-center u-margin-right-xs')
        if song_div:
            # Extract the thumbnail URL
            img_tag = song_div.find('img')
            if img_tag and 'src' in img_tag.attrs:
                thumbnail_url = img_tag['src']
                return thumbnail_url
    return None

# Example usage
song_name = "Shape of You"
thumbnail_url = get_song_thumbnail(song_name)
if thumbnail_url:
    print(f"Thumbnail URL: {thumbnail_url}")
else:
    print("Thumbnail not found.")
