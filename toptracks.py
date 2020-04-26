import spotipy
import json
from pprint import pprint
#from pymongo import MongoClient

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
cid ="<Client ID from Earlier>"
secret = "<Client Secret from Earlier>"
username = ""
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = 'user-library-read playlist-read-private user-top-read'
token = util.prompt_for_user_token(username, scope)
if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)


#sourcePlaylist = sp.user_playlist("isha0910", "0H3xnYMNTXJG8uR0ieLwi5")

# Print JSON playlist object returned by Spotify API
#print ("Playlist: ", sourcePlaylist)

topTracks = sp.current_user_top_tracks(100, 0, 'medium_term')

#y = json.dumps(topTracks)
#pprint(topTracks)

for track in topTracks['items']:
    print(track['name'])
    print(track['artists'][0]['name'])
    print(track['id'])

#x =  '$sourcePlaylist'
#print (x)
#jsonPlaylist = json.loads(x)
#print (jsonPlaylist["name"])


#tracks = sourcePlaylist["tracks"]
#songs = tracks["items"]
#while tracks['next']:
#    tracks = sp.next(tracks)
#    for item in tracks["items"]:
#        songs.append(item)
#ids = []
#print(len(songs))
#print(songs[0]['track']['id'])
#print(songs[1]['track']['id'])
#i = 0
#for i in range(len(songs)):
#    sp.user_playlist_add_tracks("<target user>", "<Target Playlist ID>", [songs[i]["track"]["id"]])
