
class Album:
    def __init__(self, name: str, *args) -> None:
        self.name = name
        self.songs = list(args)
        self.published = False

    def add_song(self, song) -> str:
        if self.published:
            return f"Cannot add songs. Album is published."
        elif song.name in map(lambda s: s.name, self.songs):
            return f"Song is already in the album."
        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return f"Cannot remove songs. Album is published."
        elif song_name not in map(lambda s: s.name, self.songs):
            return f"Song is not in the album."
        self.songs.remove(next(filter(lambda s: s.name == song_name, self.songs)))
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        data = f"Album {self.name}\n"
        for s in self.songs:
            data += f"== {s.get_info()}"
        return data