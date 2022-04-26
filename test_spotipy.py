import spotipy
from spotipy import SpotifyClientCredentials 

cid = "e71b5fabd02341e6b5e7a2afb7586754"
secret = "32105716b2334de29465959d1134f2b5"
auth_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(auth_manager=auth_manager)
results = sp.search("Beyonce")
print(results)
