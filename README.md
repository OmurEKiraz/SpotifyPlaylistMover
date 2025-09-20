# 🎵 Spotify Playlist to CSV Exporter 🎵

This tool allows you to export any public Spotify playlist into a CSV file containing track names and artist names.
The generated CSV file can then be used with my other tool to transfer your playlists to YouTube.


## 🚀 Features

Fetches playlist data from the Spotify Web API

Saves Track Name / Artist Name into a CSV file

Lightweight, simple, and fast setup




## 🛠️ Requirements

Python 3.7 or higher

A Spotify Developer Dashboard account

Spotify API Client ID and Client Secret

Python packages: spotipy



## 🔧 Step 1: Create a Spotify App

Go to the Spotify Developer Dashboard
 and log in.

Click Create an App.

Fill in the required fields:

App Name: Any name you like

App Description: Optional

Add a Redirect URI (Callback URL):

Use http://127.0.0.1:8888/callback for local development

You can also use a secure HTTPS URL if you prefer

Save your Client ID and Client Secret.

You will need these for the script

### DO NOT SHARE YOUR CLIENT ID OR CLIENT SECRET



## ⚙️ Step 2: Prepare the Script

Download or clone the project folder to your computer.

Open indexlist.py and insert your Client ID and Client Secret in the appropriate fields.

Insert the ID of the playlist you want to extract

Make sure you have Python 3 installed.

Install required Python packages (spotipy, pandas, requests) if you don’t have them.



## ▶️ Step 3: Run the Script

Open your terminal and navigate to the folder where indexlist.py is located.

Run the script using Python.

The first time you run it, a browser window will open asking for permission to access your Spotify account.

After granting permission, the script will fetch all tracks from your selected playlist and save them into a CSV file named playlist.csv.

## 📜 License

This project is licensed under the MIT License 📝


## 📂 Example CSV Output Form

The CSV file will look like this:

Track Name	Artist Name
Song Example 1	,Artist 1
Song Example 2	,Artist 2


