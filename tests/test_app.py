from playwright.sync_api import Page, expect

'''
Albums page should list the albums in the albums table. 
'''
def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    div_tags = page.locator("div")
    expect(div_tags).to_have_text([
        "Doolittle\nReleased: 1989",
        "Surfer Rosa\nReleased: 1988"
    ])

'''
Each album has a dedicated page with the album name, release year and artist.
'''
def test_get_album_id1(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    div_tags = page.locator("body")  
    expect(div_tags).to_have_text("Doolittle\nRelease year: 1989\nArtist: Pixies")

def test_get_album_id2(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/2")
    div_tags = page.locator("body")  
    expect(div_tags).to_have_text("Surfer Rosa\nRelease year: 1988\nArtist: Pixies") 

'''
The pages returned by 'GET /albums should contain a link for each album listed. It should link to 'albums/<id>, where <id> is the corresponding album's id.
That page should then show information about the specific album. 
'''
def test_visit_album_page_id1(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Surfer Rosa'") 
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Surfer Rosa")

def test_visit_album_page_id2(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Doolittle'") 
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Doolittle")

'''
Each artist has a dedicated page with the artist name and genre.
'''
def test_get_artist_id1(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists/1")
    div_tags = page.locator("body")
    expect(div_tags).to_have_text("Pixies\nGenre: Rock")

def test_get_artist_id2(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists/2")
    div_tags = page.locator("body")
    expect(div_tags).to_have_text("ABBA\nGenre: Pop")

def test_get_artist_id3(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists/3")
    div_tags = page.locator("body")
    expect(div_tags).to_have_text("Taylor Swift\nGenre: Pop")

def test_get_artist_id4(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists/4")
    div_tags = page.locator("body")
    expect(div_tags).to_have_text("Nina Simone\nGenre: Jazz")

'''
Artists page should list the artists in the artists table. 
'''
def test_get_artists(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    div_tags = page.locator("div")
    expect(div_tags).to_have_text([
        "Pixies",
        "ABBA",
        "Taylor Swift",
        "Nina Simone"
    ])

'''
Artists page should link to individual artists' pages.
'''
def test_visit_artist_page_id1(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Pixies'") 
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Pixies")
    
def test_visit_artist_page_id2(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='ABBA'") 
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("ABBA")\
    
def test_visit_artist_page_i32(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Taylor Swift'") 
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Taylor Swift")

def test_visit_artist_page_id4(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Nina Simone'") 
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Nina Simone")

'''
Create a new album and see in the list of albums.
'''
def test_create_album(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Add new album'")
    page.fill("input[name=name]", "Waterloo")
    page.fill("input[name=release_year]", "1974")
    page.fill("input[name=artist_id]", "2")
    page.click("text='Add album'")
    title_element = page.locator("h1")
    expect(title_element).to_have_text("Waterloo")
    content_element = page.locator("p")
    expect(content_element).to_have_text("Release year: 1974\nArtist: ABBA")
    page.goto(f"http://{test_web_address}/albums/3")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Waterloo")

'''
When we try to create an album with empty fields the form shows an error.
'''
def test_create_album_empty_fields(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Add new album'")
    page.click("text='Add album'")
    errors_tag = page.locator("err")
    expect(errors_tag).to_have_text("All fields must be filled in.")

'''
Try to create album with invalid artist id.
'''
def test_create_album_invalid_artist_id(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Add new album'")
    page.fill("input[name=name]", "Waterloo")
    page.fill("input[name=release_year]", "1974")
    page.fill("input[name=artist_id]", "23")
    page.click("text='Add album'")
    errors_tag = page.locator("err")
    expect(errors_tag).to_have_text("Please add artist first.")

'''
Try to create album with invalid artist id and missing field.
'''
def test_create_album_double_invalid(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Add new album'")
    page.fill("input[name=name]", "Waterloo")
    page.fill("input[name=artist_id]", "23")
    page.click("text='Add album'")
    errors_tag = page.locator("err")
    expect(errors_tag).to_have_text("All fields must be filled in.Please add artist first.")

'''
Create a new artist and see in the list of albums.
'''
def test_create_artist(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Add new artist'")
    page.fill("input[name=name]", "Pink Floyd")
    page.fill("input[name=genre]", "Rock")
    page.click("text='Add artist'")
    title_element = page.locator("h1")
    expect(title_element).to_have_text("Pink Floyd")
    content_element = page.locator("p")
    expect(content_element).to_have_text("Genre: Rock")
    page.goto(f"http://{test_web_address}/artists/5")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Pink Floyd")

'''
When we try to create an artist with empty fields the form shows an error.
'''
def test_create_artist_empty_fields(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Add new artist'")
    page.click("text='Add artist'")
    errors_tag = page.locator("err")
    expect(errors_tag).to_have_text("All fields must be filled in.")







# # Tests for your routes go here

# # === Example Code Below ===

# """
# We can get an emoji from the /emoji page
# """
# def test_get_emoji(page, test_web_address): # Note new parameters
#     # We load a virtual browser and navigate to the /emoji page
#     page.goto(f"http://{test_web_address}/emoji")

#     # We look at the <strong> tag
#     strong_tag = page.locator("strong")

#     # We assert that it has the text ":)"
#     expect(strong_tag).to_have_text(":)")

# def test_get_goodbye_message(page, test_web_address):
#     page.goto(f"http://{test_web_address}/goodbye")
#     strong_tag = page.locator("strong")
#     expect(strong_tag).to_have_text("Bye!")


# """
# after running new_album successfully list_albums should return "voyage" with a 200 response code
# """
# def test_list_albums_with_one_album(db_connection, web_client):
#     db_connection.seed("seeds/music_library.sql")
#     response = web_client.get("/list_albums")
#     assert response.status_code == 200
#     assert response.data.decode("utf-8") == "Album(1, Doolittle, 1989, 1)"

# '''
# testing new_album with the above parameters should return nothing (just data added to table) and a response code of 200
# '''
# def test_add_album_to_albums(db_connection, web_client):
#     #http://localhost:5000/add_album?title=Voyage&release_year=2022&artist_id=2
#     db_connection.seed("seeds/music_library.sql")
#     post_response = web_client.post('/add_album', data={'title':'Voyage','release_year':'2022','artist_id':'2'})
#     assert post_response.status_code == 200
#     assert post_response.data.decode("utf-8") == ""
#     get_response = web_client.get("/list_albums")
#     assert get_response.status_code == 200
#     assert get_response.data.decode("utf-8") == "Album(1, Doolittle, 1989, 1)/nAlbum(2, Voyage, 2022, 2)"

# '''
# test listing all the artists in the seed table.
# '''
# def test_list_all_artists(db_connection, web_client):
#     db_connection.seed("seeds/music_library.sql")
#     response = web_client.get('/list_artists')
#     assert response.status_code == 200
#     assert response.data.decode("utf-8") == "Pixies, ABBA, Taylor Swift, Nina Simone"

# '''
# test adding a new artist.
# '''
# def test_add_artist_to_artists(db_connection, web_client):
#     db_connection.seed("seeds/music_library.sql")
#     post_response = web_client.post('/add_artist', data={'name':'Wild nothing', 'genre':'Indie'})
#     assert post_response.status_code == 200
#     assert post_response.data.decode("utf-8") == ""
#     get_response = web_client.get('/list_artists')
#     assert get_response.status_code == 200
#     assert get_response.data.decode("utf-8") == "Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing"
    

# # === End Example Code ===
