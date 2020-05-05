import sqlite3
import pymongo
from pymongo import MongoClient

#Incoming data from front end
g_id = 1

LP1 = 0
HP1 = 100

LD1 = 0
HD1 = 1

LE1 = 0
HE1 = 1

#Connection to MongoDB server
client = MongoClient('mongodb+srv://mjneal2:Bre302th%26@playlistd-9nctl.mongodb.net/test?authSource=admin&replicaSet=Playlistd-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
db = client['Playlistd']
pg = db.Playlist_Groups

# #Test connection
# print(db.list_collection_names())

#Extracting s_ID's from group and putting in SQL serviceable format
doc = pg.find_one({'_id': g_id})
songs_list = tuple(doc["song_ids"])

#Connection to SQL server
connection = sqlite3.connect("Song.db")
cursor = connection.cursor()

#Selecting song information from SQL
sql_command = """
SELECT DISTINCT
  s.s_id as s_id,
  s.s_name as s_name,
  q.album_name as album_name,
  q.album_release_date as album_release_date,
  f.artist_names as artist_names
FROM
  Song s,

  (SELECT ap.s_id as s_id, GROUP_CONCAT(a.artist_name, ', ') as artist_names
  FROM Artist a, Artist_perform ap
  WHERE a.artist_ID = ap.artist_ID
  GROUP BY ap.s_id) f,

  (SELECT
    c.s_id as s_id,
    d.album_name as album_name,
    d.album_release_date as album_release_date
  FROM Song c, Album d
  WHERE c.album_id = d.album_id) q

WHERE s.s_id = f.s_id
AND s.s_id = q.s_id

AND s.s_id IN {songs}

AND s.s_popularity >= {LP}
AND s.s_popularity <= {HP}

AND s.s_danceability >= {LD}
AND s.s_danceability <= {HD}

AND s.s_energy >= {LE}
AND s.s_energy <= {HE}

ORDER BY s_id

LIMIT 10
;"""
# %placeholders
cursor.execute(sql_command.format(
    songs = songs_list,
    LP = LP1,
    HP = HP1,
    LD = LD1,
    HD = HD1,
    LE = LE1,
    HE = HE1
))
data = cursor.fetchall()

#Display the data
print(data)

#Save SQL changes
connection.commit()
connection.close()
