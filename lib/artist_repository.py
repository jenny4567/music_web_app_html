from lib.artist import Artist

class ArtistRepository():
    def __init__(self, connection):
        self._connection = connection
    
    # Retrieve all artists
    def all(self):
        rows = self._connection.execute("SELECT * from artists")
        artists = []
        for row in rows:
            item = Artist(row["id"], row["name"], row["genre"])
            artists.append(item)
        return artists
    
    def find(self, artist_id):
        row = self._connection.execute('SELECT * FROM artists WHERE artists.id = %s',[artist_id])
        artist = Artist(row[0]['id'],row[0]['name'], row[0]['genre'])
        return artist
    
    def create(self, artist):
        rows = self._connection.execute('INSERT INTO artists (name, genre) VALUES (%s, %s) RETURNING id', [artist.name, artist.genre])
        row = rows[0]
        artist.id = row['id']
        return artist