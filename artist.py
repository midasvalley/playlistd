# Requires the PyMongo package.
# https://api.mongodb.com/python/current
import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb+srv://mjneal2:Bre302th%26@playlistd-9nctl.mongodb.net/test?authSource=admin&replicaSet=Playlistd-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
db = client['Playlistd']

# # Test if 'Top 100' collection exists in this database
# print(db.list_collection_names())


# res = client['Playlistd']['Top100'].aggregate(
# [
#     {
#         '$unwind': {
#             'path': '$items'
#         }
#     }, {
#         '$unwind': {
#             'path': '$items.track.artists'
#         }
#     }, {
#         '$match': {
#             'items.track.artists.name': 'Post Malone'
#         }
#     }, {
#         '$project': {
#             'Track': '$items.track.name',
#             'Artist': '$items.track.artists.name'
#         }
#     }
# ]
# )

# Make 2 arrays for track name and artist
