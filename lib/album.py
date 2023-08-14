class Album():
    def __init__(self, id, title, release_year, artist_id, artist_name = None):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id
        self.artist_name = artist_name or []
        self.generate_errors = ''

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})"
    
    def is_valid(self,_connection):
        valid_ids = [str(item['id']) for item in _connection.execute('SELECT id from artists')]
        required_args = [self.title, self.release_year, self.artist_id]
        if '' in required_args or None in required_args:
            self.generate_errors += 'All fields must be filled in.'
        if (not self.artist_id in valid_ids) & (self.artist_id != '') & (self.artist_id != None):
            self.generate_errors += 'Please add artist first.'
        if self.generate_errors != '':
            return False
        return True
