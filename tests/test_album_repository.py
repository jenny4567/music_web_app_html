from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository#all
# We get a list of album objects reflecting the seed data.
# """
def test_get_all_album_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new ArtistRepository

    album = repository.all() # Get all artists

    assert album == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1)
        ]
    
'''
Create test for Albums
'''
def test_create_Album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    my_album = Album(None, "Ok Computer", 1997, 5)
    repository.create(my_album)
    assert repository.all() == [Album(1, 'Doolittle', 1989, 1), Album(2, 'Surfer Rosa', 1988, 1), Album(3, 'Ok Computer', 1997, 5)]

# '''
# Check if artist id on list function works. 
# '''    
# def test_check_artist_id(db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     repository = AlbumRepository(db_connection)    
#     assert repository.check_artist_id_valid(1) == True
#     assert repository.check_artist_id_valid(2) == True
#     assert repository.check_artist_id_valid(3) == True
#     assert repository.check_artist_id_valid(4) == True
#     assert repository.check_artist_id_valid(5) == False







# def test_find_album_record(db_connection):
#     db_connection.seed("seeds/music_library.sql") 
#     repository = AlbumRepository(db_connection) 

#     album = repository.find(2)
#     assert album == [Album('Surfer Rosa', 1988, 1)]

# '''
# Create test to find 'Dootlittle' from album_id = 1.
# '''
# def test_find_Doolittle(db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     repository = AlbumRepository(db_connection)
#     artist = repository.find_artist(1)
#     assert artist == "Pixies"

