# 🎵 Spotify Playlist to CSV Exporter 🎵

Export any public Spotify playlist to a CSV containing track names and artists. The generated CSV can then be imported into [CSV to YouTube Playlist](https://github.com/OmurEKiraz/CSVtoYoutubePlaylist)
 to transfer songs to YouTube.

## 🚀 Features

Fetches playlist data via Spotify Web API

Saves track names and artists into a CSV file

Lightweight, fast, and easy to use

## 🛠 Requirements

Python 3.7 or higher 🐍

Spotify Developer account 🌐

Spotify API Client ID and Client Secret 🔑

Python packages: spotipy, pandas, requests

## 🔧 Step 1: Create a Spotify App

Go to the Spotify Developer Dashboard
 and log in.

Click Create an App.

Fill in the required fields (App Name, Description optional).

Add a Redirect URI (callback URL):

http://127.0.0.1:8888/callback


You can also use a secure HTTPS URL if preferred.

Save your Client ID and Client Secret.
### ⚠️ Do not share your Client ID or Client Secret publicly.

## ⚙️ Step 2: Prepare the Script

Download or clone this project folder to your computer.

Open indexlist.py in your editor and insert your Client ID and Client Secret.

Insert the Spotify playlist ID you want to export.

Make sure Python 3.7+ is installed 🐍.

Install required Python packages if you haven’t:

pip install spotipy pandas requests

## ▶️ Step 3: Run the Script

Open a terminal and navigate to the folder containing indexlist.py.

Run the script with Python:

python indexlist.py


The first run will open a browser window asking for permission to access your Spotify playlists.

This is safe because it uses your own developer account and does not share data externally 🔒.

After granting permission, the script fetches all tracks from the selected playlist and saves them to playlist.csv 📄.

## 📂 Example CSV Output
Track Name,Artist Name
Song Example 1,Artist 1
Song Example 2,Artist 2

## 📜 License

This project is licensed under the MIT License 📝
