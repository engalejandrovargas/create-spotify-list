import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up your Spotify API credentials
SPOTIPY_CLIENT_ID = '7e289c029ad14a589e6e6ac4c32dec37'
SPOTIPY_CLIENT_SECRET = 'c5c16ea91f1c4819af3a8796530dd777'
SPOTIPY_REDIRECT_URI = 'https://alejandrovargas.co/'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="playlist-modify-public",
                                               open_browser=True))


# Get the playlist ID where you want to add songs
playlist_id = '3ATAxcf8Lqbn7r5OynHDaW'

# Read the text file with song names and singers
with open('songs.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Initialize a list to store Spotify track URIs
track_uris = []

# Iterate through each line in the file
for line in lines:
    # Split the line into song name and singer
    song_name, singer = map(str.strip, line.split('-'))

    # Search for the track on Spotify
    results = sp.search(q=f"{song_name} {singer}", type='track', limit=1)

    # Print the search results for debugging
    print(f"Search results for '{song_name}' by '{singer}': {results}")

    # Check if there are any results
    if results['tracks']['items']:
        # Get the Spotify URI of the first result and add it to the list
        track_uri = results['tracks']['items'][0]['uri']
        track_uris.append(track_uri)
    else:
        print(f"Could not find '{song_name}' by '{singer}' on Spotify.")


# Add tracks to the playlist
sp.playlist_add_items(playlist_id, track_uris)

