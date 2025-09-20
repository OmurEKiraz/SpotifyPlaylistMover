# Spotify Playlist to CSV Exporter
# This script connects to the Spotify API and exports a playlist's tracks into a CSV file.
# Make sure to fill them in before running.

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import csv

# ------------------------------
# Spotify API Credentials
# ------------------------------
# Fill in your Spotify Developer credentials here
CLIENT_ID = ""        # Your Spotify Developer Client ID
CLIENT_SECRET = ""    # Your Spotify Developer Client Secret
REDIRECT_URI = ""     # Your Redirect URI (e.g., http://127.0.0.1:8888/callback)

# Scope defines what permissions the app has.
# "playlist-read-private" allows reading private playlists
SCOPE = "playlist-read-private"

# ------------------------------
# Spotify Connection
# ------------------------------
# Initialize Spotipy with OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,
    open_browser=True  # Opens browser automatically for authentication
))

# ------------------------------
# Playlist Configuration
# ------------------------------
# Insert the Spotify playlist ID you want to export
playlist_id = ""  # e.g., '37i9dQZF1DXcBWIGoYBM5M'

# Fetch basic playlist info
playlist = sp.playlist(playlist_id)
playlist_name = playlist['name']  # Playlist title
total_tracks = playlist['tracks']['total']  # Number of tracks

print(f"Getting: {playlist_name} ({total_tracks} tracks)")

# ------------------------------
# Retrieve All Tracks
# ------------------------------
# Spotipy paginates results. For playlists with many tracks, we need to loop through.
tracks = []
results = sp.playlist_items(playlist_id, limit=100, offset=0)
tracks.extend(results['items'])

# Continue fetching until no more tracks
while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])

# ------------------------------
# Write Tracks to CSV
# ------------------------------
# CSV columns: Track Name, Artists
with open(f"{playlist_name}.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Track Name", "Artists"])

    for item in tracks:
        track = item['track']
        track_name = track['name']
        # Join all artists if multiple
        artists = ", ".join([artist['name'] for artist in track['artists']])
        writer.writerow([track_name, artists])

print(f"{playlist_name} Saved to CSV: {playlist_name}.csv")
