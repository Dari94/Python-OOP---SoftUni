class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        name = f"{stars_count} stars Hotel"
        return Hotel(name)

    def get_room_by_number(self, room_number):
        return [room for room in self.rooms if room.number == room_number][0]

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = self.get_room_by_number(room_number)
        result =  room.take_room(people)

        if result:
            return result
        self.guests += people

    def free_room(self, room_number):
        room = self.get_room_by_number(room_number)
        guests_to_remove = room.guests
        result = room.free_room()
        if result:
            return result
        self.guests -= guests_to_remove

    def print_status(self):
        taken_rooms = ', '.join(str(room.number) for room in self.rooms if room.is_taken)
        free_rooms = ', '.join(str(room.number) for room in self.rooms if not room.is_taken)
        print(f'Hotel {self.name} has {self.guests} total guests')
        if free_rooms:
            print(f'Free rooms: {free_rooms}')
        if taken_rooms:
            print(f'Taken rooms: {taken_rooms}')


