from lib.album import Album
""" When an album is created it will contain title, release_year and artist_id

"""

def test_album_attributes_assigned():
    album = Album (1,"Pedestrian Verse", 2013, 2)
    assert album.title == "Pedestrian Verse"
    assert album.release_year == 2013
    assert album.artist_id == 2