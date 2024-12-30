import requests

# Replace with your own SoundCloud client ID
CLIENT_ID = 'YOUR_CLIENT_ID'

def search_soundcloud(query):
    """Searches for tracks on SoundCloud and returns a list of track details."""
    url = f'https://api.soundcloud.com/tracks?client_id={CLIENT_ID}&q={query}&limit=5'
    response = requests.get(url)
    
    if response.status_code == 200:
        tracks = response.json()
        results = []
        for track in tracks:
            track_info = {
                'title': track['title'],
                'artist': track['user']['username'],
                'url': track['permalink_url'],
                'description': track['description']
            }
            results.append(track_info)
        return results
    else:
        print(f"Error: {response.status_code}")
        return None

def main():
    query = input("Enter the song or artist name to search: ")
    tracks = search_soundcloud(query)
    if tracks:
        for i, track in enumerate(tracks, 1):
            print(f"\nTrack {i}:")
            print(f"Title: {track['title']}")
            print(f"Artist: {track['artist']}")
            print(f"URL: {track['url']}")
            if track['description']:
                print(f"Description: {track['description']}")
    else:
        print("No tracks found.")

if __name__ == "__main__":
    main()
