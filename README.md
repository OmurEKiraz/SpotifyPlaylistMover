🎵 Spotify Playlist to CSV Exporter

This tool allows you to export any public Spotify playlist into a CSV file containing track names and artist names.
The generated CSV file can then be used with other tools to transfer your playlists to YouTube or other platforms.

🚀 Features

Fetches playlist data from the Spotify Web API

Saves Track Name / Artist Name into a CSV file

Lightweight, simple, and fast setup

🛠️ Requirements

Python 3.7+

A Spotify Developer Dashboard account

Spotify API Client ID and Client Secret

Python packages: spotipy, pandas, requests

🔧 Setup & Create Spotify App

Go to the Spotify Developer Dashboard and log in.

Click Create an App.

Fill in the required fields (App Name and optional description).

Add a Redirect URI (Callback URL): http://127.0.0.1:8888/callback

You can also use a secure HTTPS domain if preferred.

Save the Client ID and Client Secret. These will be used in the script.

⚙️ Script Setup

Clone the repository or download the project folder.

Open indexlist.py and insert your Client ID and Client Secret in the appropriate fields.

Install required dependencies using pip (spotipy, pandas, requests).

▶️ Usage

Run the script from your terminal using Python.

On the first run, a browser window will open asking for your consent to access your Spotify account.

After granting permission, the script fetches all tracks from the selected playlist and saves them into a CSV file (playlist.csv).

📂 CSV Output Format

The CSV file will have the following format:

Track Name	Artist Name
Song Example 1	Artist 1
Song Example 2	Artist 2
📌 Notes

Works only with public Spotify playlists

The exported CSV can be used with other tools to transfer playlists to YouTube or other platforms
