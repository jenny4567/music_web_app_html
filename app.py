import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)


# Route to albums page with list of albums which link to individual album pages.
@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('albums_template.html', albums=albums)

# Route to individual album pages by album id. 
@app.route("/albums/<id>")
def get_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find_artist(id)
    return render_template('album_page_template.html', album=album)

# Route to an individual artist page by artist id.
@app.route("/artists/<id>")
def get_artist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = repository.find(id)
    return render_template('artist_page_template.html', artist=artist) 

# Route to albums page with list of albums which link to individual album pages.
@app.route('/artists')
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template('artists_template.html', artists=artists)   

@app.route('/albums/new', methods=['GET'])
def get_album_new():
    return render_template('new_album_form.html')

@app.route('/albums', methods=['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(None, request.form['name'], request.form['release_year'], request.form['artist_id'])  
    if not album.is_valid(connection):
        return render_template('new_album_form.html', error = album.generate_errors)
    repository.create(album)
    return redirect(f"/albums/{album.id}")

@app.route('/artists/new', methods=['GET'])
def get_artist_new():
    return render_template('new_artist_form.html')

@app.route('/artists', methods=['POST'])
def create_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist(None, request.form['name'], request.form['genre'])  
    if not artist.is_valid():
        return render_template('new_artist_form.html', error = artist.generate_errors)
    repository.create(artist)
    return redirect(f"/artists/{artist.id}")











# # == Example Code Below ==

# # GET /emoji
# # Returns a smiley face in HTML
# # Try it:
# #   ; open http://localhost:5000/emoji
# @app.route('/emoji', methods=['GET'])
# def get_emoji():
#     # We use `render_template` to send the user the file `emoji.html`
#     # But first, it gets processed to look for placeholders like {{ emoji }}
#     # These placeholders are replaced with the values we pass in as arguments
#     return render_template('emoji.html', emoji=':)')

# # This imports some more example routes for you to see how they work
# # You can delete these lines if you don't need them.
# from example_routes import apply_example_routes
# apply_example_routes(app)

# @app.route('/goodbye', methods=['GET'])
# def get_goodbye():
#     return render_template('goodbye.html')

# @app.route('/list_albums', methods=['GET'])
# def list_albums():
#     #connection = get_flask_database_connection(app)
#     connection = DatabaseConnection(test_mode=True)
#     connection.connect()
#     repository = AlbumRepository(connection)
#     result = repository.all()
#     if result == []:
#         return "The database has no information in it"
#     else:
#         return "/n".join(f"{album}" for album in result)

# @app.route('/add_album', methods=['POST'])
# def add_album():
#     print("In add_album method")
#     test_album = Album(None, request.form['title'], request.form['release_year'], request.form['artist_id'])
#     print(test_album)
#     #connection = get_flask_database_connection(app)
#     connection = DatabaseConnection(test_mode=True)
#     connection.connect()
#     repository = AlbumRepository(connection)
#     repository.create(test_album)
#     return '',200

# @app.route('/list_artists', methods=['GET'])
# def list_artists():
#     #connection = get_flask_database_connection(app)
#     connection = DatabaseConnection(test_mode=True)
#     connection.connect()
#     repository = ArtistRepository(connection)
#     result = repository.all()
#     if result == []:
#         return "The database has no information in it"
#     else:
#         return ", ".join(f"{artist}" for artist in result), 200    
    
# @app.route('/add_artist', methods=['POST'])
# def add_artist():
#     test_artist = Artist(None, request.form['name'], request.form['genre'])    
#     #connection = get_flask_database_connection(app)
#     connection = DatabaseConnection(test_mode=True)
#     connection.connect()
#     repository = ArtistRepository(connection)
#     repository.create(test_artist)
#     return '',200    

# # == End Example Code ==

# # These lines start the server if you run this file directly
# # They also start the server configured to use the test database
# # if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
