from lib.album import Album

class AlbumRepository():

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row['id'], row['title'], row['release_year'], row['artist_id'])
            albums.append(item)
        return albums

    def find_artist(self, album_id):
        row = self._connection.execute('SELECT artists.name, albums.id, albums.title, albums.release_year, albums.artist_id FROM artists JOIN albums ON artists.id = albums.artist_id WHERE albums.id = %s',[album_id])
        item = Album(row[0]['id'],row[0]['title'], row[0]['release_year'], row[0]['artist_id'], row[0]['name'])
        return item
    
    def create(self, album):
        rows = self._connection.execute(
            'INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s,%s) RETURNING id', [album.title, album.release_year, album.artist_id]
        )
        #album.id = rows['id'][0]
        row = rows[0]
        album.id = row['id']
        return album







    '''
    Find artist name from artist_id. 
    '''
    # def find_artist(self, artist_id):
    #     name = self._connection.execute(
    #         "SELECT artists.name, albums.id " \
    #         "FROM artists JOIN albums ON artists.id = albums.artist_id " \
    #         "WHERE artists.id = %s", [artist_id])
    #     print(name)
    #     return name[0]['name']

    '''
    Delete an album record.
    '''
    # def delete(self, id):
    #     self._connection.execute(
    #         'DELETE FROM albums WHERE id = %s', [id])
        
    '''
    Function to match album id to multiple albums. 
    '''
    # def find(self, album_id):
    #     rows = self._connection.execute('SELECT artists.name, albums.id, albums.title, albums.release_year, albums.artist_id FROM artists JOIN albums ON artists.id = albums.artist_id WHERE albums.id = %s',[album_id])
    #     albums = []
    #     for row in rows:
    #         item = Album(row['id'],row['title'], row['release_year'], row['artist_id'], row['name'])
    #         albums.append(item)
    #     return albums
    
