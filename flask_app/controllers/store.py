from flask import render_template, redirect, session, request, flash
from flask_app import app
import spotipy
from spotipy import SpotifyClientCredentials
import requests




@app.route("/")
def store():
    headers = { 
        'TRN-api-key': 'd24c19bf-7b49-480b-9aa9-3752c5016253' #this is where we pass the headers
    }
    r = requests.get('https://api.fortnitetracker.com/v1/store', headers=headers)
    return render_template("store.html", items = r.json()) #store.html is going to take all the items in the r.json 

@app.route("/tracks")
def tracks():
    cid = "e71b5fabd02341e6b5e7a2afb7586754"
    secret = "32105716b2334de29465959d1134f2b5"
    auth_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    results = sp.search("Beyonce", type="track", limit=1)
    print(results)
    return render_template("tracks.html", tracks = results['tracks']['items'])