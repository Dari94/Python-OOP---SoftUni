


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        try:
            album = next(filter(lambda a: a.name == album_name, self.albums))
            if album.published:
                return f"Album has been published. It cannot be removed."
            self.albums.remove(album)
            return f"Album {album_name} has been removed."
        except StopIteration:
            return f"Album {album_name} is not found."

    def details(self):
        data = f"Band {self.name}\n"
        for a in self.albums:
            data += a.details()
        return data


