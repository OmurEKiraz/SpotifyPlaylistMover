# SpotifyPlaylistMover
Take your playlist and travel to youtube


You can get any public playlists id and then save them as a csv file and after that using my other tool you can transfer them to youtube playlists

First You open Spotify developers webpage and make a new app (https://developer.spotify.com/dashboard)

You must fill the loopback url as in the commented (http://127.0.0.1:8888/callback) or you should add a https domain 

Check the web API at the bottom and create app

After creating add your client secret and client id to the code



You must have atleast Python 3 

Then you move on the python files location on your terminal (e.c cd Users/Desktop/SpotifyPlaylistMover)

Then on the terminal run the script like python indexlist.py

If you made no mistakes during creating the app a browser tab will open and it will request your consent 

After you give consent it will take all the Track Name / Artist Name to the csv file

