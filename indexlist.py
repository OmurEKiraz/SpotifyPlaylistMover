import spotipy
from spotipy.oauth2 import SpotifyOAuth
import csv


CLIENT_ID = ""  #Your Spotify Developer client id
CLIENT_SECRET = "" #Your Spotify Developer client secret

REDIRECT_URI = ""  # loopback URL (e.g., http://localhost:8888/callback) or your custom URL scheme (e.g., myapp://callback)
SCOPE = "playlist-read-private"

# Spotify bağlantısı
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,
    open_browser=True
))


playlist_id = ""  #The Spotify playlist ID you want to export

# Get playlist info
playlist = sp.playlist(playlist_id)
playlist_name = playlist['name']
total_tracks = playlist['tracks']['total']

print(f"Çekiliyor: {playlist_name} ({total_tracks} şarkı)")

# Pagination for getting all tracks on bigger playlists(500+ songs)
tracks = []
results = sp.playlist_items(playlist_id, limit=100, offset=0)
tracks.extend(results['items'])

while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])

# Write to CSV
with open(f"{playlist_name}.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Track Name", "Artists"])

    for item in tracks:
        track = item['track']
        track_name = track['name']
        artists = ", ".join([artist['name'] for artist in track['artists']])
        writer.writerow([track_name, artists])

print(f"{playlist_name} CSV dosyasına kaydedildi: {playlist_name}.csv")
