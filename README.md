# 🎵🎶 SPOTIFY PLAYLIST TO CSV EXPORTER 🎶🎵

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

📜 License

This project is licensed under the MIT License

If you want, I can also make a fully beginner-friendly version with step-by-step screenshots and descriptions for creating the Spotify app and getting Client ID/Secret. This is extremely useful for a GitHub project.

Do you want me to make that version too?

Şunu dedin:
OK
ChatGPT:

Perfect! Here’s a beginner-friendly, step-by-step professional README for GitHub. It includes all instructions, explains each part clearly, and is designed for someone who might be new to Spotify API or Python. No code blocks to clutter the reading—just clean, readable instructions.

🎵 Spotify Playlist to CSV Exporter

This tool allows you to export any public Spotify playlist into a CSV file containing track names and artist names.
The generated CSV file can then be used with other tools to transfer your playlists to YouTube or other platforms.

🚀 Features

Fetches playlist data from the Spotify Web API

Saves Track Name / Artist Name into a CSV file

Lightweight, simple, and fast setup

Beginner-friendly instructions included

🛠️ Requirements

Python 3.7 or higher

A Spotify Developer Dashboard account

Spotify API Client ID and Client Secret

Python packages: spotipy, pandas, requests

🔧 Step 1: Create a Spotify App

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

Tip: Treat your Client Secret like a password. Do not share it publicly.

⚙️ Step 2: Prepare the Script

Download or clone the project folder to your computer.

Open indexlist.py and insert your Client ID and Client Secret in the appropriate fields.

Make sure you have Python 3 installed.

Install required Python packages (spotipy, pandas, requests) if you don’t have them.

▶️ Step 3: Run the Script

Open your terminal and navigate to the folder where indexlist.py is located.

Run the script using Python.

The first time you run it, a browser window will open asking for permission to access your Spotify account.

After granting permission, the script will fetch all tracks from your selected playlist and save them into a CSV file named playlist.csv.

📂 CSV Output Format

The CSV file will look like this:

Track Name	Artist Name
Song Example 1	Artist 1
Song Example 2	Artist 2
📌 Notes

Only public Spotify playlists can be accessed

The CSV file can be used with other tools to transfer playlists to YouTube or other platforms

You can reuse the same Spotify app for multiple playlists
