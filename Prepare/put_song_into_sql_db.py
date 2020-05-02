import sys
import spotipy
import sqlite3


username = 'btfjq9i9d4c3tim8adf5qln9x'
playlist_id = '37i9dQZF1EpngxJ2vk5DED'
#playlist_id = '6my95dQl1XxVAPcVlyU88A' #NCY

token = spotipy.util.prompt_for_user_token(username,
    client_id='d3a2c5cb1ea44a33b2f0dee665e22f05',
    client_secret='82802a97d56147499df1aa0ca2a88d07',
    redirect_uri='http://127.0.0.1:9090')

if not token:
    print("token issue, quit")
    sys.exit()

# login in and get the playlist by id
sp = spotipy.Spotify(auth=token)
playlist = sp.playlist(playlist_id, fields="tracks,next")

# initialize empty list
album_id = []
album_name = []
album_release_date = []
artist_id = []
artist_name = []
artist_popularity = []
s_id = []
s_name = []
s_popularity = []
s_danceability = []
s_energy = []
s_loudness = []
s_valence = []

num_songs = playlist['tracks']['total']
tracks = playlist['tracks']
while True:
    # for loop, for each song(track)
    for i, item in enumerate(tracks['items']):
        track = item['track']
        album_id.append(track['album']['id'])
        album_name.append(track['album']['name'])
        album_release_date.append(track['album']['release_date'])
        s_id.append(track['id'])
        s_name.append(track['name'])
        s_popularity.append(track['popularity'])

        # get song features
        s_features = sp.audio_features(track['id'])[0]
        s_danceability.append(s_features['danceability'])
        s_energy.append(s_features['energy'])
        s_loudness.append(s_features['loudness'])
        s_valence.append(s_features['valence'])

        # find artists
        num_artists = len(track['artists'])
        tmp_artist_id = []
        tmp_artist_name = []
        tmp_artist_popularity = []
        for j in range(num_artists):
            tmp_artist_id.append(track['artists'][j]['id'])
            tmp_artist_name.append(track['artists'][j]['name'])
            tmp_artist_popularity.append(sp.artist(track['artists'][0]['id'])['popularity'])
        artist_id.append(tmp_artist_id)
        artist_name.append(tmp_artist_name)
        artist_popularity.append(tmp_artist_popularity)
    if tracks['next'] :
        tracks = sp.next(tracks)
    else :
        break;

for i in range(num_songs):
    print(album_id[i])
    print(album_name[i])
    print(album_release_date[i])
    print(artist_id[i])
    print(artist_name[i])
    print(artist_popularity[i])
    print(s_id[i])
    print(s_name[i])
    print(s_popularity[i])
    print(s_danceability[i])
    print(s_energy[i])
    print(s_loudness[i])
    print(s_valence[i])
    print('---------------------------')
print()
print(num_songs)

# db process
conn = sqlite3.connect('Song.db')

query_insert_album = "INSERT INTO Album(album_id,album_name,album_release_date) VALUES(?,?,?);"
query_insert_song = "INSERT INTO Song(s_id,s_name,s_popularity,s_danceability,s_energy,s_loudness,s_valence,album_id) VALUES(?,?,?,?,?,?,?,?);"
query_insert_artist = "INSERT INTO Artist(artist_id,artist_name,artist_popularity) VALUES(?,?,?);"
query_insert_a_p = "INSERT INTO Artist_Perform(artist_id,s_id) VALUES(?,?);"
for i in range(num_songs):

    # insert album into db
    param = []
    param.append(album_id[i])
    param.append(album_name[i])
    param.append(album_release_date[i])
    cur = conn.cursor()
    count = cur.execute(query_insert_album,param)
    conn.commit()

    # insert song into db
    param = []
    param.append(s_id[i])
    param.append(s_name[i])
    param.append(s_popularity[i])
    param.append(s_danceability[i])
    param.append(s_energy[i])
    param.append(s_loudness[i])
    param.append(s_valence[i])
    param.append(album_id[i])
    cur = conn.cursor()
    count = cur.execute(query_insert_song,param)
    conn.commit()

    # insert artist into db
    for j in range(len(artist_id[i])) :
        param = []
        param.append(artist_id[i][j])
        param.append(artist_name[i][j])
        param.append(artist_popularity[i][j])
        cur = conn.cursor()
        count = cur.execute(query_insert_artist,param)
        conn.commit()

    # insert artist_perform info
    for j in range(len(artist_id[i])) :
        param = []
        param.append(artist_id[i][j])
        param.append(s_id[i])
        cur = conn.cursor()
        count = cur.execute(query_insert_a_p,param)
        conn.commit()
