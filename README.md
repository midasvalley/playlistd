# playlistd
CS 411 Project

# SQL Database
Song_empty.db -- This is a empty db with all the schema, empty tables. Store it just in case.  
Song.db       -- This is the db we will normally use.  
Song_added.db -- This is a backup, if something bad happens to Song.db, then we can replace the damaged Song.db with this one.  

# Prepare
The files here will not be used during demo. They are only for the preparation of the db. They may be useful for writing other codes  
put_song_into_mongodb.py -- Grab 14 playlist_ids (URIs) and put song_ids into Mongodb  
put_song_into_sql_db.py  -- Put song info into SQL db, but this file can only do one playlist_id (URI) at a time, so have to run this file 14 times to get all songs from the 14 playlist_ids (URIs)  
