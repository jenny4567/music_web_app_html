class Artist:
    def __init__(self, id, name, genre, albums = None):
        self.id = id
        self.name = name
        self.genre = genre
        self.albums = albums or []
        self.generate_errors = ''

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"{self.name}"
    
    def is_valid(self):
        required_args = [self.name, self.genre]
        if '' in required_args or None in required_args:
            self.generate_errors += 'All fields must be filled in.'
        if self.generate_errors != '':
            return False
        return True