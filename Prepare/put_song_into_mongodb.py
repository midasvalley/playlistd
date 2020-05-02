import sys
import spotipy
import pymongo

myclient = pymongo.MongoClient('mongodb+srv://mjneal2:Bre302th%26@playlistd-9nctl.mongodb.net/test?authSource=admin&replicaSet=Playlistd-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
mydb = myclient["Playlistd"]
mycol = mydb["Likes"]


username = 'btfjq9i9d4c3tim8adf5qln9x'
playlist_ids = ['37i9dQZEVXcKzM72XjQemt',
'37i9dQZF1EiTTkNtnXCuZ9',
'37i9dQZF1CAtox3ha6ytko',
'37i9dQZEVXbqdfv6ZbfTU1',
'37i9dQZF1EpnRdWrzdNhVB',
'37i9dQZF1EpDoCzO756JOR',
'37i9dQZF1Etbn0TtXgQBqB',
'37i9dQZF1EjoOWBILB0t7F',
'37i9dQZF1E9SClQchJEdVY',
'37i9dQZF1EgoGfiKX0q7Dq',
'37i9dQZF1Ejyvzv0AQ7o7O',
'37i9dQZF1EtbuWNxujK21t',
'37i9dQZF1Etf7lvaAA1woB',
'37i9dQZF1EjdnWCCvhg0au',
'37i9dQZF1EpngxJ2vk5DED']
#playlist_ids = ['6my95dQl1XxVAPcVlyU88A'] #NCY
num_playlist = len(playlist_ids)

token = spotipy.util.prompt_for_user_token(username,
    scope='user-top-read',
    client_id='d3a2c5cb1ea44a33b2f0dee665e22f05',
    client_secret='82802a97d56147499df1aa0ca2a88d07',
    redirect_uri='http://127.0.0.1:9090')

if not token:
    print("token issue, quit")
    sys.exit()

# login in and get the playlist by id
sp = spotipy.Spotify(auth=token)
user_id = 0

for playlist_id in playlist_ids:
    playlist = sp.playlist(playlist_id, fields="tracks,next")
    song_list = []
    num_songs = playlist['tracks']['total']
    tracks = playlist['tracks']
    while True:
        # for loop, for each song(track), add song id into list
        for i, item in enumerate(tracks['items']):
            track = item['track']
            song_list.append(track['id'])
        if tracks['next'] :
            tracks = sp.next(tracks)
        else :
            break;

    # insert this user into mongodb
    info = {"_id":user_id,"liked_songs":song_list}
    mycol.insert_one(info)
    user_id = user_id + 1


