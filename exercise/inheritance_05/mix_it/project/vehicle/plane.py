from inheritance_05.mix_it.project.vehicle.vehicle import Vehicle


class Plane(Vehicle):
    def __init__(self, available_seats, rows: int,seats_per_row: int):
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats_available = {}
        super().__init__(available_seats)

    def buy_ticket(self, row_number, tickets_count):
        if row_number > self.rows or row_number <= 0:
            return f"There is no row {row_number} in the plane!"

        current_seats_on_this_row_sold = 0
        if row_number in self.seats_available:
            current_seats_on_this_row_sold = self.seats_available[row_number]
        free_capacity = self.seats_per_row - current_seats_on_this_row_sold
        result = Vehicle.get_capacity(free_capacity, tickets_count)

        if isinstance(result, int):
            if row_number not in self.seats_available:
                self.seats_available[row_number] = 0
            self.seats_available[row_number] += tickets_count
            return tickets_count
        else:
            return f'Not enough tickets on row {row_number}!'