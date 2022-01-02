class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = []
        self.page = 0
        # self.photos = [[] for _ in range(self.pages)]
        for _ in range(self.pages):
            self.photos.append([])

    @classmethod
    def from_photo_count(cls, photo_count: int):
        new_instance = photo_count // 4
        return cls(new_instance)

    def add_photo(self, label: str):
        for page_num in range(len(self.photos)):
            if not len(self.photos[page_num]) >= 4:
                self.photos[page_num].append(label)
            return f'{label} photo added successfully'\
                   f'on page {page_num +1} slot {len(self.photos[page_num])}'
        return "No more free spots"

    def display(self):
        result = f'-----------\n'
        for page in self.photos:
            if page:
                result += ''.join('[] ' for _ in range(len(page))).strip()
            result += '\n'
            result += f'-----------\n'
        return result

album = PhotoAlbum(3)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())



album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
